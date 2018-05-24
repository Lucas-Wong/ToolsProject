#! /usr/bin/env python
# _*_coding:utf-8_*_

import tushare as ts
from Queue import Queue
import time
import threading
import os

stock_queue = Queue()
data_queue = Queue()
lock = threading.Lock()

class ThreadRead(threading.Thread):
    def __init__(self, queue, out_queue):
        '''
        用于根据股票代码、需要读取的日期，读取增量的日行情数据，
        :param queue:用于保存需要读取的股票代码、起始日期的列表
        :param out_queue:用于保存需要写入到数据库表的结果集列表
        :return:
        '''
        threading.Thread.__init__(self)
        self.queue = queue
        self.out_queue = out_queue
    def run(self):
        while True:
            item = self.queue.get()
            time.sleep(0.5)
            try:
                df_h_data = ts.get_h_data(item['code'], start=item['startdate'], retry_count=10, pause=0.01)
                if df_h_data is not None and len(df_h_data)>0:
                    df_h_data['secucode'] = item['code']
                    df_h_data.index.name = 'date'
                    print(df_h_data.index,item['code'],item['startdate'])
                    df_h_data['tradeday'] = df_h_data.index.strftime('%Y-%m-%d')
                    self.out_queue.put(df_h_data)
            except Exception as e:
                print(str(e))
                self.queue.put(item) # 将没有爬取成功的数据放回队列里面去，以便下次重试。
                time.sleep(10)
                continue

            self.queue.task_done()

class ThreadWrite(threading.Thread):
    def __init__(self, queue, lock, db_engine):
        '''
        :param queue: 某种形式的任务队列，此处为tushare为每个股票返回的最新日复权行情数据
        :param lock:  暂时用连接互斥操作，防止mysql高并发，后续可尝试去掉
        :param db_engine:  mysql数据库的连接对象
        :return:no
        '''
        threading.Thread.__init__(self)
        self.queue = queue
        self.lock = lock
        self.db_engine = db_engine

    def run(self):
        while True:
            item = self.queue.get()
            self._save_data(item)
            self.queue.task_done()

    def _save_data(self, item):
            with self.lock:
                try:
                    item.to_sql('cron_dailyquote', self.db_engine, if_exists='append', index=False)
                except Exception as e:  # 如果是新股，则有可能df_h_data是空对象，因此需要跳过此类情况不处理
                    print(str(e))

def main():
    '''
    用于测试多线程读取数据
    :return:
    '''
    #获取环境变量，取得相应的环境配置，上线时不需要再变更代码
    global stock_queue
    global data_queue
    config=os.getenv('FLASK_CONFIG')
    if config == 'default':
        db_url='mysql+pymysql://root:******@localhost:3306/python?charset=utf8mb4'
    else:
        db_url='mysql+pymysql://root:******@localhost:3306/test?charset=utf8mb4'
    db_engine = create_engine(db_url, echo=True)
    conn = db_engine.connect()
    # TODO 增加ts.get_stock_basics()报错的处理，如果取不到信息则直接用数据库中的股票代码信息，来获取增量信息
    # TODO 增加一个标志，如果一个股票代码的最新日期不是最新日期，则需标记该代码不需要重新获取数据，即记录该股票更新日期到了最新工作日，
    df = ts.get_stock_basics()
    df.to_sql('stock_basics',db_engine,if_exists='replace',dtype={'code': CHAR(6)})
    # 计算距离当前日期最大的工作日，以便每日定时更新
    today=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    s1=("select max(t.date) from cron_tradeday t where flag=1 and t.date <='"+ today+"'")
    selectsql=text(s1)
    maxTradeay = conn.execute(selectsql).first()
    # 计算每只股票当前加载的最大工作日期，支持重跑
    s = ("select secucode,max(t.tradeday) from cron_dailyquote t group by secucode ")
    selectsql = text(s)
    result = conn.execute(selectsql)  # 执行查询语句
    df_result = pd.DataFrame(result.fetchall())
    df_result.columns=['stockcode','max_tradeday']
    df_result.set_index(df_result['stockcode'],inplace=True)
    # 开始归档前复权历史行情至数据库当中，以便可以方便地计算后续选股模型

    for i in range(3):#使用3个线程
        t = ThreadRead(stock_queue, data_queue)
        t.setDaemon(True)
        t.start()
    for code in set(list(df.index)):
        try:
            #如果当前股票已经是最新的行情数据，则直接跳过,方便重跑。
            #print maxTradeay[0],df_result.loc[code].values[1]
            if df_result.loc[code].values[1] == maxTradeay[0]:
                continue
            startdate=getLastNdate(df_result.loc[code].values[1],1)
        except Exception as e:
            #如果某只股票没有相关的行情，则默认开始日期为2015年1月1日
            startdate='2015-01-01'
        item={}
        item['code']=code
        item['startdate']=startdate
        stock_queue.put(item) # 生成生产者任务队列
    for i in range(3):
        t = ThreadWrite(data_queue, lock, db_engine)
        t.setDaemon(True)
        t.start()
    stock_queue.join()
    data_queue.join()

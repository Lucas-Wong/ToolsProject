#! /usr/bin/env python
#_*_coding:utf-8_*_
import re
import time
import random
from selenium import webdriver
# import keys模块
from selenium.webdriver.common.keys import Keys


class Game_2048:
    """
    Game 2048
    """

    def __init__(self):
        """
        初始化函数
        """
        # 2048的矩阵列表
        self.matrix = None
        # 对应的转置矩阵
        self.matrix_tra = None
        # 打开2048的浏览器驱动实例
        self.browser = None
        self.getBrowser()
        time.sleep(1)
        self.getMatrix()
        # 键盘移动的区域, 针对body而不是2048的框
        self.body = None
        # 得分
        self.score = {'随机移动': 0, '每次最优': 0}

        # 再玩一次


    def tryAgain(self):
        """
        try again
        :return:
        """
        retry_btn = self.browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[1]/div/a[2]')
        retry_btn.click()

        # 根据账号密码进行登录


    def login(self, ac):

        """
        无论是否已登录, 都尝试先退出
        :param ac:
        :return:
        """
        try:
            logout_btn = self.browser.find_element_by_xpath('//*[@id="nav_logout"]/a')
            logout_btn.click()
            time.sleep(1)
        except:
            pass
        # 登录

        login_btn = self.browser.find_element_by_xpath('//*[@id="nav_login"]/a')
        login_btn.click()
        time.sleep(1)

        # 向元素发送键值, 并登录
        login_ac = self.browser.find_element_by_xpath('//*[@id="loginName"]')
        login_pw = self.browser.find_element_by_xpath('//*[@id="login_pwd"]')
        submit_btn = self.browser.find_element_by_xpath('//*[@id="fr_login"]/div[4]/div/button[3]')
        login_ac.send_keys(ac)
        login_pw.send_keys()
        submit_btn.click()

        '''
        import requests
        data = {'loginName':'随机移动', 'pwd':'suijiyidong','remember':'false'}
        r = requests.post('http://2048.oubk.com/login', data=data)
        print(r.text)
        '''

        '''
        # 执行js代码
        js = 'document.getElementById(\'loginName\').value =\'随机移动\';'
        self.browser.execute_script(js)
        js = 'document.getElementById(\'login_pwd\').value =\'suijiyidong\';'
        self.browser.execute_script(js)
        # 找到表单
        form = self.browser.find_element_by_xpath('//*[@id="fr_login"]')
        # 进行提交
        form.submit()
        '''
        js = '''
                function post(URL, PARAMS) {
                    var temp_form = document.createElement("form");
                    temp_form.action = URL;
                    temp_form.target = "_self";
                    temp_form.method = "post";
                    temp_form.style.display = "none";
                    for (var x in PARAMS) {
                        var opt = document.createElement("textarea");
                        opt.name = x;
                        opt.value = PARAMS[x];
                        temp_form.appendChild(opt);
                    }
                    document.body.appendChild(temp_form);
                    temp_form.submit();
                }
                '''
        # 给账号加随机数字串
        randstr = str(random.randint(100000, 2000000))
        data = "'fullName':'{}', 'pwd':'{}', 'email':'{}@qq.com'".format(ac + randstr, randstr, randstr)
        js += "post('http://2048.oubk.com/register', {" + data + "});"
        self.browser.execute_script(js)
        # 暂停2秒, 给浏览器执行js注册的时间
        time.sleep(2)
        # 刷新页面
        self.browser.get('http://2048.oubk.com/')

        self.browser.set_window_size(600, 800)
        print('提示: 当前玩家为 {}'.format(ac + randstr))

        # 打开url, 并得到驱动


    def getBrowser(self):
        """
        得到当前2048的矩阵
        :return:
        """
        self.browser = webdriver.Chrome()
        self.browser.get('http://2048.oubk.com/')



    def getMatrix(self):
        """
        清空转置矩阵及转置矩阵列表
         2048的矩阵列表
        :return:
        """
        li = [0, 0, 0, 0]
        self.matrix = [li[::] for _ in range(4)]
        # 对应的转置矩阵
        self.matrix_tra = [li[::] for _ in range(4)]

        # 获取矩阵前, 必须等一会, 否则会获取还没合并好的矩阵
        time.sleep(0.2)

        # 不能使用(.*?) 否则在移动几次后, 会匹配到不正确的数据
        s = self.browser.page_source

        # 正则寻找所有方块的位置及值
        old_tile = re.findall('<div class="tile tile-(\d+) tile-position-(\d+)-(\d+)">', s)
        new_tile = re.findall('<div class="tile tile-(\d+) tile-position-(\d+)-(\d+) tile', s)
        positions = old_tile + new_tile

        # 转换结果为矩阵(转置矩阵)
        for v, y, x in positions:
            self.matrix[int(x) - 1][int(y) - 1] = int(v)
            self.matrix_tra[int(y) - 1][int(x) - 1] = int(v)

            # 随机移动


    def run_randomMoving(self):
        self.browser.get('http://2048.oubk.com/')
        self.body = self.browser.find_element_by_tag_name('body')
        # 未弹出结束框前, 进行随机移动
        while 'Game over!' not in self.browser.page_source:
            self.move(random.choice([0, 1, 2, 3]))

        curMarks = self.browser.find_element_by_xpath \
            ('/html/body/div[2]/div/div[1]/div[1]/div/div/div[1]').text
        curMarks = int(curMarks.split('\n')[0])
        print('随机移动: 得{}分!'.format(curMarks))
        self.score['随机移动'] += curMarks

        # 每次最优


    def run_eachBest(self):
        self.browser.get('http://2048.oubk.com/')
        self.body = self.browser.find_element_by_tag_name('body')
        # 未弹出结束框前, 进行最优移动
        while 'Game over!' not in self.browser.page_source:
            self.getMatrix()
            mark_of_row_move = 0
            mark_of_col_move = 0
            # 计算水平移动的得分
            # 按行遍历矩阵
            for row in self.matrix:
                index = 0
                while index < 2:
                    if row[index] == row[index + 1]:
                        mark_of_row_move += row[index] * 2
                        index += 2
                    else:
                        index += 1
            # 计算竖直移动的得分
            # 按行遍历转置矩阵(按列遍历矩阵)
            for row in self.matrix_tra:
                index = 0
                while index < 2:
                    if row[index] == row[index + 1]:
                        mark_of_col_move += row[index] * 2
                        index += 2
                    else:
                        index += 1
            # 水平移动
            if mark_of_row_move > mark_of_col_move:
                self.move(random.choice([0, 1]))
            # 竖直移动
            elif mark_of_row_move < mark_of_col_move:
                self.move(random.choice([2, 3]))
            # 随机移动
            else:
                self.move(random.choice([0, 1, 2, 3]))

        curMarks = self.browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/div/div/div[1]').text
        curMarks = int(curMarks.split('\n')[0])
        print('每次最优: 得{}分!'.format(curMarks))
        self.score['每次最优'] += curMarks

        # 按方向移动


    def move(self, direction):
        self.body = self.browser.find_element_by_tag_name('body')
        di = {0: Keys.ARROW_LEFT,
              1: Keys.ARROW_RIGHT,
              2: Keys.ARROW_UP,
              3: Keys.ARROW_DOWN}
        self.body.send_keys(di[direction])

        # 进行下分析


    def analyze(self, times):
        self.login('随机移动')
        for _ in range(times):
            self.run_randomMoving()
            self.tryAgain()
        time.sleep(1)
        self.login('每次最优')
        for _ in range(times):
            self.run_eachBest()
            self.tryAgain()

        for k in self.score:
            print('{}: {}分'.format(k, self.score[k] / times))


Game_2048().analyze(3)
input('---')
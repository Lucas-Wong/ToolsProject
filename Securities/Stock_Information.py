#! /usr/bin/env python
# _*_coding:utf-8_*_

import tushare as ts

# 获取沪深上市公司基本情况
"""
属性
code,代码
name,名称
industry,所属行业
area,地区
pe,市盈率
outstanding,流通股本(亿)
totals,总股本(亿)
totalAssets,总资产(万)
liquidAssets,流动资产
fixedAssets,固定资产
reserved,公积金
reservedPerShare,每股公积金
esp,每股收益
bvps,每股净资
pb,市净率
timeToMarket,上市日期
undp,未分利润
perundp, 每股未分配
rev,收入同比(%)
profit,利润同比(%)
gpr,毛利率(%)
npr,净利润率(%)
holders,股东人数
"""
# listStock = ts.get_stock_basics()
# print(listStock)

# 日复权行情接口
listDay = ts.get_h_data('002337', start='2015-01-01', end='2015-03-16') #两个日期之间的前复权数据
print(listDay)
"""
parameter：
code:string,股票代码 e.g. 600848
start:string,开始日期 format：YYYY-MM-DD 为空时取当前日期
end:string,结束日期 format：YYYY-MM-DD 为空时取去年今日
autype:string,复权类型，qfq-前复权 hfq-后复权 None-不复权，默认为qfq
index:Boolean，是否是大盘指数，默认为False
retry_count : int, 默认3,如遇网络等问题重复执行的次数
pause : int, 默认 0,重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题

return：
date : 交易日期 (index)
open : 开盘价
high : 最高价
close : 收盘价
low : 最低价
volume : 成交量
amount : 成交金额
"""

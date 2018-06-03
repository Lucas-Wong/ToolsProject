# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@project = ToolsProject
@file = excel_to_oracle
@author = lucas.wang
@create_time = 2018-05-29 15:30
"""
from datetime import datetime,date
import cx_Oracle
import xlrd
import sys
import logging
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# reload(sys)
# sys.setdefaultencoding('utf8')
# 日志模块
logger = logging.getLogger("AppName")

formatter = logging.Formatter('%(asctime)s %(levelname)-5s: %(message)s')
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter
logger.addHandler(console_handler)
file_handler = logging.FileHandler("Japan-AD-20180530.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

# 读取xlxs文件，将车站保存到内存
filename = r"Lilac AD Template.xlsx"
data = xlrd.open_workbook(filename, encoding_override='utf-8')
sheetname = data.sheet_names()
sheet = data.sheet_by_index(0)
rows = sheet.nrows
cols = sheet.ncols



def to_oracle(params):
    tns_name = cx_Oracle.makedsn("iconndbdev.ariix.com", "1521", " iconndev ")
    conn = cx_Oracle.connect("iconn", "iconn", tns_name)
    cursor = conn.cursor()  # 建立Cursor光标，用此执行SQL语句
    sql = """
     INSERT INTO JPN_AD_OLD
  (    
    LILAC_ORIGINAL_ID,   LILAC_IMPORT_ID,    DIST_ID,    NEXT_RELEASE_DATE,
    NEXT_RELEASE_WEEK_ID,    WAREHOUSE_ID,    SHIPPING_METHOD,    CURRENCY_CODE,
    SHIP_TO_NAME,    SHIP_TO_PHONE,    SHIP_TO_ADDR1,    SHIP_TO_ADDR2,
    SHIP_TO_CITY,    SHIP_TO_STATE,    SHIP_TO_POSTAL_CODE,    SHIP_TO_EMAIL,
    PRODUCT_ID,    PRODUCT_LILAC_ID,    PRODUCT_NAME,    QUANTITY,    PAYMENT_TYPE
  )
  VALUES
  (
    :v0,    :v1,    :v2,    to_date(:v3, 'yyyy-MM-dd'),    :v4,    :v5,    :v6,    :v7,    :v8,    :v9,
    :v10,    :v11,    :v12,    :v13,    :v14,    :v15,    :v16,    :v17,    :v18,
    :v19,    :v20
  )
    """

    # cursor.prepare(sql)
    # cursor.executemany(None, params)
    # conn.commit()
    # print(sql)
    logger.info(params)
    cursor.execute(sql, params)
    conn.commit()
    # 执行SQL语句
    # row = cursor.fetchall()  # 调用cursor.fetchall()一次取完，cursor.fetchone()一次取一行


for row in range(rows):
    if row > 0:
        # print(sheet.row_values(row))
        colValue = ''
        colNumber = 0
        parameter = dict()
        params = []

        logger.info('Excel data'.center(50, '*'))
        logger.info(row)

        for col in sheet.row_values(row):
            if colNumber == 22:
                break

            if colNumber == 12:
                colNumber += 1
                continue

            if colNumber == 3:
                date_value = xlrd.xldate_as_tuple(col, data.datemode)
                col = str(date(*date_value[:3]).strftime('%Y/%m/%d'))

            # print(sheet.col_values(colNumber)[0])

            if isinstance(col, str):
                # colValue += '\'' + col + '\''
                # 19 name, 54 address1
                params.append(col)#.replace(u'\u30fb', u' ').replace(u'\uff7c\uff83\uff68', u' '))
                # parameter[sheet.col_values(colNumber)[0]] = col.encode("utf-8")
                # print(col)
            else:
                if colNumber == 4:
                    col = '2018' + str(int(col))
                else:
                    col = str(int(col))
                # colValue += col
                params.append(int(col))
                # parameter[sheet.col_values(colNumber)[0]] = col
                # print(col)

            # if colNumber == 21:
            #     pass
            # else:
            #     colValue += ", "
            colNumber += 1
        # print(colValue)
        # print(params)
        # params.append(colValue)
        to_oracle(params)


if __name__ == '__main__':
    pass
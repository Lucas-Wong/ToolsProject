# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@project = ToolsProject
@file = text_xlxs
@author = lucas.wang
@create_time = 2018-05-29 14:52
"""
# import  xlsxwriter
#
# workbook  = xlsxwriter.Workbook('Lilac AD Template.xlsx')
# worksheet = workbook.add_worksheet()  #()中可以加入名字
#
# worksheet.write(0, 0, 'Hello Excel')
#
# workbook.close()

import xlrd
from datetime import datetime,date

# 读取xlxs文件，将车站保存到内存
filename = r"Lilac AD Template.xlsx"
data = xlrd.open_workbook(filename)
sheetname = data.sheet_names()
sheet = data.sheet_by_index(0)
rows = sheet.nrows
cols = sheet.ncols
staName = []

for row in range(rows):
    # staName.append(sheet.row_values(row)[0])
    if row > 0:
        print(sheet.row_values(row))
        # colValue = ''
        colNumber = 0
        params = []
        for col in sheet.row_values(row):

            if colNumber == 22:
                continue

            if colNumber == 3:
                date_value = xlrd.xldate_as_tuple(col, data.datemode)
                col = str(date(*date_value[:3]).strftime('%Y/%m/%d'))


            if isinstance(col, str):
                # colValue += '\'' + col + '\''
                params.append(col)
                # print(col)
            else:
                if colNumber == 4:
                    col = '2018' + str(int(col))
                else:
                    col = str(int(col))
                # colValue += col
                params.append(int(col))
                # print(col)

            # if colNumber == 21:
            #     pass
            # else:
            #     colValue += ", "
            colNumber += 1
        # print(colValue)
        print(params)
        break

if __name__ == "__main__":
    pass

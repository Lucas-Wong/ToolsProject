# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@project = ToolsProject
@file = test_read_oracle
@author = lucas.wang
@create_time = 2018-05-29 14:21
"""
import cx_Oracle

# conn = cx_Oracle.connect(
#     "iconn/iconn@172.30.1.85:1521/iconndev"
# )  # 建立Oracle连接
# conn = cx_Oracle.connect("iconn", "iconn", "iconndbdev.ariix.com:1521/iconndev")
tns_name = cx_Oracle.makedsn("iconndbdev.ariix.com", "1521", " iconndev ")
conn = cx_Oracle.connect("iconn", "iconn", tns_name)
cursor = conn.cursor()  # 建立Cursor光标，用此执行SQL语句
sql_jpn = """
Select CUST_ID, AD_ID, ORDER_ID, COUNTRY_CODE, ERROR_CODE, ERROR_MESSAGE from (
SELECT DISTINCT CUST_ID, AD_ID, ORDER_ID, COUNTRY_CODE, ERROR_CODE, ERROR_MESSAGE FROM (
SELECT CUST_ID, AD_ID, ORDER_ID, COUNTRY_CODE, ERROR_CODE, ERROR_MESSAGE  FROM (
SELECT DISTINCT AD.CUST_ID, AD.AD_ID AS AD_ID, ORDERS.ORDER_ID AS ORDER_ID, AD.COUNTRY_CODE, JP.ERROR_CODE, JP.ERROR_MESSAGE, ROW_NUMBER() OVER (PARTITION BY AD_ID ORDER BY ORDER_ID DESC) FIRST_ONE
FROM JOB_PROC_RECORD_EXEC_RESULT JP, AD, ORDERS, AD_JOB_EXEC_RECORD job_rec
WHERE AD.AD_ID = JP.PROCESSED_RECORD_ID
AND ORDERS.AUTODELIVERY_ID = AD.AD_ID
and job_rec.WEEK_ID = ORDERS.WEEK_ID
AND orders.order_status < 20
AND JP.JOB_EXEC_DETAIL_ID = to_number(job_rec.AD_JOB_exec_detail_id)
AND trunc(job_rec.created_date) = trunc(sysdate)
AND JP.ERROR_CODE <> '200'
AND ORDERS.WEEK_ID = 201822
) WHERE FIRST_ONE = 1
UNION ALL
SELECT CUST_ID, AD_ID, NULL, COUNTRY_CODE, ERROR_CODE, ERROR_MESSAG FROM (
SELECT DISTINCT AD.CUST_ID, AD.AD_ID AS AD_ID, NULL, AD.country_code, jp.error_code as ERROR_CODE, jp.error_message as ERROR_MESSAG
FROM JOB_PROC_RECORD_EXEC_RESULT JP, AD, AD_JOB_EXEC_RECORD job_rec
WHERE AD.AD_ID = JP.PROCESSED_RECORD_ID
AND JP.JOB_EXEC_DETAIL_ID = job_rec.AD_JOB_exec_detail_id
AND JP.ERROR_CODE <> '200'
AND job_rec.WEEK_ID = 201822
AND NOT EXISTS (SELECT 1 FROM ORDERS ORD WHERE ORD.AUTODELIVERY_ID is not null and  ORD.AUTODELIVERY_ID = AD.AD_ID AND ORD.WEEK_ID = job_rec.WEEK_ID  AND ORD.ORDER_TYPE = 'ORD')
AND trunc(job_rec.created_date) = trunc(SYSDATE)
))) 
Where COUNTRY_CODE IN ('JPN')
"""
cursor.execute(sql_jpn)
# 执行SQL语句
row = cursor.fetchall()  # 调用cursor.fetchall()一次取完，cursor.fetchone()一次取一行


def GetInOutFlow(staName):  # 根据传入的车站名得到对应的车站进出站量
    sqlstr = "select t.time,t.innum,t.outnum from TARGET_STATION T where t.stationcode='{0}' order by t.time".format(
        staName
    )
    cursor.execute(sqlstr)
    InOutFlow = cursor.fetchall()  # 取出对应车站的进出站量
    return InOutFlow

cols = []
for col in cursor.description:
    cols.append(col[0])
    # print(col)

print(cols)

for x in row:
    # staName = x[0]  # 车站名字
    # InOutFlow = GetInOutFlow(staName)
    # print(InOutFlow)  # 不要直接打印将其保存到excel中
    # break

    print(x)

if __name__ == "__main__":
    pass

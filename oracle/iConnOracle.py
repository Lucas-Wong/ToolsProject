#! /usr/bin/env python
# _*_coding:utf-8_*_

import cxOracle


def update(ora):
    """

    :rtype: object
    """
    ora.Exec(r"update ad set frequency = 28 where  frequency =4 and status = 20;")

    sql = r"update AD set next_release_week_id = 201722 where ad_id in (" \
          r"select processed_record_id from job_proc_record_exec_result where error_code <> '200' and error_code in " \
          r"('7404', '7405', '7407', '7411', '7412', '7413', '7414', '7415', '7416', '7419') " \
          r"and job_exec_detail_id in ( select distinct  ad_job_exec_detail_id  from ad_job_exec_record where week_id = 201722 )) " \
          r"and not exists (select 1 from orders a where a.week_id  = 201722 and a.order_type = 'ORD' and  a.cust_id = ad.cust_id ) " \
          r"and status = 20"
    ora.Exec(sql)

    sql = r"update AD set SHIP_METHOD_ID = 1 where COUNTRY_CODE = 'USA' and WAREHOUSE_ID = 1 and SHIP_METHOD_ID in (4, 10)"
    ora.Exec(sql)

    sql = "UPDATE ADDRESS_REQUIRED_RULE SET PHONE = null WHERE COUNTRY_CODE in ('CHN', 'HKG')"
    ora.Exec(sql)

    sql = "UPDATE ADDRESS_REQUIRED_RULE SET EMAIL = null WHERE COUNTRY_CODE NOT IN ('JPN', 'KWR')"
    ora.Exec(sql)

    sql = "update ADDRESS_REQUIRED_RULE set POSTAL_CODE = null where COUNTRY_CODE in ('CHN')"
    ora.Exec(sql)


def checkRunAD(ora):
    """

    :param ora:
    :return:
    """
    sql = "select job_exec_detail_id from job_execution_detail where end_time is null and start_time > sysdate -1 " \
          "order by job_exec_detail_id desc"
    rs = ora.Query(sql)

    parme = '('

    for row in rs:
        for col in row:
            parme += str(col) + ','

    parme = parme[:-1]
    parme += ')'
    print(str(parme))
    # parm = {'id': str(parme)}
    sql = r"select sum(total_records_count), sum(success_records_count), sum(faild_records_count) " \
          r"from job_execution_detail where job_exec_detail_id in " + str(parme)
    print(sql)
    rss = ora.Query(sql)
    print(rss)


def checkRunAD2(ora):
    """

    :param ora:
    :return:
    """
    sql = r"select job_exec_detail_id from job_execution_detail where end_time is null and start_time > sysdate -1 " \
          r"order by job_exec_detail_id desc"
    rs = ora.Query(sql)
    print(rs)

    parm = ''
    for row in rs:
        for col in row:
            parm += '(select count(1) from job_proc_record_exec_result where Job_exec_detail_id = ' + str(col) + '), '

    parm = parm[:-2]

    sql = "select " + parm + " from dual"

    rss = ora.Query(sql)
    print(rss)

    '''
    for row in rss:
       for col in row:
    '''


def main():
    """
        this is main function
        text connent string
        tns = r'(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=iconndbdev.ariix.com)(PORT=1521)))(CONNECT_DATA=(SERVICE_NAME=iconndev)))'
        tns = r'jdbc:oracle:thin:@iconndbdev.ariix.com:1521:iconndev'
        tns = r'jdbc:oracle:thin:@172.30.1.85:1521:iconndev'
        tns = r'iconn/iconn@iconndbdev.ariix.com:1521/iconndev'
        tns = r'iconn/iconn@172.30.1.85:1521/iconndev'
    """
    tns = r'(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=172.30.1.85)(PORT=1521)))(CONNECT_DATA=(SID=iconndev)))'
    ora = cxOracle.cxOracle('iconn', 'iconn', tns)
    # checkRunAD2(ora)
    update(ora)


if __name__ == '__main__':
    main()

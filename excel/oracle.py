# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@project = ToolsProject
@file = oracle
@author = lucas.wang
@create_time = 2018-05-30 17:51
"""

import cx_Oracle


class Oracle(object):
    """ Oracle db operator """

    def __init__(self, user_name, password, host, instance):
        self._conn = None
        if not self._conn:
            tns_name = cx_Oracle.makedsn(host, "1521", instance)
            self._conn = cx_Oracle.connect(user_name, password, tns_name)
            self.cursor = self._new_cursor()
        else:
            pass

    def _new_cursor(self):
        cur = self._conn.cursor()
        if cur:
            return cur
        else:
            print("#Error# Get New Cursor Failed.")
            return None

    # 检查是否允许执行的sql语句
    def _permited_update_sql(self, sql):
        """Check the SQL statement that is allowed to be executed"""
        rt = True
        lrsql = sql.lower()
        sql_elems = [lrsql.strip().split()]

        # update和delete最少有四个单词项
        if len(sql_elems) < 4:
            rt = False
        # 更新删除语句，判断首单词，不带where语句的sql不予执行
        elif sql_elems[0] in ["update", "delete"]:
            if "where" not in sql_elems:
                rt = False

        return rt

    # 导出结果为文件,txt
    def Export(self, sql, file_name, colfg="||"):
        rt = self.query_all(sql)
        if rt:
            with open(file_name, "a") as fd:
                for row in rt:
                    ln_info = ""
                    for col in row:
                        ln_info += str(col) + colfg
                    ln_info += "\n"
                    fd.write(ln_info)

    def query_title(self, sql, name_params={}):

        col_names = []

        if not self.cursor:
            return col_names

        if len(name_params) > 0:
            self.cursor.execute(sql, name_params)
        else:
            self.cursor.execute(sql)

        for i in range(0, len(self.cursor.description)):
            col_names.append(self.cursor.description[i][0])

        return col_names

    def query_one(self, sql):

        rt = None

        if not self.cursor:
            return rt

        self.cursor.execute(sql)
        rt = self.cursor.fetchone()

        return rt

    def query_all_by(self, sql, name_params={}):

        rt = None

        if not self.cursor:
            return rt

        if len(name_params) > 0:
            self.cursor.execute(sql, name_params)
        else:
            self.cursor.execute(sql)

        rt = self.cursor.fetchall()

        return rt

    def insert_betch(self, sql, name_params=[]):
        """ batch insert much rows one time, use location parameter"""

        rt = None

        if not self.cursor:
            return rt

        self.cursor.prepare(sql)
        self.cursor.executemany(None, name_params)
        self.commit()

        return rt

    def update_deleter_exec(self, sql):
        """ Update or Deleter mast have where"""
        # 获取cursor
        rt = None

        if not self.cursor:
            return rt

        # 判断sql是否允许其执行
        if not self._permited_update_sql(sql):
            return rt

        # 执行语句
        rt = self.cursor.execute(sql)

        return rt

    def commit(self):
        self._conn.commit()

    def __del__(self):
        if hasattr(self, "cursor"):
            self.cursor.close()

        if hasattr(self, "_conn"):
            self._conn.close()


if __name__ == "__main__":
    # ARIIX dev
    oraDb = Oracle("iconn", "iconn", "iconndbdev.ariix.com", " iconndev ")
    # ARIIX master
    # oraDb = Oracle('iconn', 'iconn', '172.30.1.98', ' ariix ')
    # MaVie dev
    # oraDb = Oracle('iconn', 'iconn', '172.16.1.96', ' iconnd ')
    # MaVie master
    # oraDb = Oracle('iconn', 'iconn', '172.30.1.168', ' mavie ')
    cursor = oraDb.cursor

    sql = """ select * from country"""
    # print(oraDb.query_all_by(sql))
    print(oraDb.query_one(sql))

    sql = """ select * from country where country_code = :id"""
    print(oraDb.query_all_by(sql, {"id": "AUS"}))

    # create_table = """
    #     CREATE TABLE python_modules (
    #     module_name VARCHAR2(50) NOT NULL,
    #     file_path VARCHAR2(300) NOT NULL
    #     )
    #     """
    # from sys import modules
    #
    # cursor.execute(create_table)
    # M = []
    # for m_name, m_info in modules.items():
    #     try:
    #         M.append((m_name, m_info.__file__))
    #     except AttributeError:
    #         pass
    #
    # sql = "INSERT INTO python_modules(module_name, file_path) VALUES (:1, :2)"
    # oraDb.insert_betch(sql, M)

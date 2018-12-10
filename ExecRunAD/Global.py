# _*_ coding:utf-8 _*_
"""
-----------------------------------------------------------
 Name：            ToolsProject/Global.py
 Purpose：         

 Author：          lucas.wang

 Created：         2018-07-30
 Copyright：       (C) lucas.wang 2018
 Licence:          MIT
 ----------------------------------------------------------
"""
# ! /usr/bin/env python

global Master_1_Url
global Master_2_Url
global Common_Week
global Job_Id_List
global Job_Done_Int
global Job_Total_Count_Dict
global Is_Run

def set_master_1_url(value):
    global Master_1_Url
    Master_1_Url = value

def get_master_1_url():
    global Master_1_Url
    return Master_1_Url

def set_master_2_url(value):
    global Master_2_Url
    Master_2_Url = value

def get_master_2_url():
    global Master_2_Url
    return Master_2_Url

def set_comm_week(value):
    global Common_Week
    Common_Week = value

def get_comm_week():
    global Common_Week
    return Common_Week

def set_job_id_list(value):
    global Job_Id_List
    Job_Id_List = value

def get_job_id_list():
    global Job_Id_List
    return Job_Id_List

def set_job_done(value):
    global Job_Done_Int
    Job_Done_Int = value

def get_job_done():
    global Job_Done_Int
    return Job_Done_Int

def set_job_total_count(value):
    global Job_Total_Count_Dict
    Job_Total_Count_Dict = value

def get_job_total_count():
    global Job_Total_Count_Dict
    return Job_Total_Count_Dict

def set_is_run(value):
    global Is_Run
    Is_Run = value

def get_is_run():
    global Is_Run
    return Is_Run

if __name__ == '__main__':
    pass
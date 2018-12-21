# _*_ coding:utf-8 _*_
"""
-----------------------------------------------------------
 Name：            ToolsProject/Run_AD
 Purpose：         

 Author：          lucas.wang

 Created：         2018-07-30
 Copyright：       (C) lucas.wang 2018
 Licence:          MIT
 ----------------------------------------------------------
"""
# ! /usr/bin/env python

import Global
import json
import time
import Parameter
import Execute
import Global
import logging
import logging.config
import os

filepath = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(filepath)
logger_name = "AppName"
logger = logging.getLogger(logger_name)

class run_ad(object):

    def __init__(self):
        pass

    def main(self, is_all):
        """
        Run AD main function
        :param is_all:
        :return:
        """

        Job_id_list = []
        Job_done = 0
        Job_total_count = {}

        parameter_function = Parameter.parameter(Global.get_comm_week(), 0)

        if str("all") == str(is_all):
            run_country = parameter_function.AllCountry()
            return_code = self.Exce(Global.get_master_1_url(), run_country)

            run_ad_object = json.loads(return_code)

            Job_id_list = [run_ad_object["data"]["jobExecutationId"]]
            Job_done = 1
            Job_total_count[run_ad_object["data"]["jobExecutationId"]] = run_ad_object["data"]["totalAdCount"]

            logger.info(run_ad_object)
        else:
            run_country = parameter_function.JPN()
            return_code = self.Exce(Global.get_master_1_url(), run_country)

            run_ad_object = json.loads(return_code)

            Job_id_list.append([run_ad_object["data"]["jobExecutationId"]])
            Job_total_count[run_ad_object["data"]["jobExecutationId"]] = run_ad_object["data"]["totalAdCount"]

            logger.info(run_ad_object)

            run_country = parameter_function.CHN()
            return_code = self.Exce(Global.get_master_2_url(), run_country)

            run_ad_object = json.loads(return_code)

            Job_id_list.append([run_ad_object["data"]["jobExecutationId"]])
            Job_total_count[run_ad_object["data"]["jobExecutationId"]] = run_ad_object["data"]["totalAdCount"]

            logger.info(run_ad_object)

            run_country = parameter_function.USA()
            return_code = self.Exce(Global.get_master_2_url(), run_country)

            run_ad_object = json.loads(return_code)

            Job_id_list.append([run_ad_object["data"]["jobExecutationId"]])
            Job_total_count[run_ad_object["data"]["jobExecutationId"]] = run_ad_object["data"]["totalAdCount"]

            logger.info(run_ad_object)

            run_country = parameter_function.Other()
            return_code = self.Exce(Global.get_master_2_url(), run_country)

            run_ad_object = json.loads(return_code)

            Job_id_list.append([run_ad_object["data"]["jobExecutationId"]])
            Job_total_count[run_ad_object["data"]["jobExecutationId"]] = run_ad_object["data"]["totalAdCount"]

            logger.info(run_ad_object)

            Job_done = 4

        Global.set_job_id_list(Job_id_list)
        Global.set_job_done(Job_done)
        Global.set_job_total_count(Job_total_count)


    def Exce(self, url, run_country):
        run_job = Execute.execute(url)
        response = run_job.post(run_country)
        logger.info("1************************")
        logger.info(response.status_code)

        if response.status_code is not 200:
            time.sleep(30)
            self.Exce(url, run_country)
        else:
            return json.loads(response.text)["string"]

if __name__ == '__main__':
    pass

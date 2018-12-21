# _*_ coding:utf-8 _*_
"""
-----------------------------------------------------------
 Name：            ToolsProject/Run
 Purpose：         

 Author：          lucas.wang

 Created：         2018-07-30
 Copyright：       (C) lucas.wang 2018
 Licence:          MIT
 ----------------------------------------------------------
"""
# ! /usr/bin/env python

import time
import Run_AD
import Monitor_AD
import Global
import logging
import logging.config
import os

filepath = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(filepath)
logger_name = "AppName"
logger = logging.getLogger(logger_name)

class init_run(object):

    def __init__(self):
        pass

    def run(self, is_all="other"):
        run_ad = Run_AD.run_ad()
        run_ad.main(is_all)

        monitor_ad = Monitor_AD.monitor_ad()
        monitor_ad.main()

    def main(self):
        t = time.localtime()
        h = t.tm_hour
        m = t.tm_min
        s = t.tm_sec
        w = time.strftime('%w', t)
        logger.info(h, m, s, w)
        time.sleep(0.3)
        str_time = 12
        str_time_2 = 14
        is_friday = True
        is_saturday = True
        Global.set_is_run(False)

        now = time.localtime()
        while True:
            if (now.tm_hour >= str_time and now.tm_hour < str_time_2) and is_friday:
                logger.info("start run friday", str(now.tm_hour), ":", str(now.tm_min))
                is_friday = False
                self.run("all")
                # return_value = self.friday()
                # print("2************************")
                # print(return_value)
                # if return_value is None:
                #     is_friday = True
                #     time.sleep(2)

            if now.tm_hour >= str_time_2 and is_saturday:
                logger.info("start run saturday", str(now.tm_hour), ":", str(now.tm_min))
                is_saturday = False
                Global.set_comm_week(int(Global.get_comm_week()) + 1)
                self.run()
                # is_done = self.saturday()

                # if is_done:
                #     break

            if Global.get_is_run():
                break

if __name__ == '__main__':
    pass
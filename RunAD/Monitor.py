# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-01-15 
"""

import json
import time
import sys
import Execute
import parameter

class monitor(object):
    """
    Monitor AD Job implementation
    """

    def __init__(self, version):
        self.version = version

    def run_ad(self, job_id):
        """
        Monitor run ad number
        :param job_id:
        :return:
        """
        para = parameter.parameter(0, job_id)
        run_parameter = para.go_on_ad_to_order()

        run_job = Execute.execute(self.version)
        response = run_job.post(run_parameter)
        print("1************************")
        print(response.status_code)

        if response.status_code is not 200:
            return None
        else:
            return_object = json.loads(json.loads(response.text)["string"])

            if int(str(return_object["errorCode"])) == 200:
                implementation = return_object["data"]["totalAdCount"]
                # for country in implementation:
                #     print("monitor", country)
                return implementation
            else:
                return None


    def is_done(self, job_id):
        """
        Monitor AD Job is over
        :param job_id:
        :return:
        """
        para = parameter.parameter(0, job_id)
        friday_run = para.is_finish()

        run_job = Execute.execute(self.version)
        response = run_job.post(friday_run)
        print("1************************")
        print(response.status_code)

        if response.status_code is not 200:
            return None
        else:
            return_object = json.loads(json.loads(response.text)["string"])

            if int(str(return_object["errorCode"])) == 200:
                print("monitor", str(job_id) + ": " + str(return_object["data"]["isDone"]))
                return str(return_object["data"]["isDone"])
            else:
                return None

    def run_monitor(self, job_id):
        monitor_count = 0
        monitor_error_count = 0
        monitor_first_total_count = 0

        while True:
            return_monitor_object = self.run_ad(job_id)
            if return_monitor_object is not None:
                monitor_total_ad_count_dict = list(return_monitor_object)
                for country_item in monitor_total_ad_count_dict:
                    total_processeds = dict(country_item)
                    monitor_count += int(total_processeds["totalProcessedCount"])

                if monitor_count == monitor_first_total_count:
                    monitor_error_count += 1
                else:
                    monitor_error_count = 0
                    monitor_first_total_count = monitor_count
                    monitor_count = 0

                print("Monitor job(", job_id, ") total count : ", monitor_first_total_count)

                time.sleep(10)
                is_done = json.loads(self.is_done(job_id))

                if str(1) == str(is_done):
                    print("Monitor Job : ", job_id, " over.")
                    break
                else:
                    print("Monitor Job : ", job_id, " Continue to monitor. ")
                    continue
            else:
                print("Monitor error, reset monitor.")


if __name__ == '__main__':
    """
    This example realizes testing and explanation.
    """
    run_monitor = monitor("dev")

    job_id_list = [2891]

    t = time.localtime()
    h = t.tm_hour
    m = t.tm_min
    s = t.tm_sec
    w = time.strftime('%w', t)
    print(h, m, s, w)
    time.sleep(0.3)
    end_date = 23
    str_time = m

    while True:
        try:
            now = time.localtime()
            if now.tm_hour == end_date:
                print("End App")
                sys.exit(0)
            else:
                if now.tm_min >= str_time:
                    print("start run:" + str(now.tm_hour) + ":" + str(now.tm_min))
                    for id in job_id_list:
                        run_monitor.run_ad(id)
                        time.sleep(10)
                        run_monitor.is_done(id)
                    str_time = now.tm_min + 2
                    if str_time >= 60:
                        str_time = 0
        except Exception as whileEx:
            print(whileEx)
        finally:
            time.sleep(60)
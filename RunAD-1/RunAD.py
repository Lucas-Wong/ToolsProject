#! /usr/bin/env python
# _*_coding:utf-8_*_

import DataEncoding
import parameter
import FridayRunAD
import Monitor
import json
import requests
import six
import time


class RunAD(object):
    """
    Run ad main function
    """

    job_id = []
    job_total_count = {}

    def __init__(self, week_id, next_week_id, version):
        self.week_id = week_id
        self.next_week_id = next_week_id
        self.version = version

    def main(self):
        try:
            t = time.localtime()
            h = t.tm_hour
            m = t.tm_min
            s = t.tm_sec
            w = time.strftime('%w', t)
            print(h, m, s, w)
            time.sleep(0.3)
            friday_22 = 10
            saturday_00 = 15
            is_friday_operation = True
            is_payment_operation = False
            is_saturday_operation = True
            is_monitor_operation = False

            while True:
                try:
                    now = time.localtime()
                    if is_friday_operation is True:
                        if now.tm_hour == friday_22:
                            is_friday_operation = False
                            print("Start Run AD")
                            friday = FridayRunAD.FridayRunAD(self.week_id, self.version)
                            return_object = json.loads(friday.run_ad())
                            print(return_object)
                            if int(str(return_object["errorCode"])) == 200:
                                self.job_id.append(return_object["data"]["jobExecutationId"])
                                print(self.job_id)
                                for totalCount in return_object["data"]["totalAdCount"]:
                                    self.job_total_count[return_object["data"]["jobExecutationId"]] = totalCount["totalCount"]
                            else:
                                print(str(return_object["errorMessage"]))
                                is_friday_operation = True
                            # friday.paymentAD()
                            print(self.job_total_count)

                    if is_payment_operation is True:
                        pass

                    if is_saturday_operation is True:
                        if now.tm_hour == saturday_00:
                            is_saturday_operation = False

                    if self.job_id.count(object) > 0:
                        is_monitor_operation = True
                        for job_id in self.job_id:
                            monitor = Monitor.Monitor(self.week_id, job_id, self.version, self.job_total_count)
                            processed_count = monitor.friday_run_ad

                            if self.job_total_count == processed_count:
                                # exit(0)
                                is_payment_operation = True


                except Exception as whileEx:
                    print("try error")
                    print(whileEx)
                finally:
                    time.sleep(60)

        except Exception as et:
            print(et)


if __name__ == '__main__':
    run = RunAD(201751, 201752, 'dev')
    run.main()

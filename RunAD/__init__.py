# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-01-15 
"""

# import time
# import json
import Run
# import RunAD
# import Monitor

# class init(object):
#
#     def __init__(self):
#         self.version = "dev"
#         self.week = 201802
#
#     def test(self):
#         t = time.localtime()
#         h = t.tm_hour
#         m = t.tm_min
#         s = t.tm_sec
#         w = time.strftime('%w', t)
#         print(h, m, s, w)
#         time.sleep(0.3)
#         end_date = 23
#         str_time = 13
#         str_time_2 = 15
#
#         monitor_total_count = 0
#         monitor_payment_total_count = 0
#
#         now = time.localtime()
#         if now.tm_hour >= str_time and now.tm_hour < str_time_2:
#             # Run friday AD
#             print("start run:", str(now.tm_hour), ":", str(now.tm_min))
#             run_ad = RunAD.run_ad()
#
#             print("init", self.version, "all", self.week)
#             run_ad_object = json.loads(run_ad.run(self.version, "all", self.week))
#             print("init", run_ad_object)
#             if int(str(run_ad_object["errorCode"])) == 200:
#                 job_id = run_ad_object["data"]["jobExecutationId"]
#                 run_ad_total_count_dict = list(run_ad_object["data"]["totalAdCount"])
#                 for item in run_ad_total_count_dict:
#                     total_count = dict(item)
#                     monitor_total_count += int(total_count["totalCount"])
#
#                 print("init Job(", job_id, ") total count:", monitor_total_count)
#                 monitor = Monitor.monitor(self.version)
#
#                 monitor.run_monitor(job_id)
#             else:
#                 print("init Execute job error: ", str(run_ad_object["errorMessage"]))
#
#             # Run Friday payment
#             data = json.loads(run_ad.payment(self.version, self.week))
#
#             if int(str(data["errorCode"])) == 200:
#                 job_id = data["data"]["jobExecutationId"]
#                 run_payment_total_count_dict = list(data["data"]["totalAdCount"])
#                 for item in run_payment_total_count_dict:
#                     print(item)
#                     total_count = dict(item)
#                     monitor_payment_total_count += int(total_count["totalCount"])
#
#                 print("init Job(", job_id, ") total count:", monitor_payment_total_count)
#
#                 monitor = Monitor.monitor(self.version)
#
#                 monitor.run_monitor(job_id)
#
#
#         if now.tm_hour >= str_time_2:
#             pass


if __name__ == '__main__':
    test = Run.init_run("dev", 201802)
    test.main()
# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-01-16 
"""
import json
import time
import _thread
import RunAD
import Monitor

class init_run(object):

    def __init__(self, version, week):
        self.version = version
        self.week = week

    def friday(self):
        monitor_total_count = 0
        monitor_payment_total_count = 0

        # Run friday AD
        run_ad = RunAD.run_ad()

        print("init", self.version, "all", self.week)
        return_object = run_ad.run(self.version, "all", self.week)
        if return_object is not None:
            run_ad_object = json.loads(return_object)
            print("init", run_ad_object)
            if int(str(run_ad_object["errorCode"])) == 200:
                job_id = run_ad_object["data"]["jobExecutationId"]
                run_ad_total_count_dict = list(run_ad_object["data"]["totalAdCount"])
                for item in run_ad_total_count_dict:
                    total_count = dict(item)
                    monitor_total_count += int(total_count["totalCount"])

                print("init Job(", job_id, ") total count:", monitor_total_count)
                monitor = Monitor.monitor(self.version)

                # _thread.start_new_thread(monitor.run_monitor, (job_id,))
                monitor.run_monitor(job_id)
            else:
                print("init Execute job error: ", str(run_ad_object["errorMessage"]))

            # Run Friday payment
            data = json.loads(run_ad.payment(self.version, self.week))

            if int(str(data["errorCode"])) == 200:
                job_id = data["data"]["jobExecutationId"]
                run_payment_total_count_dict = list(data["data"]["totalAdCount"])
                for item in run_payment_total_count_dict:
                    print(item)
                    total_count = dict(item)
                    monitor_payment_total_count += int(total_count["totalCount"])

                print("init Job(", job_id, ") total count:", monitor_payment_total_count)

                monitor = Monitor.monitor(self.version)

                monitor.run_monitor(job_id)
            return job_id
        else:
            return None

    def saturday(self):
        monitor_total_count = 0
        monitor_count = 0
        job_id_dict = {}
        country_job_dict = {}
        monitor_error_count_dict = {}
        monitor_first_total_count = {}

        run_ad = RunAD.run_ad()
        country_list = ["jpn", "usa", "chn", "other"]

        for country in country_list:
            print("country : ", country)
            return_object = run_ad.run(self.version, country, self.week)
            if return_object is not None:
                run_ad_object = json.loads(return_object)
                if int(str(run_ad_object["errorCode"])) == 200:
                    job_id = run_ad_object["data"]["jobExecutationId"]
                    run_ad_total_count_dict = list(run_ad_object["data"]["totalAdCount"])
                    for item in run_ad_total_count_dict:
                        total_count = dict(item)
                        monitor_total_count += int(total_count["totalCount"])

                    job_id_dict[str(job_id)] = monitor_total_count
                    country_job_dict[str(job_id)] = country
                    print("init Job(", job_id, ") total count:", monitor_total_count)
                    monitor_total_count = 0

        print(job_id_dict, type(job_id_dict))
        monitor = Monitor.monitor(self.version)

        while True:
            if len(job_id_dict) == 0:
                break

            job_id_dict_copy = job_id_dict.copy()
            country_job_dict_copy = country_job_dict.copy()
            for job_id in job_id_dict.keys():
                print("Job(", job_id, ") total count: ", job_id_dict[job_id])
                return_monitor_object = monitor.run_ad(job_id)
                if return_monitor_object is not None:
                    monitor_total_ad_count_dict = list(return_monitor_object)
                    for country_item in monitor_total_ad_count_dict:
                        total_processeds = dict(country_item)
                        monitor_count += int(total_processeds["totalProcessedCount"])

                    if str(job_id) in monitor_first_total_count:
                        if monitor_count == monitor_first_total_count[str(job_id)]:
                            monitor_error_count_dict[str(job_id)] += 1
                        else:
                            monitor_error_count_dict[str(job_id)] = 0
                            monitor_first_total_count[str(job_id)] = monitor_count
                            monitor_count = 0
                    else:
                        monitor_error_count_dict[str(job_id)] = 0
                        monitor_first_total_count[str(job_id)] = monitor_count
                        monitor_count = 0

                    print("Monitor job(", job_id, ") total count : ", monitor_first_total_count[str(job_id)])

                    time.sleep(10)
                    is_done = json.loads(monitor.is_done(job_id))

                    if str(1) == str(is_done):
                        print("Monitor Job : ", job_id, " over.")
                        # del job_id_dict[str(job_id)]
                        job_id_dict_copy.pop(str(job_id))
                    else:
                        print("Monitor Job : ", job_id, " Continue to monitor. ")

                    if int(monitor_error_count_dict[str(job_id)]) > 10:
                        if country_job_dict.has_key[str(job_id)]:
                            run_ad_object = json.loads(run_ad.run(self.version, country_job_dict[str(job_id)], self.week))
                            if int(str(run_ad_object["errorCode"])) == 200:
                                job_id_new = run_ad_object["data"]["jobExecutationId"]
                                run_ad_total_count_dict = list(run_ad_object["data"]["totalAdCount"])
                                for item in run_ad_total_count_dict:
                                    total_count = dict(item)
                                    monitor_total_count += int(total_count["totalCount"])

                                job_id_dict[str(job_id_new)] = monitor_total_count
                                country_job_dict[str(job_id_new)] = country_job_dict[str(job_id)]
                                print("init Job(", job_id_new, ") total count:", monitor_total_count)
                                monitor_total_count = 0

                                # del country_job_dict[str(job_id)]
                                country_job_dict_copy.pop(str(job_id))

            job_id_dict = job_id_dict_copy.copy()
            country_job_dict = country_job_dict_copy.copy()

        return True


    def main(self):
        t = time.localtime()
        h = t.tm_hour
        m = t.tm_min
        s = t.tm_sec
        w = time.strftime('%w', t)
        print(h, m, s, w)
        time.sleep(0.3)
        str_time = 12
        str_time_2 = 14
        is_friday = True
        is_saturday = True

        now = time.localtime()
        while True:
            if (now.tm_hour >= str_time and now.tm_hour < str_time_2) and is_friday:
                print("start run friday", str(now.tm_hour), ":", str(now.tm_min))
                is_friday = False
                return_value = self.friday()
                print("2************************")
                print(return_value)
                if return_value is None:
                    is_friday = True
                    time.sleep(2)

            if now.tm_hour >= str_time_2 and is_saturday:
                print("start run saturday", str(now.tm_hour), ":", str(now.tm_min))
                is_saturday = False
                is_done = self.saturday()

                if is_done:
                    break

if __name__ == '__main__':
    init = init_run("dev", 201802)
    init.main()
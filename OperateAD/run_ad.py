# -*- coding: utf-8 -*-
"""
-----------------------------------------------------
    File Name:        run_ad
    Author:           Lucas.wang
    Date:             2019-02-06 16:19
    Description:      
-----------------------------------------------------
    Change Activity:  2019-02-06 16:19
    Description:      
----------------------------------------------------
"""
import check_job

class run_ad():

    def __init__(self):
        pass

    def run(self, company, version, week, how_many_times):
        check_job = check_job()
        job_id_list = []
        job_total_count_dictionary = {}

        # 1.设置 country list

        # 2. run ad 2cn

        # 3. check ad job
        check_job.check(job_id_list, job_total_count_dictionary)
        # 4. run payment

        # 5. check ad job
        check_job.check(job_id_list, job_total_count_dictionary)
        # 6. run ad 1cn

        # 7.check ad job
        check_job.check(job_id_list, job_total_count_dictionary)
        # pass

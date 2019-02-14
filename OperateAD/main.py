# -*- coding: utf-8 -*-
"""
-----------------------------------------------------
    File Name:        main.py
    Author:           Lucas.wang
    Date:             2019-02-06 16:17
    Description:      
-----------------------------------------------------
    Change Activity:  2019-02-06 16:17
    Description:      
----------------------------------------------------
"""
import run_ad

if __name__ == '__main__':
    run_ad_job = run_ad()
    # run_ad_job.run("ARIIX", "dev", 201801, 2)
    run_ad_job.run("MAVIE", "dev", 201802, 1)
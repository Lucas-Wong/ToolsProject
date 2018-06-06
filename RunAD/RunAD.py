# ! /usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@author = lucas.wang 
@create_time = 2018-01-15 
"""

import json
import parameter
import Execute

class run_ad(object):
    """
    Execute AD Job
    """

    def __init__(self):
        pass

    def run(self, version, is_all, week_id):
        """
        Run AD Job
        :return:
        """

        parameter_function = parameter.parameter(week_id, 0)

        if str("all") == str(is_all):
            run_country = parameter_function.AllCountry()
        elif str("jpn") == str(is_all):
            run_country = parameter_function.JPN()
        elif str("chn") == str(is_all):
            run_country = parameter_function.CHN()
        elif str("usa") == str(is_all):
            run_country = parameter_function.USA()
        else:
            run_country = parameter_function.Other()

        run_job = Execute.execute(version)
        response = run_job.post(run_country)
        print("1************************")
        print(response.status_code)

        if response.status_code is not 200:
            return None
        else:
            return json.loads(response.text)["string"]

    def payment(self, version, week_id):
        """
        Run AD payment
        :return:
        """
        parameter_function = parameter.parameter(week_id, 0)

        run_payment = parameter_function.payment()

        run_job = Execute.execute(version)
        response = run_job.post(run_payment)

        if response.status_code is not 200:
            return None
        else:
            return json.loads(response.text)["string"]

if __name__ == '__main__':
    run_ad_job = run_ad()
    run_ad_job.run("dev", "all", 201801)
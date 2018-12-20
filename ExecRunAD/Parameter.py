# _*_ coding:utf-8 _*_
"""
-----------------------------------------------------------
 Name：            ToolsProject/Parameter
 Purpose：         Parameter class

 Author：          lucas.wang

 Created：         2018-07-30
 Copyright：       (C) lucas.wang 2018
 Licence:          MIT
 ----------------------------------------------------------
"""
# ! /usr/bin/env python

class parameter(object):
    """
    Url parameter
    """

    monitor_run_ad_hand = {"token": "tt", "errorCode": "200", "errorMessage": "", "status": "NORMAL", "source": "client", "userId": 721}

    monitor_run_ad_body = {"userId": 721}

    JPN_list = ["JPN"]
    USA_list = ["USA"]
    CHN_list = ["GBR", "CHN"]
    OTHER_list = ["KAZ", "NLD", "MEX", "FRA", "IRL", "AUS", "ESP", "AUT", "RUS", "SWE", "ITA", "BEL", "DEU", "HRV", "FIN", "CAN", "PRT", "HKG", "TWN", "EST", "POL", "DNK", "SGP", "AUT", "HUN", "KGZ", "PRI", "LUX"]

    def __init__(self, week_id, job_id):
        self.week_id = week_id
        self.job_id = job_id

    def AllCountry(self):
        """
        friday run ad parameter
        :return:
        """
        hand = self.monitor_run_ad_hand
        hand["processKey"] = "runAdToOrderProcess"
        body = self.monitor_run_ad_body
        body["countryList"] = self.JPN_list + self.USA_list + self.CHN_list + self.OTHER_list
        body["commWeek"] = self.week_id

        return_json = {"messageHead": hand,
                "messageBody": body}

        return return_json

    def JPN(self):
        """
        Saturday run ad parameter: country = Japan
        :return:
        """
        hand = self.monitor_run_ad_hand
        hand["processKey"] = "runAdToOrderProcess"
        body = self.monitor_run_ad_body
        body["countryList"] = self.JPN_list
        body["commWeek"] = self.week_id

        return_json = {"messageHead": hand, "messageBody": body}

        return return_json

    def Other(self):
        """
        Saturday run ad parameter: country = other country
        :return:
        """
        hand = self.monitor_run_ad_hand
        hand["processKey"] = "runAdToOrderProcess"
        body = self.monitor_run_ad_body
        body["countryList"] = self.OTHER_list
        body["commWeek"] = self.week_id

        return_json = {"messageHead": hand,
                "messageBody": body}
        return return_json

    def USA(self):
        """
        Saturday run ad parameter: country = USA
        :return:
        """
        hand = self.monitor_run_ad_hand
        hand["processKey"] = "runAdToOrderProcess"
        body = self.monitor_run_ad_body
        body["countryList"] = self.USA_list
        body["commWeek"] = self.week_id

        return_json = {"messageHead": hand,
                "messageBody": body}
        return return_json

    def CHN(self):
        """
        Saturday run ad parameter: country = China, GBR
        :return:
        """
        hand = self.monitor_run_ad_hand
        hand["processKey"] = "runAdToOrderProcess"
        body = self.monitor_run_ad_body
        body["countryList"] = self.CHN_list
        body["commWeek"] = self.week_id

        return_json = {"messageHead": hand,
                "messageBody": body}

        return return_json

    def go_on_ad_to_order(self):
        """
        Get country number
        :return:
        """
        hand = self.monitor_run_ad_hand
        hand["processKey"] = "getJobExecutingStatisticResult"

        return_json = {"messageHead": hand,
                "messageBody": {"jobExecDetailId": self.job_id, "groupby": "country"}}

        return return_json

    def is_finish(self):
        """
        Check job is done
        :return:
        """
        hand = self.monitor_run_ad_hand
        hand["processKey"] = "checkJobIsDoneHanlder"

        return_json = {"messageHead": hand,
                "messageBody": {"jobExecDetailId": self.job_id}}

        return return_json

    def payment(self):
        """
        Run payment
        :return:
        """
        hand = self.monitor_run_ad_hand
        hand["processKey"] = "runPayFailedADOrderProcess"
        body = self.monitor_run_ad_body
        body["commWeek"] = self.week_id
        body["countryList"] = self.JPN_list + self.USA_list + self.CHN_list + self.OTHER_list

        return_json = {"messageHead": hand,
                "messageBody": body}

        return return_json

if __name__ == '__main__':
    run = parameter(201801, 1128)
    # 201739 run
    FridayRun = run.AllCountry()
    print(FridayRun)

    # 201740 run
    usa = run.USA()
    print(usa)

    jpn = run.JPN()
    print(jpn)

    chn_gbr = run.CHN()
    print(chn_gbr)

    other = run.Other()
    print(other)

    go_to = run.go_on_ad_to_order()
    print(go_to)

    finsh = run.is_finish()
    print(finsh)
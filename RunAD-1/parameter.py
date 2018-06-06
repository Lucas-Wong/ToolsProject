#! /usr/bin/env python
# _*_coding:utf-8_*_

class parameter(object):
    """
    Url parameter
    """

    hand = {"token": "tt", "errorCode": "200", "errorMessage": "", "status": "NORMAL",
                                "source": "client", "userId": 721,
                                "processKey": "runAdToOrderProcess"}

    monitor_hand = {"token": "tt", "errorCode": "200", "errorMessage": "", "status": "NORMAL",
                                "source": "client", "userId": 721,
                                "processKey": "getJobExecutingStatisticResult"}

    monitor_done_hand = {"token": "tt", "errorCode": "200", "errorMessage": "", "status": "NORMAL",
                                "source": "client", "userId": 721,
                                "processKey": "checkJobIsDoneHanlder"}

    monitor_error_hand = {"token": "tt", "errorCode": "200", "errorMessage": "", "status": "NORMAL",
                                "source": "client", "userId": 721,
                                "processKey": "getErrorJobProcessedRecordResultListHandler"}

    def __init__(self, week_id, job_id):
        self.week_id = week_id
        self.job_id = job_id

    def AllCountry(self):
        """
        friday run ad parameter
        :return:
        """
        body = {"messageHead": self.hand,
                "messageBody": {"commWeek": self.week_id, "userId": 29,
                                "countryList": ["KAZ", "NLD", "MEX",
                                                "FRA", "IRL", "AUS",
                                                "ESP", "AUT", "RUS",
                                                "SWE", "ITA", "BEL",
                                                "DEU", "HRV", "FIN",
                                                "CAN", "PRT", "HKG",
                                                "TWN", "EST", "POL",
                                                "DNK", "SGP", "AUT",
                                                "HUN", "KGZ", "PRI",
                                                "LUX", "JPN", "USA",
                                                "GBR", "CHN"]}}
        return body

    def JPN(self):
        """
        Saturday run ad parameter: country = Japan
        :return:
        """
        body = {"messageHead": self.hand,
                "messageBody": {"commWeek": self.week_id, "userId": 29,
                                "countryList": ["JPN"]}}
        return body

    def Other(self):
        """
        Saturday run ad parameter: country = other country
        :return:
        """
        body = {"messageHead": self.hand,
                "messageBody": {"commWeek": self.week_id, "userId": 29,
                                "countryList": ["KAZ", "NLD", "MEX",
                                                "FRA", "IRL", "AUS",
                                                "ESP", "AUT", "RUS",
                                                "SWE", "ITA", "BEL",
                                                "DEU", "HRV", "FIN",
                                                "CAN", "PRT", "HKG",
                                                "TWN", "EST", "POL",
                                                "DNK", "SGP", "AUT",
                                                "HUN", "KGZ", "PRI",
                                                "LUX"]}}
        return body

    def USA(self):
        """
        Saturday run ad parameter: country = USA
        :return:
        """
        body = {"messageHead": self.hand,
                "messageBody": {"commWeek": self.week_id, "userId": 29,
                                "countryList": ["USA"]}}
        return body

    def CHN(self):
        """
        Saturday run ad parameter: country = China, GBR
        :return:
        """
        body = {"messageHead": self.hand,
                "messageBody": {"commWeek": self.week_id, "userId": 29,
                                "countryList": ["GBR", "CHN"]}}
        return body

    def go_on_ad_to_order(self):
        """
        Get country number
        :return:
        """
        monitor_body = {"messageHead": self.monitor_hand,
                "messageBody": {"jobExecDetailId": self.job_id, "groupby": "country"}}
        return monitor_body

    def is_finish(self):
        """
        Check job is done
        :return:
        """
        monitor_body = {"messageHead": self.monitor_done_hand,
                "messageBody": {"jobExecDetailId": self.job_id}}
        return monitor_body

    def is_error(self):
        """
        Check job is done
        :return:
        """
        monitor_body = {"messageHead": self.monitor_error_hand,
                "messageBody": {"jobExecDetailId": self.job_id}}
        return monitor_body

if __name__ == '__main__':
    run = parameter(201739, 0)
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

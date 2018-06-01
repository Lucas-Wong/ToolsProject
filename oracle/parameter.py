#! /usr/bin/env python
# _*_coding:utf-8_*_

class parameter():

    hand = {"token": "tt", "errorCode": "200", "errorMessage": "", "status": "NORMAL",
                                "source": "client",
                                "processKey": "runAdToOrderProcess"}


    def __init__(self, weekId):
        self.week_id = weekId

    def AllCountry(self):
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
        body = {"messageHead": self.hand,
                "messageBody": {"commWeek": self.week_id, "userId": 29,
                                "countryList": ["JPN"]}}
        return body

    def Other(self):
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
        body = {"messageHead": self.hand,
                "messageBody": {"commWeek": self.week_id, "userId": 29,
                                "countryList": ["USA"]}}
        return body

    def CHN(self):
        body = {"messageHead": self.hand,
                "messageBody": {"commWeek": self.week_id, "userId": 29,
                                "countryList": ["GBR", "CHN"]}}
        return body

if __name__ == '__main__':
    run = parameter(201739, 201740)
    # 201739 run
    FridayRun = run.AllCountry()

    # 201740 run
    usa = run.USA()
    jpn = run.JPN()
    chn_gbr = run.CHN()
    other = run.Other()

#!/usr/bin/env python
"""
 Created by howie.hu at 2019/4/19.
"""


class HourlyClassification:
    FRIDAY = 5
    WORK_HOUR_OF_DAY = 8.0
    MORE_PAY_RATE = 1.5

    def __init__(self, hour_salary):
        self.hour_salary = hour_salary
        self.time_cards = []

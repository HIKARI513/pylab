#!/usr/bin/env python
"""
 Created by howie.hu at 2019/4/19.
"""
import datetime
import typing

from src.paycheck import Paycheck
from src.payment_classification import PaymentClassification
from src.time_card import TimeCard


class HourlyClassification(PaymentClassification):
    FRIDAY = 5
    WORK_HOUR_OF_DAY = 8.0
    MORE_PAY_RATE = 1.5

    def __init__(self, hour_salary):
        self.hour_salary = hour_salary
        self.time_cards = []

    def add_time_card(self, time_card: TimeCard):
        self.time_cards.append(time_card)

    def get_time_card(self, date: datetime.date) -> typing.Union[TimeCard, None]:
        for time_card in self.time_cards:
            if time_card.get_date() == date:
                return time_card
        return None

    def calculate_pay(self, paycheck: Paycheck):
        pay = 0.0
        for time_card in self.time_cards:
            pass

    def is_in_pay_periods(self, time_card: TimeCard, pay_day: datetime.date):
        start_day = pay_day + datetime.timedelta(days=-5)

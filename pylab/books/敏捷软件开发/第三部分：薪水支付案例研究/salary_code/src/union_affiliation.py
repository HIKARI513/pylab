#!/usr/bin/env python
"""
 Created by howie.hu at 2019/4/22.
"""
import datetime
import typing

from src.affiliation import Affiliation
from src.service_charge import ServiceCharge


class UnionAffiliation(Affiliation):
    CHARGE_DAY_OF_WEEK: int = 5

    def __init__(self, member_id: int, weekly_charge: float):
        self.member_id = member_id
        self.weekly_charge = weekly_charge
        self.service_charges = []

    def add_service_charge(self, service_charge: ServiceCharge):
        self.service_charges.append(service_charge)

    def get_service_charge(self, date: datetime.date) -> typing.Union[ServiceCharge, None]:
        for service_charge in self.service_charges:
            if service_charge.get_date() == date:
                return service_charge
        return None

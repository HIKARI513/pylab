#!/usr/bin/env python
"""
 Created by howie.hu at 2019/4/19.
"""

from src.add_employee_transaction import AddEmployeeTransaction
from src.hourly_classification import HourlyClassification
from src.weekly_schedule import WeeklySchedule


class AddHourlyEmployee(AddEmployeeTransaction):
    def add_hourly_employee(self, emp_id, name, address, hour_salary):
        super().add_employee_transaction(emp_id, name, address)
        self.hour_salary = hour_salary

    def make_classification(self):
        return HourlyClassification(self.hour_salary)

    def make_schedule(self):
        return WeeklySchedule(HourlyClassification.FRIDAY)

#!/usr/bin/env python
"""
 Created by howie.hu at 2019/4/19.
"""
from src.add_employee_transaction import AddEmployeeTransaction
from src.commissioned_classification import CommissionedClassification
from src.bl_weekly_schedule import BlweeklySchedule


class AddCommissionedEmployee(AddEmployeeTransaction):
    def add_commissioned_employee(self, emp_id, name, address, salary, commissioned_rate):
        super().add_employee_transaction(emp_id, name, address)
        self.salary = salary
        self.commissioned_rate = commissioned_rate

    def make_classification(self):
        return CommissionedClassification(self.salary, self.commissioned_rate)

    def make_schedule(self):
        return BlweeklySchedule(5)

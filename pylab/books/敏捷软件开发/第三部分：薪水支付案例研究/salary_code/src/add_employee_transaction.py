#!/usr/bin/env python
"""
 Created by howie.hu at 2019/4/19.
"""

from src.employee import Employee
from src.hold_method import HoldMethod
from src.payroll_database import PayrollDatabase
from src.transaction import Transaction


class AddEmployeeTransaction(Transaction):
    def __init__(self, emp_id: int, name: str, address: str):
        self._emp_id, self._name, self._address = emp_id, name, address
        self.classification, self.schedule, self.method = None, None, None

    def make_classification(self):
        pass

    def make_schedule(self):
        pass

    def execute(self):
        e = Employee(self._emp_id, self._name, self._address)
        e.classification = self.make_classification()
        e.schedule = self.make_schedule()
        e.method = HoldMethod()
        PayrollDatabase.add_employee(self._emp_id, e)


if __name__ == "__main__":
    t = AddEmployeeTransaction(1, '2', '3')

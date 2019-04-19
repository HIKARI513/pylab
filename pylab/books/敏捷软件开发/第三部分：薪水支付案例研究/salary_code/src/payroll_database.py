#!/usr/bin/env python
"""
 Created by howie.hu at 2019/4/19.
"""


class PayrollDatabase:
    employees = {}

    @classmethod
    def add_employee(cls, emp_id, employee):
        cls.employees[emp_id] = employee

    @classmethod
    def get_employee(cls, emp_id):
        return cls.employees[emp_id]

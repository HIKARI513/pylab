#!/usr/bin/env python
"""
 Created by howie.hu at 2019/4/19.
"""


class PayrollDatabase:
    employees = {}

    @classmethod
    def add_employee(cls, emp_id: int, employee: str):
        cls.employees[emp_id] = employee

    @classmethod
    def delete_employee(cls, emp_id: int):
        cls.employees.pop(emp_id)

    @classmethod
    def get_employee(cls, emp_id: int):
        try:
            return cls.employees[emp_id]
        except:
            return None

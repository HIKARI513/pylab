import pytest

from src.payroll_database import PayrollDatabase


def test_add_salaried_employee():
    emp_id = 1
    t = AddSalariedEmployee(emp_id, "Bob", "Home", 1000.00)
    e = PayrollDatabase.get_employee(emp_id)

    assert e.name == "Bob"

    pc = e.Classification
    assert pc is SalariedClassification

    ps = e.Schedule
    assert ps is MonthlySchedule

    pm = e.Method
    assert pm is HoldMethod

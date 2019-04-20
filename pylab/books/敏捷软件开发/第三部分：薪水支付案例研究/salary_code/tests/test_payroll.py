import datetime

from src.add_salaried_employee import AddSalariedEmployee
from src.add_commissioned_employee import AddCommissionedEmployee
from src.add_hourly_empoylee import AddHourlyEmployee
from src.delete_employee_transaction import DeleteEmployeeTransaction
from src.hold_method import HoldMethod
from src.hourly_classification import HourlyClassification
from src.monthly_schedule import MonthlySchedule
from src.payroll_database import PayrollDatabase
from src.salaried_classification import SalariedClassification
from src.time_card_transaction import TimeCardTransaction


def test_add_salaried_employee():
    emp_id = 1
    t = AddSalariedEmployee(emp_id, "Bob", "Home", 1000.00)
    t.execute()
    e = PayrollDatabase.get_employee(emp_id)
    assert e.name == "Bob"

    pc = e.classification
    assert isinstance(pc, SalariedClassification) == True

    ps = e.schedule
    assert isinstance(ps, MonthlySchedule) == True

    pm = e.method
    assert isinstance(pm, HoldMethod) == True


def test_delete_employee_transaction():
    emp_id = 4
    t = AddCommissionedEmployee(emp_id, "Bill", "Home", 2500, 3.2)
    t.execute()

    e = PayrollDatabase.get_employee(emp_id)
    assert e.name == "Bill"

    dt = DeleteEmployeeTransaction(emp_id=emp_id)
    dt.execute()

    e = PayrollDatabase.get_employee(emp_id)
    assert e == None


def test_time_card_transaction():
    emp_id = 5

    t = AddHourlyEmployee(emp_id, "Bill", "Home", 15.25)
    t.execute()

    tct = TimeCardTransaction(date=datetime.date(2005, 7, 31), hours=8.0, emp_id=emp_id)
    tct.execute()

    e = PayrollDatabase.get_employee(emp_id)
    assert e.name == "Bill"

    hc = pc = e.classification
    assert isinstance(pc, HourlyClassification)

    tc = hc.get_time_card(datetime.date(2005, 7, 31))
    assert tc.get_hours() == 8.0

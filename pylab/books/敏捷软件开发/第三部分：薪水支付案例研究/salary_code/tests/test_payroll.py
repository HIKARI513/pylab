import datetime

from src.add_salaried_employee import AddSalariedEmployee
from src.add_commissioned_employee import AddCommissionedEmployee
from src.add_hourly_empoylee import AddHourlyEmployee
from src.change_member_transaction import ChangeMemberTransaction
from src.change_name_transaction import ChangeNameTransaction
from src.change_hourly_transaction import ChangeHourlyTransaction
from src.delete_employee_transaction import DeleteEmployeeTransaction
from src.hold_method import HoldMethod
from src.hourly_classification import HourlyClassification
from src.monthly_schedule import MonthlySchedule
from src.paycheck import Paycheck
from src.payday_transaction import PaydayTransaction
from src.payroll_database import PayrollDatabase
from src.salaried_classification import SalariedClassification
from src.serveice_charge_transaction import ServiceChargeTransaction
from src.time_card_transaction import TimeCardTransaction
from src.union_affiliation import UnionAffiliation
from src.weekly_schedule import WeeklySchedule


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


def test_add_service_charge():
    emp_id = 2
    member_id = 86

    t = AddHourlyEmployee(emp_id, "Bill", "Home", 15.25)
    t.execute()
    e = PayrollDatabase.get_employee(emp_id)

    assert e.name == "Bill"

    af = UnionAffiliation(member_id, 12.5)
    e.affiliation = af

    PayrollDatabase.add_union_member(member_id, e)

    sct = ServiceChargeTransaction(member_id, datetime.date(2005, 8, 8), 12.95)
    sct.execute()

    sc = af.get_service_charge(datetime.date(2005, 8, 8))
    assert sc != None
    assert sc.get_amount() == 12.95


def test_change_name_transaction():
    emp_id = 2

    t = AddHourlyEmployee(emp_id, "Bill", "Home", 15.25)
    t.execute()

    cnt = ChangeNameTransaction(emp_id, "Bob")
    cnt.execute()

    e = PayrollDatabase.get_employee(emp_id)

    assert e.name == "Bob"


def test_change_hourly_transaction():
    emp_id = 3
    t = AddCommissionedEmployee(emp_id, "Lance", "Home", 2500, 3.2)
    t.execute()

    cht = ChangeHourlyTransaction(emp_id, 27.52)
    cht.execute()

    e: AddCommissionedEmployee = None
    e = PayrollDatabase.get_employee(emp_id)
    assert e.name == "Lance"

    hc = pc = e.classification
    assert isinstance(pc, HourlyClassification)
    assert hc.hour_salary == 27.52

    ps = e.schedule
    assert isinstance(ps, WeeklySchedule)


def test_change_union_member():
    emp_id = 8
    member_id = 7743

    t = AddHourlyEmployee(emp_id, "Bill", "Home", 15.25)
    t.execute()

    cmt = ChangeMemberTransaction(emp_id, member_id, 99.42)
    cmt.execute()

    e = PayrollDatabase.get_employee(emp_id)
    assert e.name == "Bill"

    affiliation = e.affiliation
    assert affiliation is not None
    assert isinstance(affiliation, UnionAffiliation)
    assert affiliation.weekly_charge == 99.42

    member = PayrollDatabase.get_union_member(member_id)
    assert e == member


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


def test_pay_single_salaried_employee():
    emp_id = 1
    t = AddSalariedEmployee(emp_id, "Bob", "Home", 1000.00)
    t.execute()

    pay_date = datetime.date(2001, 11, 30)
    pt = PaydayTransaction(pay_date)
    pt.execute()

    pc: Paycheck = pt.get_paycheck(emp_id)

    assert pc.pay_date == pay_date
    assert pc.gross_pay == 1000.00
    assert pc.disposition == "Hold"
    assert pc.deductions == 0.0


def test_time_card_transaction():
    emp_id = 5

    t = AddHourlyEmployee(emp_id, "Bill", "Home", 15.25)
    t.execute()

    tct = TimeCardTransaction(date=datetime.date(2005, 7, 31), hours=8.0, emp_id=emp_id)
    tct.execute()

    e = PayrollDatabase.get_employee(emp_id)
    assert e.name == "Bill"

    pc: HourlyClassification = e.classification
    assert isinstance(pc, HourlyClassification)

    tc = pc.get_time_card(datetime.date(2005, 7, 31))
    assert tc.get_hours() == 8.0

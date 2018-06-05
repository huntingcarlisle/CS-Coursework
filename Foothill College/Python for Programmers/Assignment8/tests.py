'''
This program tests the classes Employee, Manager, and EmployeeList

Author: Hunter S. Carlisle
'''

from employee import Employee
from manager import Manager
from EmployeeList import EmployeeList

## Create Valid Employee
print ("==== TESTING EMPLOYEE CLASS ====")

try:
    hsc = Employee("Hunter", "Carlisle", "123-45-6789", 300000.0)
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

print(hsc)

## Give Valid Raise
hsc.giveRaise(.40)

print(hsc)

## Give Invalid Raise
try:
    hsc.giveRaise(-.20)
except ValueError as errorObject:
    print(errorObject)

print(hsc)

## Attempt to create invalid employees
try:
    djt = Employee("Donald", "Drumpf", 111111111, 30.0)
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

try:
    bho = Employee("Barack", 0.8, "111-11-1111", 400000.0)
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

try:
    gwb = Employee(43, "Bush", "111-11-1111", 400000.0)
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

try:
    wjc = Employee("Bill", "Clinton", "111-11-1111", "I did not have...")
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

try:
    hrc = Employee("Hillary", "Clinton", "987-65-4321", 123456.0)
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)


# print(djt)
# print(bho)
# print(gwb)
# print(wjc)
print()

## CREATE MANAGER EMPLOYEE
print ("==== TESTING MANAGER SUBCLASS ====")

try:
    mrManager = Manager("Mr", "Manager", "111-11-1111", 10000.0, "Boss Man", 1000.0)
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

print (mrManager)

try:
    mrIncompetent = Manager("Mr", "Manager", "111-11-1111", 10000.0, 0, 1000.0)
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

# print (mrIncompetent)

try:
    mrIntern = Manager("Mr", "Manager", "111-11-1111", 10000.0, "Intern", "free lunch")
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

# print (mrIntern)

print()

print ("==== TESTING EMPLOYEE LIST ====")

firmEmployees = EmployeeList()

## Add employees
firmEmployees.addEmployee(hsc)         # employee
firmEmployees.addEmployee(mrManager)   # manager
firmEmployees.addEmployee(hrc)

## Give employees a raise

print(firmEmployees)
print()

for employee in firmEmployees.getList():
    employee.giveRaise(.25)

print(firmEmployees)

print ("==== TESTING EMPLOYEE EQ METHOD ====")
print (hsc == hrc)    # FALSE
print (mrManager == hsc)    # FALSE
e1 = Employee("hunter", "carlisle", "999-99-9999", 500.0)
e2 = Employee("HUNTER", "CARLISLE", "123-32-1232", 100.0)
print (hsc == e1)   # TRUE
print (hsc == e2)   # TRUE
print()

print ("==== TESTING EMPLOYEE LT METHOD ====")
print (hsc < hrc)    # TRUE
print (mrManager < hsc)    # FALSE
e3 = Employee("Hero", "Carlisle", "999-99-9999", 500.0)
e4 = Employee("HERO", "CARLISLE", "123-32-1232", 100.0)
print (hsc < e3)   # FALSE
print (e4 < hsc)   # TRUE
print()

print ("==== TESTING EMPLOYEE EQ AND LT METHOD ARE CONSISTENT ====")
print (hsc < e1)   # FALSE
print (hsc > e1)   # FALSE
print (hsc == e1)   # TRUE
print()

print ("==== TESTING EMPLOYEE LIST SORT ====")
sortingList = EmployeeList()
sortingList.addEmployee(hrc)
sortingList.addEmployee(mrManager)
sortingList.addEmployee(hsc)
sortingList.addEmployee(e3)

print(sortingList)
print()
print(sortingList.sort())
print()

print ("==== IMPLEMENTING SORT IN A MORE 'MAGIC' WAY (I.E. WITHOUT USING THE EMPLOYEELIST OBJECT BUT RATHER A NORMAL PYTHON LIST) ====")
employeeList = [hrc, mrManager, hsc, e3]
print (employeeList)
print()
print (sorted(employeeList))




#    ======= OUTPUT =======
# ~/workspace/CS-Coursework/Foothill College/Python for Programmers/Assignment8/ (master) $ python tests.py
# ==== TESTING EMPLOYEE CLASS ====
# Hunter Carlisle is an employee of the firm whose social security number is 123-45-6789 and salary is 300000
# Hunter Carlisle is an employee of the firm whose social security number is 123-45-6789 and salary is 420000
# Invalid raise percentage
# Hunter Carlisle is an employee of the firm whose social security number is 123-45-6789 and salary is 420000
# Invalid employee details
# Invalid employee details
# Invalid employee details
# Invalid employee details

# ==== TESTING MANAGER SUBCLASS ====
# Mr Manager is an employee of the firm whose social security number is 111-11-1111 and salary is 10000, this employee is also a manager of the firm whose job title is Boss Man with an annual bonus of 1000
# Invalid employee details
# Invalid employee details

# ==== TESTING EMPLOYEE LIST ====
# Hunter Carlisle is an employee of the firm whose social security number is 123-45-6789 and salary is 420000
# Mr Manager is an employee of the firm whose social security number is 111-11-1111 and salary is 10000, this employee is also a manager of the firm whose job title is Boss Man with an annual bonus of 1000
# Hillary Clinton is an employee of the firm whose social security number is 987-65-4321 and salary is 123456


# Hunter Carlisle is an employee of the firm whose social security number is 123-45-6789 and salary is 525000
# Mr Manager is an employee of the firm whose social security number is 111-11-1111 and salary is 12500, this employee is also a manager of the firm whose job title is Boss Man with an annual bonus of 1000
# Hillary Clinton is an employee of the firm whose social security number is 987-65-4321 and salary is 154320

# ==== TESTING EMPLOYEE EQ METHOD ====
# False
# False
# True
# True

# ==== TESTING EMPLOYEE LT METHOD ====
# True
# False
# False
# True

# ==== TESTING EMPLOYEE EQ AND LT METHOD ARE CONSISTENT ====
# False
# False
# True

# ==== TESTING EMPLOYEE LIST SORT ====
# Hillary Clinton is an employee of the firm whose social security number is 987-65-4321 and salary is 154320
# Mr Manager is an employee of the firm whose social security number is 111-11-1111 and salary is 12500, this employee is also a manager of the firm whose job title is Boss Man with an annual bonus of 1000
# Hunter Carlisle is an employee of the firm whose social security number is 123-45-6789 and salary is 525000
# Hero Carlisle is an employee of the firm whose social security number is 999-99-9999 and salary is 500


# Hero Carlisle is an employee of the firm whose social security number is 999-99-9999 and salary is 500
# Hunter Carlisle is an employee of the firm whose social security number is 123-45-6789 and salary is 525000
# Hillary Clinton is an employee of the firm whose social security number is 987-65-4321 and salary is 154320
# Mr Manager is an employee of the firm whose social security number is 111-11-1111 and salary is 12500, this employee is also a manager of the firm whose job title is Boss Man with an annual bonus of 1000


# ==== IMPLEMENTING SORT IN A MORE 'MAGIC' WAY (I.E. WITHOUT USING THE EMPLOYEELIST OBJECT BUT RATHER A NORMAL PYTHON LIST) ====
# [Hillary Clinton is an employee of the firm whose social security number is 987-65-4321 and salary is 154320, Mr Manager is an employee of the firm whose social security number is 111-11-1111 and salary is 12500, this employee is also a manager of the firm whose job title is Boss Man with an annual bonus of 1000, Hunter Carlisle is an employee of the firm whose social security number is 123-45-6789 and salary is 525000, Hero Carlisle is an employee of the firm whose social security number is 999-99-9999 and salary is 500]

# [Hero Carlisle is an employee of the firm whose social security number is 999-99-9999 and salary is 500, Hunter Carlisle is an employee of the firm whose social security number is 123-45-6789 and salary is 525000, Hillary Clinton is an employee of the firm whose social security number is 987-65-4321 and salary is 154320, Mr Manager is an employee of the firm whose social security number is 111-11-1111 and salary is 12500, this employee is also a manager of the firm whose job title is Boss Man with an annual bonus of 1000]
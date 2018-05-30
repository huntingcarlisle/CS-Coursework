from employee import Employee
from manager import Manager

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

print(hsc)git add .

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

## PART III ASSIGNMENT - EMPLOYEE LIST
print ("==== TESTING EMPLOYEE LIST ====")

class EmployeeList:
    '''
    One object of this class represents a list of employees, including managers
    '''
    def __init__(self):
        self.employeeList = []

    def addEmployee(self, employee):
        '''
        Used to add an employee to  self.employeeList


        '''
        self.employeeList.append(employee)

    def getList(self):
        '''
        Used to safely access a copy of self.employeeList outside of the class

        Returns: a COPY of self.employeeList
        '''
        return self.employeeList[:]

firmEmployees = EmployeeList()

## Add employees
firmEmployees.addEmployee(hsc)         # employee
firmEmployees.addEmployee(mrManager)   # manager

## Give employees a raise
print(hsc)
print(mrManager)
print()

for employee in firmEmployees.getList():
    employee.giveRaise(.25)

print()
print(hsc)
print(mrManager)
print()



#    ======= OUTPUT =======
# ~/workspace/CS-Coursework/Foothill College/Python for Programmers/Assignment7/ (master) $ python tests.py
# Hunter Carlisle is an employee of the firm whose social security number is 123-45-6789 and salary is 300000
# Hunter Carlisle is an employee of the firm whose social security number is 123-45-6789 and salary is 420000
# Invalid raise percentage
# Hunter Carlisle is an employee of the firm whose social security number is 123-45-6789 and salary is 420000
# Invalid employee details
# Invalid employee details
# Invalid employee details
# Invalid employee details
# Mr Manager is an manager of the firm whose job title is Boss Man and salary is 10000 with an annual bonus of 1000
# Invalid employee details

# Hunter Carlisle is an employee of the firm whose social security number is 123-45-6789 and salary is 420000
# Mr Manager is an manager of the firm whose job title is Boss Man and salary is 10000 with an annual bonus of 1000


# Hunter Carlisle is an employee of the firm whose social security number is 123-45-6789 and salary is 525000
# Mr Manager is an manager of the firm whose job title is Boss Man and salary is 12500 with an annual bonus of 1000

# ~/workspace/CS-Coursework/Foothill College/Python for Programmers/Assignment7/ (master) $ python tests.py
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
# Mr Manager is an manager of the firm whose job title is Boss Man and salary is 10000 with an annual bonus of 1000
# Invalid employee details
# Invalid employee details

# ==== TESTING EMPLOYEE LIST ====
# Hunter Carlisle is an employee of the firm whose social security number is 123-45-6789 and salary is 420000
# Mr Manager is an manager of the firm whose job title is Boss Man and salary is 10000 with an annual bonus of 1000


# Hunter Carlisle is an employee of the firm whose social security number is 123-45-6789 and salary is 525000
# Mr Manager is an manager of the firm whose job title is Boss Man and salary is 12500 with an annual bonus of 1000
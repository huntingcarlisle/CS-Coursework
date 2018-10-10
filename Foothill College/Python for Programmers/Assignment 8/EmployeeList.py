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

    def __str__(self):
        '''
        Returns the EmployeeList object as a paragraph with each employee on one line.
        '''
        s = ""
        for employee in range(len(self.employeeList)):
            s = s + str(self.employeeList[employee]) + "\n"
        return s

    def sort(self):
        '''
        Used to sort an object of the EmployeeList class
        Returns: a sorted copy of self.employeeList
        '''
        sortedEmployeeList = EmployeeList()
        for emp in sorted(self.employeeList):
            sortedEmployeeList.addEmployee(emp)
        return sortedEmployeeList

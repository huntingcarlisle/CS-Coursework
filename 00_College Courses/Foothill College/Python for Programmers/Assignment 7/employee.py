class Employee:
   """
   One object of class Employee represents one employee
   """
   def __init__(self, firstName, lastName, socialSecurityNumber, baseSalary):
      '''
      Initializes an Employee object

      firstName and lastName (string): the name of the employee
      socialSecurityNumber (string): ssn, including dashes:
      baseSalary (float): current annual salary

      an Employee object has two attributes:
         self.firstName
         self.lastName
         self.ssn
         self.salary
      '''
      if type(firstName) == str and type(lastName) == str and type(socialSecurityNumber) == str and type(baseSalary) == float:
         self.firstName = firstName
         self.lastName = lastName
         self.ssn = socialSecurityNumber
         self.salary = baseSalary
      else:
         raise TypeError("Invalid employee details")

   def __str__(self):
      return "%s %s is an employee of the firm whose social security number is %s and salary is %d" % (self.firstName, self.lastName, self.ssn, self.salary)


   def giveRaise(self, percentRaise):
      '''
      Increases employee salary by input percentage (float)
      '''
      if (percentRaise > 0):
         self.salary = self.salary * (1 + percentRaise)
      else:
         raise ValueError("Invalid raise percentage")



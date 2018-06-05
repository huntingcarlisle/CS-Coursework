from employee import Employee

class Manager(Employee):
   """
   One object of class manager represents one employee with
   additional roles and responsibility consistent with their status as boss-type-person
   """
   def __init__(self, firstName, lastName, socialSecurityNumber, baseSalary, jobTitle, annualBonus):
      '''
      Initializes an Manager object

      jobTitle (string): the title of the manager
      annualBonus (float): dollar amount of annual bonus

      a Manager object has two attributes:
         self.title
         self.bonus
      '''
      Employee.__init__(self, firstName, lastName, socialSecurityNumber, baseSalary)
      if type(jobTitle) == str and type(annualBonus) == float:
         self.title = jobTitle
         self.bonus = annualBonus
      else:
         raise TypeError("Invalid employee details")

   def __str__(self):
      '''
      Returns the Manager object as a sentence.
      '''
      return super().__str__() + ", this employee is also a manager of the firm whose job title is %s with an annual bonus of %d" % (self.title,  self.bonus)




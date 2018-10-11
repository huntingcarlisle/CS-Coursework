""" One object of class Account represents one bank account """
class Account:
   def __init__(self):
      print ("Account constructor")
      self.balance = 0
      self.customer = "Mickey Mouse"

   def deposit(self, amount):
      self.balance = self.balance + amount

   def __str__(self):
      return "%s has a balance of %d" % (self.customer, self.balance)

   def __int__(self):
       '''
       Return the balance in the account object
       '''
       return int(self.balance)
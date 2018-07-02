""" One object of class SavingsAccount represents one
    savings account with a customer, a balance, and an interest rate
"""

from account import Account

class SavingsAccount (Account):
# syntax above shows that SavingsAccount is a subclass of the superclass Account

   def __init__(self):
        Account.__init__(self)  # calls the Account constructor to initialize that part of the object
        print ("SavingsAccount constructor")
        self.interestRate = 0.05

   def __str__(self):
        return Account.__str__(self) + ", and the interest rate is " + str(self.interestRate)

""" This is the test program to see how these two types of objects are constructed """

if __name__ == "__main__":
    savingsAccount = SavingsAccount()
    print(int(savingsAccount))  # expect 0
    savingsAccount.deposit(10)
    print(int(savingsAccount)) # expect 10


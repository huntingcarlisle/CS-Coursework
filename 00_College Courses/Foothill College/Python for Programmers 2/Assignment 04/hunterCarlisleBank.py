"""
Hunter Carlisle | Foothill College Fall 2018 | Lab Three

Definition for the BankAccount Class
"""

from decimal import Decimal
from datetime import datetime


class BankAccount:
    """
    One object of class BankAccount represents a simple bank account
    with a balance that can be adjusted with deposits/withdrawls
    """

    def __init__(self, initial_balance=Decimal("0.0")):
        """
        Initializes a BankAccount object with initial balance.
        initial_balance (Decimal): starting balance in BankAccount
        last_interest_adjustment (integer): date of last interest adjustment
        """
        if type(initial_balance) == int or type(initial_balance) == float:
            self.balance = Decimal(initial_balance)
        else:
            raise TypeError("Initial balance must be a number.")
        self.last_interest_adjustment = int(str(datetime.now().year)
                                            + str(datetime.now().month)) - 1

    def deposit(self, amount):
        """
        Deposits input amount to account.
        """
        if amount > 0 and (type(amount) == int or type(amount) == float):
            self.balance += Decimal(amount)
        else:
            raise ValueError("Deposit amount must be positive number.")

    def withdraw(self, amount):
        """
        Withdraws input amount from account.
        """
        if amount > 0 and (type(amount) == int or type(amount) == float):
            if amount < self.balance:
                self.balance -= Decimal(amount)
            else:
                self.balance -= Decimal(10)
        else:
            raise ValueError("Withdrawal amount must be positive number.")

    def add_interest(self, rate):
        """
        Adds input interest to account, if eligible.
        An account is eligible if interest has not been adjusted this month.
        """
        if int(str(datetime.now().year) + str(datetime.now().month)) \
                > self.last_interest_adjustment:
            if 1 <= rate <= 2 and (type(rate) == int or type(rate) == float):
                self.balance += self.balance * Decimal(rate) / Decimal(100)
                self.last_interest_adjustment = int(str(datetime.now().year)
                                                    + str(datetime.now().month))
            else:
                raise ValueError("Rate must be a number between 1 and 2.")
        else:
            print("Declined, you need to wait until next month.")

    def get_balance(self):
        """
        Returns current account balance.
        """
        if self.balance >= 0:
            return "$" + '{0:,.2f}'.format(self.balance)
        else:
            return "-$" + '{0:,.2f}'.format(abs(self.balance))

    def withdraw_all(self):
        """
        Withdraws all funds from account.
        """
        self.balance = Decimal(0)
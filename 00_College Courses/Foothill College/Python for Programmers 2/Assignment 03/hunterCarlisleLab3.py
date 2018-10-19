
"""
Hunter Carlisle | Foothill College Fall 2018 | Lab Three

This is the test driver file for the BankAccount Class

"""

from hunterCarlisleBank import BankAccount


def main():
    print("Action: Open New Account - Initial Deposit $500.00")
    new_account = BankAccount(500.00)
    print("Balance: " + new_account.get_balance())
    print("Action: Deposit $500.00")
    new_account.deposit(500.00)
    print("Balance: " + new_account.get_balance())
    print("Action: Withdraw $2000.00 (and get penalty)")
    new_account.withdraw(2000.00)
    print("Balance: " + new_account.get_balance())
    print("Action: Add interest 1%")
    new_account.add_interest(1)
    print("Balance: " + new_account.get_balance())
    print("Action: Add interest 2% (ineligible)")
    new_account.add_interest(2)
    print("Balance: " + new_account.get_balance())
    print("Action: Deposit $125,000.99")
    new_account.deposit(125000.99)
    print("Balance: " + new_account.get_balance())
    print("Action: Withdraw $.99")
    new_account.withdraw(.99)
    print("Balance: " + new_account.get_balance())
    print("Action: Deposit $126,500.00")
    new_account.withdraw(126500.00)
    print("Balance: " + new_account.get_balance())
    print("Action: Withdraw $10.00")
    new_account.withdraw(10.00)
    print("Balance: " + new_account.get_balance())
    print("Action: Add interest 1% (ineligible)")
    new_account.add_interest(1)
    print("Balance: " + new_account.get_balance())
    print("Action: Withdraw all funds")
    new_account.withdraw_all()
    print("Balance: " + new_account.get_balance())
    print("Action: Withdraw $.99 (oh no! negative balance)")
    new_account.withdraw(.99)
    print("Balance: " + new_account.get_balance())


main()


""" PROGRAM RUN
Action: Open New Account - Initial Deposit $500.00
Balance: $500.00
Action: Deposit $500.00
Balance: $1,000.00
Action: Withdraw $2000.00 (and get penalty)
Balance: $990.00
Action: Add interest 1%
Balance: $999.90
Action: Add interest 2% (ineligible)
Declined, you need to wait until next month.
Balance: $999.90
Action: Deposit $125,000.99
Balance: $126,000.89
Action: Withdraw $.99
Balance: $125,999.90
Action: Deposit $126,500.00
Balance: $125,989.90
Action: Withdraw $10.00
Balance: $125,979.90
Action: Add interest 1% (ineligible)
Declined, you need to wait until next month.
Balance: $125,979.90
Action: Withdraw all funds
Balance: $0.00
Action: Withdraw $.99 (oh no! negative balance)
Balance: -$10.00

Process finished with exit code 0
"""

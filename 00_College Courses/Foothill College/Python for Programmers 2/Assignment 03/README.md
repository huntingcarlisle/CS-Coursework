Object Oriented Programming
---------------------------

Application:  Implementing and Testing a Bank Account Class
-----------------------------------------------------------

_Make sure that you have read and understood_

*   **_Unit module3_**
*   **_Helpful Python3 tutorial links:_**
    *   [**_Classes_** (Links to an external site.)Links to an external site.](https://docs.python.org/3/tutorial/classes.html)
    *   [**_decimal - Decimal fixed point and floating point arithmetic_** (Links to an external site.)Links to an external site.](https://docs.python.org/3/library/decimal.html)

before submitting this assignment.  Hand in only one submission.

**Understand the Application**

Your task this lab is to design, implement and test your own class called **BankAccount** that models a simple bank account.  The bank account has a balance that can be adjusted by deposits and withdrawals.  Your class will implement this behavior.

Floating-point numbers are approximate values and can lead to rounding errors.  As a result, working with floating-point numbers can yield unexpected results.  A more reliable way to work with currency calculations is to use the **decimal** module to work with _decimal numbers_.  Decimal numbers work like a floating-point number, except that they are exact values so that you do not have to worry about the unexpected results that can be introduced by floating -point numbers.  

**The Program Spec**

Write a basic class that simulates a bank account that supports the following options:

*   Customers can deposit and withdraw funds.
*    If sufficient funds are not available for withdrawal, a $10.00 overdraft penalty is charged.
*   Once within a given month, interest can be added to the account. The interest rate can vary every month.

**Class BankAccount **

**Instance Member:** (Decimal) balance

I**nstance Methods**

*   **constructor** - Constructs a bank account with a given balance. Provides the default parameter **initial\_balance** (default balance = Decimal("0.0").
*   **deposit -** Deposits money into the account.  Takes the parameter **amount** to deposit. 
*   **withdraw** - Makes a withdrawal from the account **_or_** charges a penalty if sufficient funds are not available.  Takes the parameter **amount** to withdraw.
*   **add\_interest** - Adds interest once monthly to a positive account balance.  Takes the parameter **rate** that represents the current rate of interest (for allowable rate of interest 1% <= **rate** <= 2%). Monitor the date and only apply the rate calculation once monthly.
*   **get\_balance** - Returns the current account balance.

**Deliverables:  2 files to submit:**

*   Your bank account class file (name this file **yournameBank.py**) **_and_**
*   Your class test driver (name this file **yournameLab3.py**) 

Example:  

Ann Foothill's bank account class filename would be annFoothillBank.py  

Ann Foothill's test driver filename would be annFoothillLab3.py

Provide a copy of your test run in your test driver file.

Be sure to comment out your run so that your **.py** file will still run in the grader test bed.  

**Input Error Checking:  **Mutators must validate parameter data before writing to private instance fields.  If parameter data is invalid there is no change in state of the bank account.

**Test Run Requirements:** Provide a test driver that includes at minimum the following actions:

*   Instantiate a bank account with an original balance of $1000.00
*   Deposit $500.00
*   Withdraws $2000.00
*   Adds 1% interest 
*   Adds  2% interest
*   Deposit $125,000.99
*   Withdraws $0.99
*   Withdraws $126,500.00
*   Withdraws $10.00
*   Adds 1% interest

Show the account balance after each action.

Your test driver will need to import your class.

Example:

from yournameBank import BankAccount

Example:  Ann Foothill would import her BankAccount class into the test driver as follows:

from annFoothillBank import BankAccount

If you need an example, see the Unit 3 Module code examples.

Here are some tips and REQUIREMENTS:

1. Always use self for the first argument to instance methods.

2\. Use named constants versus literal values.  

3\. Format currency output display values to 2 decimal places.  Supply the $ symbol.  Reflect negative balances as -$ (i.e. -$10.00).  Display thousands separators.

**More:**

*   Be sure that all output is descriptive.  
*   No user input should be done in this program.

I am not supplying a sample output this week - the above description is adequate.
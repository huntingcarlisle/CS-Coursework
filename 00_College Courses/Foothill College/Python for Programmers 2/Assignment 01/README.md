Arithmetic, Data Types, User Input, Formatting Output, Importing Modules - Grade 18.5 out of 18.5
------------------------------------------------------------------------

_Make sure that you have read and understood_

*   **_Unit module1_**
*   [**_Python Code Quality Guidelines_**](/courses/7633/files/1265125/download?verifier=HMn4MdlN9H1ee0V7iREucYCHCDPpNstno6bOllse&wrap=1 "Python Code Quality Guidelines.pdf")[![Preview the document](/images/preview.png)](/courses/7633/files/1265125/download?verifier=HMn4MdlN9H1ee0V7iREucYCHCDPpNstno6bOllse&wrap=1 "Preview the document")
*   **_Helpful Python3 tutorial links:_**
    *   [_Built-in Types_ (Links to an external site.)Links to an external site.](https://docs.python.org/3/library/stdtypes.html)
    *   [_datetime - Basic date and time types_ (Links to an external site.)Links to an external site.](https://docs.python.org/3/library/datetime.html)
    *   [_Input and Output_ (Links to an external site.)Links to an external site.](https://docs.python.org/3/tutorial/inputoutput.html)
    *   [_PEP 8 -- Style Guide for Python Code_ (Links to an external site.)Links to an external site.](https://www.python.org/dev/peps/pep-0008/)

before submitting this assignment.  Hand in only one submission.

Every programming assignment is as much a test of **English language comprehension **as it is a test of programming or mathematical skills. This week, the explanations of the formulae below are given clearly in plain English if you read carefully. However, if there is **_any_** question about what is being asked, you are urged to ask for clarification in the public forums.  

**Understand the Application**

Create two int variables, **my\_id** and **n\_let**, into which will be stored:

*   **my\_id **\= The sum of the numbers in your College Generated **student ID**.  (This is the sum of an 8-digit number; not to confuse it with your social security # or a password, which it is not).
*   **n\_let** _\=_ The number of letters in your **family (last) name.**

In order to receive any credit for this assignment, these two values must match what I have for you on my class roster.

Your program will compute some values based on these two numbers, so that each student will have a unique output.

**The Program Spec**

The following expressions assume that you have stored the sum of the numbers of your student ID into the variable **my\_id**, and the number of letters in your last (family) name into the variable **n\_let**. Your program will compute these values based on the user input data supplied for name and ID.

Your program should compute and display the results for the following expressions:

expression1:             my\_id / 2

expression 2:            my\_id % 2

expression 3:            2 + 3 + … + n\_let

expression 4:            my\_id + n\_let

expression 5:            abs(n\_let – my\_id)

expression 6:            (my\_id) / (n\_let + 1100)

expression 7:            (n\_let % n\_let) and (my\_id \* my\_id)

expression 8:            1 or (my\_id / 0)

expression 9:            round(3.15, 1)

Write a Python program that computes and displays the results of these nine expressions. Import the [datetime (Links to an external site.)Links to an external site.](https://docs.python.org/3/library/datetime.html) module to generate the date of your test run. Print this date in your run output.  

**Input Error Checking:** Validate all user input before computation.  A valid student id contains only digits and is of length 8.  A valid last name contains only characters and is of a minimum length 2, maximum length 15.

Your program display should look something like this (although the values will differ for each student):


Enter your family name: Student  
Enter your student ID: 12345678  
my\_id is: 36  
n\_let is: 7  
expression 1: 18.00  
...  
Today's date is 2018-04-12

Here are some _tips_ and REQUIREMENTS:

1.  The "..." is called an "ellipsis" and means "and so forth". So, when n\_let is 7, the expression **2 + 3 \_+... + nLet **really means to **add the numbers from 2 all the way up to and including the number 7.**
2.  Your personal information is supposed to be entered as user input.
3.  Assign the arithmetic expression results to an ordered collection data structure (i.e. list or tuple).
4.  Use a space around operators.
5.  Keep source statement width < 80 characters so as not to cause text wrap-around in some editors.
6.  Perform the necessary data conversions to perform arithmetic operations.
7.  As you can see in the sample run, the first thing your program needs to do is print out your **family (last) name **and your **student ID**. 
8.  Format floating point numbers to 2 decimal places.
9.  Import the [datetime  (Links to an external site.)Links to an external site.](https://docs.python.org/3/library/datetime.html)module to display the current date of your test run submission.
10.  Ensure that your solution is well organized. Providing a program header and comments to document and organize your source code. 
11.  Provide a commented out copy of your program run.  Enclose the run inside of comment delimiters so that your program will run in the grader test bed.  Place the run after your program source code. 

**Deliverable:**

1\.    Hand in a **.py** file (Example yournameLab1.py).

2.    Include a Program Header followed by the Python source followed by the run (comment out the run).  

**Example Lab File Format Submission:  **

*   Student Name:  Ann Foothill
*   Submission file name [annFoothillLab1.py](/courses/7633/files/1265093/download?verifier=GeCw3GXd2YSdWb1B5OnL08s7SJO2gRDIs1wNyaeS&wrap=1 "annFoothillLab1.py")[![Preview the document](/images/preview.png)](/courses/7633/files/1265093/download?verifier=GeCw3GXd2YSdWb1B5OnL08s7SJO2gRDIs1wNyaeS&wrap=1 "Preview the document")

[Example Solution](/courses/7633/files/1329477/download?verifier=OQuXKAL91Z6n6MMBLopErz2iJjBLJ3TtfvLgkYQ2&wrap=1 "CS21B_ExampleSolnLab1.py")[![Preview the document](/images/preview.png)](/courses/7633/files/1329477/download?verifier=OQuXKAL91Z6n6MMBLopErz2iJjBLJ3TtfvLgkYQ2&wrap=1 "Preview the document")

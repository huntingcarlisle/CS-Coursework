Assignment 2 - Arithmetic
=========================

Make sure you have read and understood

*   both **_m_**_**odules A**_ and _**B**_ this week, and
*   _**module 2R - Lab Homework Requirements**_

before submitting this assignment. Hand in only one program, please. 

#### Some Easy Arithmetic

_Every programming assignment is as much a test of **English language comprehension** as it is a test of programming or mathematical skills.  This week, the  explanations of the formulae below are given clearly in plain English if you read carefully.  However, if there is any question about what is being asked, you are urged to ask for clarification in the public forums._

### Understand the Application

You will create two **int** variables into which you will store

*   Your Foothill College _**student ID.**_ (This is normally an 8-digit number;  don't confuse it with your social security # or a password, which it is not.)
*   The number of letters in your _**family (last) name**_.

In order to receive any credit for this assignment, these two values must match what I have for you on my class roster.

Your program will compute some values based on these two numbers, so each student will have a unique output.

### The Program Spec

The following five expressions assume that you have stored your student ID into the variable **_my_**_**Id**_, and the number of letters in your last (family) name into the variable _**numLet**_.  You can manually enter both of these using _**assignment statements**_ in your program source.  No user input allowed.  Compute the following five values:

#1:       m y I d  %  17

#2:    (  m y I d  + 4  )   %  9

#3:    m y I d   m y I d  +  500.

#4:     1  +  2  +  3  + . . .  +  n u m L e t

#5:     15 , 000.   80.  +  \[   m y I d  − 123 , 456    (  n u m L e t  + 20  )  2   \]

First do the math on paper so you know what answers your program should generate (but don't hand this stage in).  Write a program that computes and displays these five values.   Your run should look something like this (although the values will differ for each student):

/\* -------------------------- Run ----------------------

My family name is Cecil
My Student ID is 22222222
The number of characters in my last name is 5

Expression #1 ------------ : 7

Expression #2 ------------ : 2

Expression #3 ------------ :  ...

   ...

------------------------------------------------------- \*/

Note that the first three lines are output from your program, not added after the run.  This should all be done in one run of a single program, not several runs. 

Here are some tips and **_REQUIREMENTS_**:

1.  Don't limit the precision of the expected double output in any way. (E.g., Avoid  using advanced formatting to make the result look shorter or neater than they would by using the simpler default formatting.)  We want to see as many decimal places for the double results as possible.
2.  The "..." is called an "ellipsis" and means "and so forth."  So, in expression **#4** if your _**numLet**_ is 8, the expression **1 + 2 + ... +** _**numLet**_  really means 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8.  Since we have not covered loops, just use this latter expression to compute result in expression **#4**.
3.  Do not try to take short cuts. For expression **#4**, I want to see every number in the computation.  As an example, in hint **#2** directly above, you see that I listed the entire addition when describing the expression **1 + 2 + ... + _numLet_**, so your program should also use the full expression. Remember that long source code lines (> 80 chars) are illegal according to my style rules.
4.  Your personal info is not supposed to be entered by the user at run-time.  You should make assignments to the variables in your program.
5.  Only one run, please, which means you must produce all **five** answers in your program in a single source file.
6.  Expressions **#1**, **#2** and **#4** should use ordinary **_int arithmetic_**, which means using the **int** variables without any special tools.  However, expressions **#3** and **#5** are meant to display the _**full double accuracy**_ that the divisions will produce,  You should take appropriate action to do that.
7.  Use as few variables as possible. You can, for example, use one **intResult** variable for the three int expressions and a second **doubleResult** variable for the two double expressions.  However, don't use five separate result variables.
8.  As you see in the sample run, the first thing your program needs to do is print out your **_last (family) name_**, your _**student ID**_, and the number of characters, including special symbols, if any which you are using as a basis for these computations.
9.  Do not use any power or exponential methods to compute #5.  First, we haven't had that yet, and second, it is inefficient to use a **pow()** method to compute small integral powers likes squares or cubes. Instead, use multiplication to compute the power(s) you need.
10.  Each incorrect result or expression will incur a penalty of -3 to -4, depending on the severity of the error that caused the problem, so be sure to check your work.

Once your assignment is graded and returned, you can view the instructor solution here:

*   [Quiz List](/courses/7627/quizzes)

Your access code will be provided in your graded assignment comments.  Find the assignment in the list, click "Take Survey" and you will see the solution.  Even though it is called a "Quiz", it is actually just a solution; there is no need to submit anything, just open the quiz and see the solution.
Lab Assignment 4 - Grade: 18.5 out of 18.5
================

*   Due Tuesday, 10/23/18 by 11:59pm
*   Points 22.5
*   Submitting a file upload
*   Available Oct 17 at 8am - Oct 25 at 11:59pm 9 days

Regular Expressions 
--------------------

Application: Date Format Converter
----------------------------------

**_Make sure that you have read and understood_**

*   **Module week4**
*   **Text: _The Quick Python Book_, Third Ed., Naomi Ceder, Ch. 16**
*   **Helpful Python3 tutorial links:**
    *   [Regular Expression Operations](https://docs.python.org/3/library/re.html)
    *   [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)
    *   [Text Processing Services](https://docs.python.org/3/library/text.html)
    *   [_Built-in Exceptions_](https://docs.python.org/3/library/exceptions.html)

Before submitting this assignment.  Hand in only one submission.

**Format Conversion**

Often, in working with big data, the task of converting document formats to alternate formats either for data storage and retrieval or document presentation presents itself. 

**Understand the Application**

For this lab, the task at hand is to create a date format converter.  Your program will convert a date in the format `mm/dd/yyyy` to the format `month day, year`.

**The Program Spec**

Prompt the user to obtain a date from the user.  Specify the required input format: `mm/dd/yyyy`  Use a regular expression to validate the user input date format.  If the format is incorrect raise a `SystemExit`. 

Split the input string into respective month, day, and year components.  Using a list to hold the month format as a string, convert the month input to the correct string month name.  You will need to calculate an appropriate index to retrieve the correct month name from the month list.

Use the Gregorian calendar for valid **dd**:  

The 12 Months
-------------

The [Gregorian calendar](https://www.timeanddate.com/calendar/gregorian-calendar.html) consists of the following 12 months:

1.  [January](https://www.timeanddate.com/calendar/months/january.html) - 31 days
2.  [February](https://www.timeanddate.com/calendar/months/february.html) - 28 days in a [common year](https://www.timeanddate.com/date/common-year.html) and 29 days in [leap years](https://www.timeanddate.com/date/leapyear.html)
3.  [March](https://www.timeanddate.com/calendar/months/march.html) - 31 days
4.  [April](https://www.timeanddate.com/calendar/months/april.html) - 30 days
5.  [May](https://www.timeanddate.com/calendar/months/may.html) - 31 days
6.  [June](https://www.timeanddate.com/calendar/months/june.html) - 30 days
7.  [July](https://www.timeanddate.com/calendar/months/july.html) - 31 days
8.  [August](https://www.timeanddate.com/calendar/months/august.html) - 31 days
9.  [September](https://www.timeanddate.com/calendar/months/september.html) - 30 days
10.  [October](https://www.timeanddate.com/calendar/months/october.html) - 31 days
11.  [November](https://www.timeanddate.com/calendar/months/november.html) - 30 days
12.  [December](https://www.timeanddate.com/calendar/months/december.html) - 31 days

Below is an example conversion:
```
Enter a date (mm/dd/yyyy): 01/01/2018  
The converted date is: January 01, 2018
```

**Testing Requirements:**  Use a loop construct to display 5 date conversions.  The 1st 3 test cases should consist of valid user input.  The 4th test case should be a leap year. The last 5th test case should consist of invalid user input.

Here are some tips and REQUIREMENTS:

1. A list is used to store the month string names.
1. An index is calculated to retrieve the correct month from the list based on the user input.
1. A user prompt instructs the user of the expected input date format: `mm/dd/yyyy`
1. Obtain and validate user input. Display an error message and raise a `SystemExit` if invalid. 
1. The converted date output is in the format: `month day, year` 
1. The output display: month is spelled out, the day is 2 digits dd and the year is 4 digits dddd.
1. Use named constants instead of literal values (i.e. `NUM_DATES = 5`).
1. Require 2 digits be supplied for mm and dd, 4 digits be supplied for year **y**yyy  (require that the leftmost digit of the year **not** to be a 0).  Use valid user input date range:  01/01/1000 - 12/31/2999.
   

Lab 4 Rubric
-----

Criteria |  Pts
--- | ---
**On Time Submission** | 4.0 pts  
**Application: Date Format Converter**: Satisfies the assignment class specification. | 9.0 pts
**Commented out run included**: A copy of the program test run output is attached after the source code inside of the test driver file (enclosed within comment delimiters). Five test cases (4 valid, 1 invalid). The run matches the source code submitted. | 9.0 pts 
**Coding Style**: Includes a program header that includes name and a short description as to what the application does. Is correctly formatted. Source is documented. | 0.5 pts
**Total Points:** | 22.5 pts

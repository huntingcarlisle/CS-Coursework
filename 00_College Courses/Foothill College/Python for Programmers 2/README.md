CS 21B-01W Intermediate Python Programming
------------------------------------------



Fall 2018 | CRN 21996 | Foothill College
----------

Instructor: Geri Lamble

E-mail:  [lamblegeri@fhda.edu](mailto:lamblegeri@fhda.edu)

**Lectures:** online **Labs:** online

### Course Description

This course builds on the student’s prior knowledge of the Python programming language by offering a more in-depth and advanced approach to building effective Python applications.  Specific topics include user interfaces, networked applications, databases, multi-threading and regular expressions.  The course reinforces object oriented design, thorough documentation, testing and conventional programming style.

**Prerequisite: ** Advisory CS 3A or CS 21A or relevant experience

**RecommendedText: **The Quick Python Book, Third Edition, by Naomi Cedar ISBN: 9781617294037

The text for the course is _recommended_ in that forum discussion questions can be directed to a section in the book for further explanation. It is expected that students will have access to this reference.

This book can be ordered through the [**Foothill Bookstore** (Links to an external site.)Links to an external site.](http://books.foothill.edu/).

**Required Software: Python3.**  You will need access to a Python interpreter and a text editor.  In this class we will be using Python3.

Software: 
----------

Go to the [**www.python.org** (Links to an external site.)Links to an external site.](http://www.python.org) Downloads page link listed below.  Be careful to choose the version for your operating system and hardware.  The python.org website also provides user documentation and tutorials.

*   [**Python 3 Downloads** (Links to an external site.)Links to an external site.](http://www.python.org/)
*   [**Python documentation** (Links to an external site.)Links to an external site.](https://docs.python.org/3/)
*   [**Python Tutorial** (Links to an external site.)Links to an external site.](https://docs.python.org/3/tutorial/index.html)

### Course Objectives

Understand Python’s memory model and issues with mutability.

Recognize various aspects of Python code that exhibit better performance.

Discuss implementation differences between the standard data types.

Distinguish between Python 2 and 3, use migrations tactics, discuss porting issues, and write code compatible with both versions.

Write code that executes other (Python and non-Python) programs.

Use the standard Python developer and testing tools.

Write Python code with fewer bugs and other issues.

### [Student Learning Outcomes (Links to an external site.)Links to an external site.](http://www.fgamedia.org/faculty/loceff/cs_courses/common/slos/cs_slos_1.html)

A successful student will be able to develop a Python program that runs other programs, accesses a database, and transfers files over a network.

A successful student will be able to develop an event driven Python program that interacts with the user through a graphic user interface that employs windows, dialog boxes, buttons, menus and text fields.

### Grades

Your grade is determined by:

*   Assignments 75%
*   Exams 25%

### Tests

There will be a midterm exam (worth 20 points) and a comprehensive final exam (worth 40 points). Exams will be administered online.

### Lab Assignments

There will be eight required lab assignments (worth 22.5 points each).  There is an optional ninth lab assignment that can be used to replace a low lab score. Labs will be turned in online. 

### Grading Scale

| **Grade  ** | **Lower %  ** | **Upper %** |
|--- | --- | --- |
| A | 93% | 100% |
| A- | 90% | 92% |
| B+ | 87% | 89% |
| B | 83% | 86% |
| B- | 80% | 82% |

Course Expectations
-------------------

### Attendance Policy

Regular attendance is required.  Students will be dropped for non-participation for the following:

*   Not posting a first week Introduction
*   Not submitting the first assignment
*   Missing two consecutive lab submissions
*   Missing the midterm exam
*   Missing three total lab submissions

### Course Communication

Course material will be provided in Canvas including announcements, discussions, lecture notes, lab assignments, and exams.

Course Outline
--------------

**Week** | **Topics**
--- | ---
1 | Introduction. Python Review: Basic Data Types: Numeric, Sequence, Unordered Collections; Hashing, Object Memory Model
2 | More Python Review: Control Flow, Functions, File I/O, Exceptions
3 | Modules and Packages, Object oriented programming, advanced function: map, filter and reduce
4 | Regular Expressions
5 | Databases
6 | The Web and Search; Midterm Exam
7 | GUI
8 | Network Programming
9 | Internet Client Programming
10 | Multi-threading Programming
11 | Web Programming: CSI and WSGI
12 | Final Exam


Help Resources
--------------

[STEM Success Center](https://foothill.edu/stemcenter/)

College Policies
----------------

### Academic Honesty

Your lab and exam submissions must be your own work.

The following guidelines apply:

You are encouraged to discuss in the forum about course questions but you may not examine nor reuse any other student's code. You are not allowed to copy code from **any** source — other students, the Web, etc.

Disability:
-----------

To obtain disability-related accommodations, students must contact the [**Disability Resource Center (DRC)**](https://foothill.edu/drc/) at the start of the quarter.

To contact DRC, you may:  

·      Visit DRC in Room 5400  
·      Email DRC at [drc@foothill.edu](https://www.mail.fhda.edu/owa/redir.aspx?C=1YvRhd7XtMJyiWW05thSdW7V-VkgHcxXX25DKeZh8S_1cehH_wHVCA..&URL=mailto%3aadaptivelearningdrc%40foothill.edu)\>  
·      Call DRC at 650-949-7017 to make an appointment  

If you already have an accommodation notification from DRC, please contact me privately to discuss your needs. 

Changes:
--------

This syllabus is subject to changes, additions, deletions, and/or corrections.

**Last Updated: ** 9/23/2018 2:42 PM

# Python Code Quality Guidelines

Clarity and readability are important, as well as extensibility, meaning code
that can be easily enhanced and extended.

Use these coding standards to evaluate your own code.

Style Standards

1. Variable names: all lowercase, with underscores between any words

```
Please do not use camelCase, but instead words_with_underscores.
```
2. Use 4-space Indents, no tabs

```
Insert 4 spaces whenever using the [Tab] key. If you are using an IDE
editor, you must configure it to do the same.
```
3. One space on either side of operators

```
var = aa + bb # note one space on either side of = and +
```
```
This might seem picky, but it is all for readability, which is extremely
important in the professional world.
```
4. No space between function name and argument list (parentheses)

string_length = len('hello') # not len ('hello')


Naming and Clarity

5. Use descriptive variable names; never use the plural for a loop variable

```
Variable names should be descriptive to aid the reader, who should not
have to hold the meaning of several variables in mind at once (as would be
if named aa, bb, etc.). If a variable holds the user's first name, it should be
called first_name, user_fname, fname, i.e. something descriptive. If you
call first name name1 and last name name2 you're not being as clear. If
you call first name aa then the variable's identity becomes opaque to the
reader (until he or she traces it back in your code).
```
```
In particular there is one particular misnomer that I caution you to avoid:
```
```
fh = open('datafile.txt')
for lines in fh: # please use singular ('line')
items = lines.split() # are we splitting one line, or many?
```
```
We use the for construct to loop through a file line-by-line, but the control
variable lines is supposed to be only one element at a time. Therefore it's
misleading to call it lines when it's really just one line.
```
6. Do Not Use the Built-In Names for Your Variables

```
It would be easier if Python would prohibit the use of these names, but it
does not. list, dict, file, len, float, int, str and other builtin function names
can be overwritten if we assign to these labels.
```
```
>>> len('hello')
5
>>> len = 0.
>>> len('hello')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
```
7. Use the string format() method to combine values with strings.

```
Some folks prefer to stick to string concatenation or use commas when
printing -- instead, use the string format() method to combine values
```

```
(numbers or strings) with strings. (This is not a style convention, yet I feel
this is something you should be familiar with.)
```
```
Compare this:
```
```
name = 'Ann'
age = 2 5
print('My name is ' + name + ' and my age is ' + str(age) + '.')
```
```
to this:
```
```
name = 'Ann'
age = 25
print('My name is {} and my age is {}'.format(name, age))
```
8. Comment your code only when needed for clarity, and please remove
diagnostic code

```
Most code if clearly written can be read and understood easily, but some
code is by nature a little harder to read (such as list comprehensions,
lambdas, code involving multidimensional structures, etc.). In these cases
it makes sense to add a comment to explain what is happening.
```
```
Some students like to comment each of their code steps. One method is to
start with a comment outline and then write code to fulfill each
comment. This is fine for draft work, but please remove unnecessary
comments before submitting.
```
9. Put a String Comment at the top of the script with title description and
author

```
This is a great habit that you will thank yourself for acquiring, and it will
help me in reviewing as well. No matter how short, every script should
have an identifier that will make it instantly recognizable to you when you
open the script later (otherwise you are forced to start reading it to get a
sense of what it is supposed to be doing).
#!/usr/bin/env python 3
"""ann _foothill _1.2.py -- calculate a tip based on user input"""
```

```
This "docstring" should be the first line of your code. Such strings can
also be used for automatically generated documentation. Customarily we
use a "triple-quoted string" for this purpose, although it can be a single- or
double-quoted string as well.
```
Code Organization

10. Conceptualize the logical "steps" of your code.

```
Consider that every program takes discrete steps; separate your code
visually (with blank lines) so these steps can be quickly identified by the
reader as well. Note: keep in mind that these are guidelines and do not
need to be followed in every case; you will begin to develop good judgment
about what is readable, what is well organized, etc.
```
```
a. Take input. Most programs begin by taking user input or reading
command-line input, which tells the program how to function.
```
```
b. Validate and/or "normalize" input. If the input is coming from the user, it
has to be checked to see if it is valid. It may also need to be converted into
a usable form -- for example, if the user is asked to input an integer, the
string needs to be converted to an integer. If the user is asked to input a
filename, the program must determine if the file exists and can be read.
```
```
c. Process or compute the data. This is the main event - once everything
has been normalized and is ready to go, then we go through the
computations -- summing, aggregating, etc.
```
```
d. Output the results. Finally, we inform the user of the results by printing
the results of the computation.
```
```
Again, these steps do not always apply -- but if you can avoid mixing them
(for example, normalizing while you are in the middle of computation) then
your code will be much clearer and more straightforward.
```
11. Use Blank Lines Sparingly, but Use Them to Separate Logical Steps

```
Think of your code as an essay with paragraphs. Note in the code above
that each step is comprised of a few statements and these are single-
```

```
spaced, and that between steps we have placed a blank line. This
indicates to the reader what the steps are and how best to read the
code. This sort of logical separation greatly aids readability.
```
12. "Flat is better than nested"

```
Nested code creates logical dependencies, which means that one section
of code is dependent on the other to be fully understood by the reader. If
the dependencies are not needed, we have unnecessary logical
complexity. Compare these two code snippets -- in the first below, notice
that the computational while loop (bolded below) is logically dependent on
the if and the other while, even though it does not need to be. Also note
that the if and else are separated, requiring the reader to unite those two
pieces in order to make sense of it.
```
```
counter = 0
while True:
max_count = input('enter an int: ')
if max_count.isdigit():
while counter < max_count:
print(counter)
counter = counter + 1
print('done')
else:
print('sorry, bad input, try again')
```
```
In a flatter (i.e., less indented) version of the same code below, each step
(take and validate user input; convert input to int(); perform the
computation) is separate, flatter and easier to read. It is also easier to
maintain. The mind does not need to take in the whole of the code in order
to comprehend the logic - instead one can understand the first step, then
move on to the next step without having to remember anything.
```
```
counter = 0
while True:
max_count = input('enter an int: ')
if max_count.isdigit():
break
print('sorry, try again')
max_count = int(max_count)
while counter < max_count:
print(counter)
counter = counter + 1
```

13. Avoid Repetition (DRY principle)

```
Don't Repeat Yourself: if you find yourself issuing the same statement or
group of statements more than once, ask whether the repetition can be
eliminated.
```
```
When you have finished your program, go over it once more and look for
repetitions.
```
```
while True:
your_guess = input("Your guess? (q to quit): ")
if your_guess == "q":
exit()
if int( your_guess ) < number_to_guess:
counter = counter + 1
print("your guess is LOWER than the number I'm thinking of.")
if int( your_guess ) > number_to_guess:
counter = counter + 1
print("your guess is HIGHER than the number I'm thinking of.")
if int( your_guess ) == number_to_guess:
counter = counter + 1
print("you got it! You guessed it in {} tries".format(counter))
quit()
```
```
Can you move the counter = counter + 1 to a different location where it
only needs to appear once? Can you also perform the int() conversion
once so it is not repeated?
```
14. Avoid Using Intermediate Structures

```
This one is harder to explain in specific, but I have found that many
students get used to using one container structure (in particular, list is a
favorite) and so try to do everything with that structure. They also like to
break down steps into multiple loops, by looping through one list, modifying
an element and appending it to a new list, then looping through the new
list, modifying an element and appending the element to a third list, etc.,
when the whole thing could be done in one list, by performing successive
operations in the one loop.
```
```
In this example, stripped_lines, an intermediate structure, is not
necessary:
```
```
stripped_lines = []
ids = []
```

```
for line in open(filename).readlines():
line = line.rstrip()
stripped_lines.append(line)
for line in stripped_lines:
elements = line.split(':')
ids.append(elements[-1])
```
These two loops could be consolidated into one loop:

```
ids = []
for line in open(filename).readlines():
line = line.rstrip()
elements = line.split(':')
ids.append(elements[-1])
```

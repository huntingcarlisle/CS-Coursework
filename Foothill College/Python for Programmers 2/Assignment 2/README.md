Lab Assignment 2
Due Tuesday by 11:59pm  Points 22.5  Submitting a file upload  File Types py and txt Available Oct 3 at 8pm - Oct 11 at 11:59pm 8 days
Programming with Files
Application:  Data Analysis and Exception Handling 
Make sure that you have read and understood

Unit module2
Helpful Python3 tutorial links:
Control Flow Tools (Links to an external site.)Links to an external site.
Reading and Writing Files (Links to an external site.)Links to an external site.
Errors and Exceptions (Links to an external site.)Links to an external site.
before submitting this assignment.  Hand in only one submission.


Reading from and Writing to a File

A file is a grouping of related data that can be read by a computer program.  Files may be stored in many different places including the hard drive, a thumb drive, on a CD, at a network location, really any place where a program could have access to it. While files occur in many forms and sizes, a text file is a bunch of text written using an editor and usually stored on a hard drive.  Files can be read and written from Python programs.  Files are another type of sequence as far as Python programs are concerned and we can iterate over them just as we would any sequence.  Files are sequences of strings, one string for each line of the file.  To read from a file we open it and then iterate over the lines of the file. 

When writing to a file we use the file.write method.  Unlike the print function, you cannot write multiple items by separating them with commas.  The write method takes only one argument, the string to write.  To write multiple items to a line of a file, you must use the string concatenation (i.e. the + operator) to concatenate the items together.  When comma separated items in a print statement are printed, a space character is automatically added between between comma separated items. This is not true of string concatenation.  If we want a space in the concatenated strings, we must add it ourselves.

If we have non-string items to write to a file, they must be converted to strings using the str function.  Otherwise, we will get a run-time error when Python tries to concatenate a string to a non-string item.

Understand the Application

This week’s program we will read from one file and write to another file. 

The Program Spec

It is frequently the case that a file contains more than one line that relates to each other in some way creating a record in a file. Whether you are writing code in Python or some other language, this Reading Records From a File pattern comes up over and over again.  To read a multi-line record from a file we can use the record format specification as a design guide in reading records from a file.

You will read a record from one file and write a new record to another file. 

Write a program that checks for the following expectations of a text file to read:

The file must exist
A record in the file must have the following format:
Last name
First name
Address
City, State Zip Code
Phone Number
The program prompts the user for the name of a file.  

Key potential errors to program for include:

The file may not exist
The file might not contain complete record entries
For a valid text file, the processing data task is to:

count the number of record entries in a text phonebook file
create a new file that contains abbreviated record entries to includes 2 lines:
(Last Name, First Name; Phone Number). 
Write a program that counts the number of entries in a phonebook file. Print out a result message and number of entries in a phonebook for a valid address text file. Create a second file, phonebook.txt, where the records created have the following format:

Last name, First name
Phone Number
Not to allow duplicate entries in the phonebook.txt created file.  

Allow the provision to evaluate multiple text files in one program execution.

Deliverables: 

yournameLab2.py  Your source code solution and a copy of the run pasted into your source submission file.  Be sure to comment out your run so that your .py file will still run in the grader test bed.  
yournamephonebook.txt The new record text file that your program creates.
Input Error Checking: Check if the file exists.  Check if the file is valid.  You can assume the the record line entries have been correctly entered in the file read.  You do need to check if each record entry is complete. 

Test Run Requirements:  Three test files are provided to use as a test suite for your program. Demonstrate a test case to raise exception conditions.  Use the provided test files below (demo.txt, addressbook.txt, err.txt)  as your test run validator.  

Here are some other tips and requirements:

1.    Keep provided test files intact. 

demo.txtPreview the document
addressbook.txtPreview the document
err.txtPreview the document
2.    Handle exceptions.

3.    Provide an appropriate display message  for your test cases.  

4.    Provide the count for a valid data file.  

Here is a sample partial run:

Please enter the file name to read <Hit Enter to Quit>: nofile.txt
Error: file not found.
Please enter the file name to read <Hit Enter to Quit>: demo.txt
You have 2 entries in your demo address book.
Please enter the file name <Hit Enter to Quit>: address.txt
Error: file not found.
Please enter the file name <Hit Enter to Quit>: addressbook.txt

...
Rubric
Lab 2 Rubric
Lab 2 Rubric
Criteria	Ratings	Pts
This criterion is linked to a Learning Outcome On Time Submission
Submitted on time 4 points One day late -2 points Two days late -4 points
4.0 pts
Full Marks
2.0 pts
0.0 pts
No Marks
4.0 pts
This criterion is linked to a Learning Outcome Source
Satisfies the application requirements as specified in the assignment.
9.0 pts
Full Marks
0.0 pts
No Marks
9.0 pts
This criterion is linked to a Learning Outcome Commented out run included
A copy of the program run output is attached after the source code (enclosed within comment delimiters). The run matches the source code submitted.
9.0 pts
Full Marks
0.0 pts
No Marks
9.0 pts
This criterion is linked to a Learning Outcome Coding Style
Includes a program header that includes name and a short description as to what the application does. Is correctly formatted.
0.5 pts
Full Marks
0.0 pts
No Marks
0.5 pts
Total Points: 22.5
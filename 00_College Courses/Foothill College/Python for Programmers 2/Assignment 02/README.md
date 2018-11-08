Programming with Files - Grade 18.25 out of 18.5
----------------------

Application:  Data Analysis and Exception Handling 
---------------------------------------------------

_Make sure that you have read and understood_

*   **_Unit module2_**
*   **_Helpful Python3 tutorial links:_**  
    *   [**_Control Flow Tools_** (Links to an external site.)Links to an external site.](https://docs.python.org/3/tutorial/controlflow.html)
    *   [**_Reading and Writing Files_** (Links to an external site.)Links to an external site.](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
    *   [**_Errors and Exceptions_** (Links to an external site.)Links to an external site.](https://docs.python.org/3/tutorial/errors.html)

before submitting this assignment.  Hand in only one submission.

**Reading from and Writing to a File**

A file is a grouping of related data that can be read by a computer program.  Files may be stored in many different places including the hard drive, a thumb drive, on a CD, at a network location, really any place where a program could have access to it. While files occur in many forms and sizes, a _text file_ is a bunch of text written using an editor and usually stored on a hard drive.  Files can be read and written from Python programs.  Files are another type of sequence as far as Python programs are concerned and we can iterate over them just as we would any sequence.  Files are sequences of strings, one string for each line of the file.  To read from a file we open it and then iterate over the lines of the file. 

When writing to a file we use the **file.write** method.  Unlike the print function, you cannot write multiple items by separating them with commas.  The write method takes only one argument, the string to write.  To write multiple items to a line of a file, you must use the string concatenation (i.e. the + operator) to concatenate the items together.  When comma separated items in a print statement are printed, a space character is automatically added between between comma separated items. This is not true of string concatenation.  If we want a space in the concatenated strings, we must add it ourselves.

If we have non-string items to write to a file, they must be converted to strings using the **str** function.  Otherwise, we will get a run-time error when Python tries to concatenate a string to a non-string item.

**Understand the Application**

This week’s program we will read from one file and write to another file. 

**The Program Spec**

It is frequently the case that a file contains more than one line that relates to each other in some way creating a **record** in a file. Whether you are writing code in Python or some other language, this _Reading Records From a File_ pattern comes up over and over again.  To read a multi-line record from a file we can use the record format specification as a design guide in reading records from a file.

You will read a record from one file and write a new record to another file. 

Write a program that checks for the following expectations of a text file to read:

*   The file must exist
*   A record in the file must have the following format:

1.  Last name
2.  First name
3.  Address
4.  City, State Zip Code
5.  Phone Number

The program prompts the user for the name of a file.  

Key potential errors to program for include:

*   The file may not exist
*   The file might not contain complete record entries

For a valid text file, the processing data task is to:

*   count the number of record entries in a text phonebook file
*   create a new file that contains abbreviated record entries to includes 2 lines:
*   (Last Name, First Name; Phone Number). 

Write a program that counts the number of entries in a phonebook file. Print out a result message and number of entries in a phonebook for a valid address text file. Create a second file, phonebook.txt, where the records created have the following format:

1.  Last name, First name
2.  Phone Number

Not to allow duplicate entries in the phonebook.txt created file.  

Allow the provision to evaluate multiple text files in one program execution.

**Deliverables: **

*   **yournameLab2.py**  Your source code solution and a copy of the run pasted into your source submission file.  Be sure to comment out your run so that your **.py** file will still run in the grader test bed.  
*   **yournamephonebook.txt** The new record text file that your program creates.

**Input Error Checking:** Check if the file exists.  Check if the file is valid.  You can assume the the record line entries have been correctly entered in the file read.  You do need to check if each record entry is complete. 

**Test Run Requirements:**  Three test files are provided to use as a test suite for your program. Demonstrate a test case to raise exception conditions.  Use the provided test files below (demo.txt, addressbook.txt, err.txt)  as your test run validator.  

Here are some other _tips_ and _requirements_:

1.    Keep provided test files intact. 

*   [demo.txt](/courses/7633/files/1327040/download?verifier=yktZy8HFd4H9ZgSPje6uIszKad3z2rdBGS9bvQCP&wrap=1 "demo.txt")[![Preview the document](/images/preview.png)](/courses/7633/files/1327040/download?verifier=yktZy8HFd4H9ZgSPje6uIszKad3z2rdBGS9bvQCP&wrap=1 "Preview the document")
*   [addressbook.txt](/courses/7633/files/1327039/download?verifier=cJbfNzNBDDMrvWKttvL6yktjzjBtfYUREsMwCJqn&wrap=1 "addressbook.txt")[![Preview the document](/images/preview.png)](/courses/7633/files/1327039/download?verifier=cJbfNzNBDDMrvWKttvL6yktjzjBtfYUREsMwCJqn&wrap=1 "Preview the document")
*   [err.txt](/courses/7633/files/1327773/download?verifier=UXjet31de3Mn8MzGtR9k0hUgtBte9hECzoQP562c&wrap=1 "err.txt")[![Preview the document](/images/preview.png)](/courses/7633/files/1327773/download?verifier=UXjet31de3Mn8MzGtR9k0hUgtBte9hECzoQP562c&wrap=1 "Preview the document")

2\.    Handle exceptions.

3.    Provide an appropriate display message  for your test cases.  

4\.    Provide the count for a valid data file.  

Here is a sample **partial** run:

Please enter the file name to read <Hit Enter to Quit>: nofile.txt  
Error: file not found.  
Please enter the file name to read <Hit Enter to Quit>: demo.txt  
You have 2 entries in your demo address book.  
Please enter the file name <Hit Enter to Quit>: address.txt  
Error: file not found.  
Please enter the file name <Hit Enter to Quit>: addressbook.txt  

...[](/courses/7633/files/1327040/download?verifier=yktZy8HFd4H9ZgSPje6uIszKad3z2rdBGS9bvQCP&wrap=1 "demo.txt")

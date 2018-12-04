Multithreaded Programming
-------------------------

Using threads in Python
-----------------------

**_Make sure that you have read and understood_**

*   **_module week 10 _**
*   **_Helpful Python3 tutorial link_**
    *   **[_threading - Thread based parallelism_ (Links to an external site.)Links to an external site.](https://docs.python.org/3/library/threading.html)**

In this optional lab you will have an opportunity to use Python's threading module to work with threads. 

_This bonus assignment is worth 22.5 points. Don't worry about the fact that it may say " 0 points possible." Do include a statement in your submission file to let me know what lab assignment you' would like this optional one to replace._

_/\* Please replace:   \*/_

 **Understand the Application**

For this lab you will create a basic application programming interface (API) for spawning multiple threads in a program using Python3's threading module. 

**The Program Spec**

Write a program that creates a _minimum_ of two threads with different target functions. Each thread will perform the work of each function.  Each function will compute a task (described below) and print out a result.

**Implementation Details**

Write a program that creates a _minimum_ of two threads using Python's threading module. The first thread will have a target function to compute and then display the result value. 

The second thread will have a target function to compute and then display the result value.

In short, the nth (2 <= _n_ <= 5) thread will have a target function to compute and then display the result.

Your program's main function will start the threads.  Do be sure to coordinate the output display so that first thread displays its result before the second thread, _and so on. _

**Test Run Requirements:** 

Here are some other _tips_ and requirements:

1\. Validate that the threads get created successfully.

2\. Use a minimum of 2 threads up to a maximum of 5 threads.

3\. The work of the target functions can be as basic as adding 2 numbers to as complex as solving one of our earlier lab assignments...the target function operations are up to your creation. 

4\.  Not to mix thread output (i.e. print all of job _n_'s output prior to job _n + 1_'s output).  You will want to use synchronization methods available in the threading module. 

5\. Provide a screenshot of the result output of the threads.

Thread 1 job one: 5  
Thread 2 job two: 8 

**Deliverable:  **

*   **yournameLab9.py**  Your source code solution and a copy of the run pasted into your source submission file.  Be sure to comment out your run so that your **.py** file will still run in the grader test bed.

**Reminders:** 

*   Include a statement in your program header to let me know which lab you would like to replace.
*   There is no late submission window for this lab - all submissions due Tuesday, Dec. 4th 11:59 PM.
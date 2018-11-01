Assignment 1 - _Hello World!_ - Grade 18 out of 18
=============================

Even though this is an extremely easy assignment, I want everyone to do it.   Let's all just focus on making sure we have the compiler working, the indentation perfect and the tabs out.  This will ensure you get the most points in your first assignment, which may come in handy down the road.   Make sure you have read and understood

*   both **_m_**_**odules A**_ and _**B**_ this week, and
*   _**module 2R - Lab Homework Requirements**_

before submitting this assignment. Hand in only one program, please. 

#### _Hello World!_

Compile and run the **_"Hello World!"_** program from your first week's module. 

 Add three pieces of information to the output through either extra **cout** statements or a continuation of the existing **cout** statement:

*   Include your last (family) name.
*   Include your Foothill ID # (which is usually an eight digit number)
*   Note any two details   from page one of my _**Syllabus**_ and three details from the _**Lab Homework Requirements Page 2: Specific Requirements**_ (five details in all).  Don't copy/paste but paraphrase each detail **_in your own words._**

Here's an example:

#include <iostream>
using namespace std;

int main()
{
   cout << "Hello Foothill College Students!\\n\\n";
   cout << "My family name is Cecil" << endl;
   cout << "My student ID is 12345678" << endl << endl;
   cout << "  \[ your \]  "
       << "   \[ notes \]  "
       << "   \[ here\]  " << endl << endl;
   return 0;
}

/\* ---------------------- RUN -------------------------------------

Hello Foothill College Students!

My family name is Cecil
My student ID is 12345678

Syllabus detail #1: ...

Syllabus detail #2: ...

Specific lab detail #1: ...

Specific lab detail #2: ...

Specific lab detail #3: ...

Press any key to continue . . .

---------------------------------------------------------------------- \*/

You can use this as a template and enhance it somewhat to display the  information differently.  However, make sure the five items very clearly identifiable on the output.  Also, there is no point penalty if the output (run) wraps lines or  breaks words in the middle as it reaches the end of each line.  But try to fix that, anyway, by inserting _new line_ characters or using multiple **cout** statements to keep each line from getting too long.

Be careful about accepting the indentation that **Visual C++**, **Xcode** or any other compiler gives as you type long lines into your source **cout** statements.  The compiler may try to sneak _**tabs**_ in.  You know how to test to see whether that whitespace is a tab or three spaces, and you should restore any tabs to three spaces, manually as explained in the modules.

Because this is the first assignment, I will summarize some rules from your handout _**"Homework Requirements."**_  You are responsible for every rule in that module so make a habit of always checking your assignment against the rules it contains.  Here are some of them:

1.  Hand in only one file as an attachment.
2.  Hand in a plain text file, preferably a **.txt** file.  Examples of unacceptable formats are .rtf, .pdf, .pic, .zip, .doc or .jpg files.
3.  Include both the source and the run.
4.  Remove all tabs as described in the modules**.**
5.  Obey the style rules as described in the modules.
6.  Do not do computations in a screen output statement. Do not mix computation and output, ever (this will apply starting next week).
7.  Make sure the run "matches" your source.  If the  run you submit could not have come from the source you submit, it will be graded as if you did not hand in a run.

Sorry for all the rules, but there is a reason for each, and they are all very easy to follow.

Once your assignment is graded and returned, you can view the instructor solution here:

*   [Quiz List](/courses/7627/quizzes)

Your access code will be provided in your graded assignment comments.  Find the assignment in the list, click "Take Survey" and you will see the solution.  Even though it is called a "Quiz", it is actually just a solution; there is no need to submit anything, just open the quiz and see the solution.

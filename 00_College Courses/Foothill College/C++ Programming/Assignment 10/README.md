Assignment 10 - A StudentArrayUtilities Class with an Internal Array
====================================================================

_This extra credit assignment is worth 10 points.  Don't worry about the fact that it may say " .1 points possible." _

### Understand the Problem

Our previous **StudentArrayUtilities** (**SAU**) class consisted of a set of static class methods that acted on arrays of students.  We take this a step further.  Rather than having our client define and manage the array, let's give **SAU** the ability to do that.  There will be two main changes required:

*   **Adding and Removing Students** - We will provide methods **addStudent()** and **removeStudent()** as _**instance methods**_ in our **SAU** class.  Our clients can use these to add or remove individual students to an **SAU** object.  The client may not see where or how the students are stored, internally.  The extent to which we allow the client to gain access to the internal data is up to us, and in this assignment, we will give the client very limited access:  our implementation will behave a bit like a stack data structure, so that adding is like "pushing" and removing is like (but not exactly the same as) "popping".
*   **Earlier Methods Become Instance Methods** - Once we have the data **_internal_** to our **SAU** object, there is no need to pass arrays;  the data is already present as _**this**_ data.  So older methods, like **sort()** and **toString()**, are converted to **_instance methods_**, and their signatures are changed to reflect this fact.  When a sort is requested, the client only has to call **someUtilObj.sort()**, and it is understood that the **Students** to be sorted are the ones in the **_this_**  object's internal array created by the many previous calls to **addStudent()** and, perhaps, trimmed by some calls to **removeStudent**().

### StudentArrayUtilities Spec

#### Summary

The class will store its _**private data**_ as _**an array of Student**_ objects.   The natural -- and in a sense _universal_ -- solution to this arrangement is to have two private data members: one for the _**array**_, and a second for the **int** which holds us the number of actual students being stored in the array at any point in time:
``` cpp
   Student theArray\[ ... \];
   int numStudents;
```
**theArray** will be a fixed-size array, that size being the maximum number of **Students** we expect to ever manage.  It will hold many more elements than we need, typically.  **numStudents** would initially be **0** (during an object instantiation of this class), would grow as students are added via **addStudent()** and shrink as **Students** are removed via **removeStudent()**.  A common use for **numStudents**, besides telling us how many actual **Students** are in the object, is to tell any method that cares where the last (i.e., _highest_ in the array) **Student** is stored.  So, if **numStudents** is **12**, it means there are **12** **Students** in the array, even if the **theArray** happens to have, say, **1000 = MAX\_STUDENTS** positions of available capacity.   The active **Students** are stored in locations **0 - 11**, **theArray\[11\]** is the location of the **Student** in the highest occupied position, while **theArray\[12\]** is where the next **Student** would be added if and when a subsequent call was made to **addStudent()**.

The client may not need to know all this, but that's what's going on, internally.  

An **SAU** object is instantiated using a default constructor and, once created, will use the **addStudent()** mutator to build a **Student** roster for the object.  If the client wants to reduce the population of that object it would call **removeStudent()**.  Here is a typical instantiation followed by the addition of a couple **Student**s:
``` cpp
   StudentArrayUtilities myStuds;

   myStuds.addStudent( Student( "bartman", "petra", 102 ) );
   myStuds.addStudent( Student( "charters", "rodney", 295 ) );
``` 
As you see, there is no need for the client to create any arrays.  However, if the client happens to have an array of **Students**, it can use that array along with a loop to add many students efficiently, as in:
``` cpp
   for ( k = 0; k < arraySize; k++ )
      myStuds.addStudent( myClass\[k\] );
``` 
Once there are some **Student**s in the **SAU** object, we can display them with the help of the instance method **toString()**:
``` cpp
   cout << myStuds.toString( "Here are the students currently being stored: " );
``` 
This is a method similar to the **toString()** of our older **SAU** class, but now we see no array need be passed, since this is an instance method which carries the full data of the object wherever it goes (via the _**this**_ data).  Likewise, the sort is handled without a parameter:
``` cpp
    myStuds.arraySort();
``` 
That method call would result in our internal array being re-ordered.  As before, and without any modifications needed, that sort would be based on the underlying **Student** class's _**sort key**_.

Calling **toString()** after an **arraySort()** is invoked would naturally show the new order of the internal array.

Finally, the **removeStudent()** method would remove (from the internal array inside its **SAU** object) one of the **Student**s.  Which **Student**?  That's up to this spec and we could have many different answers.  The answer for _us_ (and for _you_) is that it will remove and return the student in the **_highest occupied array location_** of the internal array.  So a call to:
``` cpp
    student = myStuds.removeStudent();
``` 
Would remove the **Student** in location which is determined by the current value of the private member (but not necessarily that exact location -- this is something you will determine based on all the information just given.  It copies that removed object to the **Student** variable on the LHS for use by the client.

#### Static (Public) Members

*   A const int **MAX\_STUDENTS** which you can set to 20 for testing, but would be larger in general.  This is used to instantiate the internal array, whose capacity (physical array size) never changes from this one value.

#### Instance (Private) Members

*    **Student theArray\[MAX\_STUDENTS\]**  - our internal array whose size is always **MAX\_STUDENTS**, but whose actual data is stored in elements **0** through **numStudents - 1**.
*   ** int numStudents** - the current number of actual students stored in the array.  This can never be > **MAX\_STUDENTS**, and you have to make sure that it isn't.

#### Instance (Public) Methods

*   **bool addStudent( Student stud )** \- This method will place the passed-parameter into the next available location (highest) of our internal array.  It has to make sure not to overrun the internal array by breaching its capacity, **MAX\_STUDENTS**.
*   **Student removeStudent()** \- Removes and returns the Student in the highest occupied position in the array.  Note, depending on whether or not the internal array has been modified by a sort, this may -- but does not have to be -- the most recently added **Student**.  If there are no students in the array, it returns a _**default Student**_ -- i.e., create and return an _**anonymous**_ student using the _**default constructor**_ in the return line.  Therefore, the test for an error by the client is to compare the returned student with any default student (like an anonymously automatic **Student()**, as in  
      
     if ( Student::compareTwoStudents( retStud, Student() ) ) ...   
      
    However, this is not foolproof;  there might be a default student in the array.  We'll let this weakness slide for now and just accept it.  See the sample code which uses this technique, as can you.  
      
    The following methods are still here, but are now changed to instance methods.  The information that was supplied by their array parameters is now provided as part of the _**this**_ object in the form of **numStudents** (for the array size) and **theArray** (for the hitherto passed array).  You would now use those members in their definitions  
     
*   **string toString( string title )** \- This returns, usually for display by client, our the entire array in a single **string**, just like the static version did, but without the need for an array parameter.
*   **public void arraySort()** \- Just like the old static _**sort**_, but no need for an array parameter.   It works on the internal array.
*   **double getMedianDestructive()** - as above.

#### Helper (Private) Methods

*   **bool floatLargestToTop( int top )** - Same as our old version, but now an **_instance_** method.  Use this data in place of parameters lost from prior version.
*   **void mySwap(Student &a, Student &b)** \- Remains **static** and need not be changed.

#### Sample Client

Here is some client code to use while debugging.  You should be able to determine the correct run that results.  You should provide some code that is more complete than this in your testing.  For this test (and your own testing) set **MAX\_STUDENTS** to **20**.
``` cpp
int main()
{
   int k;
   Student  myClass\[\] = 
   {  
      Student("smith","fred", 95),  
      Student("bauer","jack",123),
      Student("jacobs","carrie", 195),  Student("renquist","abe",148),
      Student("3ackson","trevor", 108),  Student("perry","fred",225),
      Student("loceff","fred", 44),  Student("stollings","pamela",452),
      Student("charters","rodney", 295),  Student("cassar","john",321)
   };

   Student student;
   int arraySize = sizeof(myClass) / sizeof(myClass\[0\]);

   // instantiate an SAU object
   StudentArrayUtilities myStuds;

   // we can add stdunts manually and individually
   myStuds.addStudent( Student( "bartman", "petra", 102 ) );
   myStuds.addStudent( Student( "charters", "rodney", 295 ) );

   // if we happen to have an array available, we can add students in loop.
   for ( k = 0; k < arraySize; k++ )
      myStuds.addStudent( myClass\[k\] );

   cout << myStuds.toString( "Before: " );

   myStuds.arraySort();
   cout << myStuds.toString("After default sort: ");

   Student::setSortKey(Student::SORT\_BY\_FIRST);
   myStuds.arraySort();
   cout << myStuds.toString( "After sort by first: " );

   // test median
   cout << "Median of evenClass = "
      << myStuds.getMedianDestructive()
      << endl;

   // various tests of removing and adding too many students
   for (k = 0; k < 100; k++)
   {
      student = myStuds.removeStudent();
      if ( Student::compareTwoStudents( student, Student() ) )
         cout << "Removed " << student.toString();
      else
      {
         cout << "Empty after " << k << " removes." << endl;
         break;
      }
   }

   for (k = 0; k < 100; k++)
   {
      if (!myStuds.addStudent(Student("first", "last", 22)))
      {
         cout << "Full after " << k << " adds." << endl;
         break;
      }
   }
}
```
### _That's all.  See you at the Final Exam, and have a wonderful break, next quarter, and life._

Once your assignment is graded and returned, you can view the instructor solution here:

*   [Quiz List](/courses/7627/quizzes)

Your access code will be provided in your graded assignment comments.  Find the assignment in the list, click "Take Survey" and you will see the solution.  Even though it is called a "Quiz," it is actually just a solution; there is no need to submit anything, just open the quiz and see the solution.

_That's all.  See you at the Final Exam, and have a wonderful break, next quarter, and life._

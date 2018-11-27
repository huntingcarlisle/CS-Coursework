Assignment 9 - Changing Sort Keys
=================================

Make sure you have read and understood

*   both **_m_**_**odules A**_ and _**B**_ this week, and
*   _**module 2R - Lab Homework Requirements**_

before submitting this assignment. Hand in only one program, please. 

_While it may appear long at first, this lab is easier than it looks, so stay calm. It is easier because:_

1.  _i__t uses material and code that you learned, compiled and ran over a week ago when you studied **Module 8,** and_
2.  _b__elow, I give you very explicit directions on what to do for each of the very short methods you need to write._

_You will start with my existing **Student** and **StudentArrayUtilities** classes that you have already compiled and run when you read the modules. Then you will modify each of these classes as described below and provide a new test client._

### Understand the Application

#### Sort Flexibility (Student class)

In _**week 8**_, we saw an example of a **Student** class that provided a **compareTwoStudents()** method. We needed to define such a method because our _**sort algorithm**_ (which was in the **StudentArrayUtilities** (**SAU**) class) had to have a basis for comparing two **Student** objects, the foundation of **SAU**s sorting algorithm.  Since a **Student** is a compound data type, not a **double** or a **String**, there was no pre-defined **compareTo()** available, so we created our own **compareTwoStudents()**, which  was based on the spelling of the _**last name**_.  You can review those notes to see its definition.

We want to make the sort more flexible in this assignment.  Sometimes we want to sort on _**last name**_, as we did in the lectures, but other times we may choose to sort on the _**first name**_ (useful for informal communication) or _**total points**_ (useful for analyzing statistics).  We could go into the **compareTwoStudents()** method and change its definition to work on _**first name**_ or _**total points**_, but all that does is replace the inflexibility of _**last name**_ with the inflexibility of some other criteria.  So here's the  plan:  we will provide a static **Student** class method called **setSortKey()** which will establish a new sort criteria.  A client will invoke it whenever it wants to switch to a new basis for comparison.  The client will pass a parameter to **setSortKey()** telling it which one of the three **Student** fields it wants future sort algorithms to use.

#### Console Output (SAU class)

Another change we'll make affects the output modality.  Rather than using **JOptionPane**, we want to make the class "U.I. neutral." So we will replace **SAU**'s **toString()** method with a **toString()** method, and let the client choose how to use that.  In our example **main()** we will be sending the String array to the _**console**_, only.

#### Median (SAU class)

We'll add one more method to our **SAU** class: **double getMedianDestructive( Student\[\] someArray )**.  This method will return the _**median**_ of the **totalPoints** values in  an array.  Look up _**median**_.  It is defined as the "middle-value" and is easily computed, but you first have to sort the array in order to find it.  Fortunately, you already have the sort method.

#### Client

Our client will declare _four **Student** arrays_ to make sure our median works:  one array that had an odd number of students (_**15**_), one that has an even number of students (_**16**_), one that has a _**single student**_ and one that has _**no students**_ (we will define the median of an array with no elements to be 0.0).

We'll test the **sortKey** and sort algorithm only on the even numbered array, and then we will test our median computation on all four arrays.

### The Program Spec

These changes should not be complicated as long as you read carefully and follow directions. New and modified members/methods are all very short, so stay focused and apply what you learned back in _**week 8**_.

#### _Additions_ to the Student Class

We will add the following members to the class in the modules.

##### Public static int constants (finals):

*   **SORT\_BY\_FIRST** = 88
*   **SORT\_BY\_LAST** \= 98
*   **SORT\_BY\_POINTS** \= 108

These are the three _**sort keys**_ that will be used by the client and the class, alike, to keep track of, or set, the _**sort key**_.   If the client wants to establish a new _**sort key**_, it will pass one of these tokens (say **Student.SORT\_BY\_FIRST**) to the setter described next.    I have intentionally made the literal values non-contiguous so you would not rely on their particular values in your logic.   You should be able to change the values without breaking your program (but you don't have to change them;  use the three values above).

##### Private static int:

*   **sortKey** - this will always have one of the three constants above as its value. Make sure it initially has **SORT\_BY\_LAST** in it, but after the client changes it, it could be any of the above constants.

You should supply the following simple **_public static methods_**:

*   **boolean setSortKey( int key )** -- a _**mutator**_ for the member **sortKey**.
*   **int getSortKey()** -- an _**accessor**_ for **sortKey**.

#### _Modification_ to the Student Class

*   **compareTwoStudents( ... )** -- same signatures as in the modules, but now this method has to look at the **sortKey** and compare the two **Students** based on the currently active **sortKey**.  A **switch** statement with three different expressions is all you need, and each expression will be very similar to the one already in the modules (in fact one will be identical).  As you saw in the modules, it needs to return an **int**, which is _**positive**_, if the first student is **_greater_** than the second, _**negative**_ if _**less than**_, and _**zero**_ if they are the _**same**_, _based on the current value of **sortKey**, of course_.

#### _Change_ to the StudentArrayUtilities Class

*   **Replace toString() with toString().**  Generate the same kind of **String**, but instead of sending it to the screen, return it to the client.
*   Add a _**public**_ static method ****double getMedianDestructive(Student\[\] array, int arraySize******)** - This computes and returns the **_median_** of the total scores of all the students in the array  The details are simple, but you have to take them each carefully:
    *   Dispose of the cases of an empty array (0 elements) and one-element array.  Empty arrays return 0.0, always, and one-element array returns its one and only **Student**'s **totalPoints**.  (This second case can actually be skipped if you handle the next cases correctly, but it doesn't hurt to do it separately, here.)
    *   **Even-numbered arrays >= 2** elements:  find the two middle elements and return their average of their total points.
    *   **Odd-numbered arrays >= 3** elements:  return the total points of the exact middle element.
    *   **Special Note**:  This method has to do the following.  It must **_sort the array_** according to **totalPoints** in order to get the medians, and that's easy since we already have the sort method.  Then it has to find the middle-student's score (e.g., if the array is size **21**, the middle element is the score in **array\[10\]**, _after the sort_).  But, before doing the sort, it also has to change the **sortKey** of the **Student** class to **SORT\_BY\_POINTS**.  One detail, that you may not have thought of, is that, at the very start of the method, it needs to save the **_client's sort key_**.  Then, before returning, restore the client's sort key.  This method doesn't know what that sort key might be, but there is an accessor **getSortKey()** that will answer that question.
    *   This method has the word "**Destructive**" in its name to remind the client that it may (and usually will) modify the order of the array, since it is going to sort the array by _**total points**_ in the process of computing the _**median**_.  However, it will not destroy or modify the client's **sortKey** when the method returns to client (see previous bullet).

#### The Foothill main()

Our client will declare _four **Student** arrays_:  using direct initialization, as in the modules: no user input.  The array sizes should be 15, 16, 1 and 0.  The second array can be the same as the first with one extra **Student** tagged onto the end.  Each array should be initialized in no particular order:  unsorted in all fields.

Using the largest, even numbered, array:

1.  display the array immediately before calling a sort method,
2.  sort the array using the default (initial) _**sort key**_ and display,
3.  change the _**sort key**_ to _**first name**_, sort and display,
4.  change the _**sort key**_ to _**total score**_, sort and display,
5.  **setSortKey()** to _**first name**_, call the **getMedianDestructive()** method and display the **_median score_**. and finally
6.  call **getSortKey()** to make sure that the **getMedianDestructive()** method preserved the client's **sortKey** value of _**first name**_ that was just set prior to the **getMedianDestructive()** call.

Using each of the other three arrays:

*   get the median of each array and display.  No other testing needed in this part.

Here's a sample output, but you must not use my arrays.  Make your own as per the spec above.

Before: 
  smith, fred points: 95
  bauer, jack points: 123
  jacobs, carrie points: 195
  renquist, abe points: 148
  zz-error, trevor points: 108
  perry, fred points: 225
  loceff, fred points: 44
  stollings, pamela points: 452
  charters, rodney points: 295
  cassar, john points: 321

Sorting by default ---------------
After: 
  bauer, jack points: 123
  cassar, john points: 321
  charters, rodney points: 295
  jacobs, carrie points: 195
  loceff, fred points: 44
  perry, fred points: 225
  renquist, abe points: 148
  smith, fred points: 95
  stollings, pamela points: 452
  zz-error, trevor points: 108

Sorting by first name ---------------
After: 
  renquist, abe points: 148
  jacobs, carrie points: 195
  loceff, fred points: 44
  perry, fred points: 225
  smith, fred points: 95
  bauer, jack points: 123
  cassar, john points: 321
  stollings, pamela points: 452
  charters, rodney points: 295
  zz-error, trevor points: 108

Sorting by total points ---------------
After: 
  loceff, fred points: 44
  smith, fred points: 95
  zz-error, trevor points: 108
  bauer, jack points: 123
  renquist, abe points: 148
  jacobs, carrie points: 195
  perry, fred points: 225
  charters, rodney points: 295
  cassar, john points: 321
  stollings, pamela points: 452

Median of evenClass = 171.5
Successfully preserved sort key.
Median of oddClass = 148.0
Median of smallClass = 95.0
Median of noClass = 0.0

Once your assignment is graded and returned, you can view the instructor solution here:

*   [Quiz List](/courses/7627/quizzes)

Your access code will be provided in your graded assignment comments.  Find the assignment in the list, click "Take Survey" and you will see the solution.  Even though it is called a "Quiz," it is actually just a solution; there is no need to submit anything, just open the quiz and see the solution.
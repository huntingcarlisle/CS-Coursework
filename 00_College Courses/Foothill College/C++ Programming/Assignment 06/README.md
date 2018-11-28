Assignment 6 - A Triple String Class - Grade 18 out of 18
====================================

Make sure you have read and understood

*   both **_m_**_**odules A**_ and _**B**_ this week, and
*   _**module 2R - Lab Homework Requirements**_

#### A Simple Class: TripleString

### Understand the Application

The assignment is to first create a class called **TripleString**. **TripleString** will consist of three _**private member**_ **Strings** as its basic data. There will be a few _**instance methods**_ to support that data.

Once defined, we will use it to instantiate **TripleString** objects that can be used in our **main()** method. In a later assignment, the **TripleString** class will help us create a more involved application.

The three private member **strings** in the class are named **string1**, **string2**, and **string3**. We will also add a few public **static const** members such as final int **MAX\_LEN** and **MIN\_LEN** These represents the maximum and minimum length that our class will allow any of its **strings** to be set to. We can use these static members in the **TripleString** method whose job it is to test for valid strings (see below).

### The Program Spec

**Class TripleString Spec**

##### Private Class Instance Members:

*   **string string1**
*   **string string2**
*   **string string3**

All legal strings should be between 1 and 50 characters.

As stated in the modules, we never want to see a _**literal**_ in our _**methods**_.  So the class should have **static** members to hold values for the _**limits**_ described above as well as _**default values**_ for any _member_ whose **_object_** is _**construct-**_ed using illegal _**arguments**_ from the _**client**_.  These are put in the **public static** section.

##### Public Class Static Constants (declare to be _**const**_):

*   **MIN\_LEN** = 1

*   **MAX\_LEN** = 50

*   **DEFAULT\_STRING** = " (undefined) "


#### Public Instance Methods

##### Default Constructor

> **TripleString()** \-- a default constructor that initializes all members to **DEFAULT\_STRING**.

##### Paramteter-Taking Constructor

> **TripleString(string str1, string str2, string str3)** \-- a constructor that initializes all members according to the passed parameters.  It has to  to be sure each **string** satisfies the class requirement for a member **string**. It does this, as in the modules, by calling the _**mutators**_ and taking possible action if a **return** value is **false**. If any passed parameter does not pass the test, a _**default**_ **string** should be stored in that member.

##### Mutators/Accessor

> **set()**s and **get()**s for these members.  Mutators in our course are named using the convention as follows: **setString1( ... )**,  **setString3( ... )**, etc.  Likewise with accessors:  **getString2()**.  We need an accessor and mutator _for each individual string member,_ so there are three pairs of methods in this category.  Mutators make use of the private helper method **validString().** When a mutator detects an invalid **string**, no action should be taken.  The mutator returns **false**, and the existing **string** stored in that member prior to the call remains in that member, not a new default **string**.
>
> **string toString()** - a method that returns a **string** which contains all the information (three strings) of the **TripleString** object.  This **string** can be in any format as long as it is understandable and clearly formatted.

#### Private Static Helper Methods

> **bool validString( string str )** -- a helper function that the mutators can use to determine whether a **xtring** is legal. This method returns **true** if its **length is between MIN\_LEN and MAX\_LEN** (inclusive).  It returns **false**, otherwise.

##### Where it All Goes

There are now a variety of program elements, so let's review the order in which things appear in your .cpp file:

1.  includes and namespace
2.  class prototype(s)
3.  static member initialization
4.  global-scope method prototype(s)  \[You may not need them for this assignment.\]
5.  main() definition
6.  global-scope method definition( )  \[You may not need them for this assignment.\]
7.  class method definition(s)

In other words, **Foothill.cpp** will look like this:
``` cpp
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

class TripleString
{
   // prototype
};

// define static constants

// client ---------------------------------------------------------------------
int main()
{
   // main client "driver"
}

//  TripleString class methods
// constructors
TripleString::TripleString()
{
   // constructor defintion
}

TripleString::TripleString(string string1, string string2, string string3)
{
   // constructor definition
}

// mutators and other class definitions...
```
As you see, **TripleString** class methods are  defined _**after**_, not _within_, the **TripleString** class prototype.   Those methods are also defined after the **main()** method. 

### The Foothill main()

1.  _**Instantiate**_ four or more **TripleString** objects, some of them using the default constructor, some using the constructor that takes parameters.
2.  Immediately _**display**_ all objects.
3.  _**Mutate**_ one or more members of every object.
4.  _**Display**_ all objects a second time.
5.  Do two explicit _**mutator tests.**_ For each, call a _**mutator**_ in an **if/else** statement which prints one message if the call is successful and a different message if the call fails.
6.  Make two _**accessor calls**_ to demonstrate that they work.

#### More:

*   Be sure that all output is descriptive. Use labels to differentiate your output sections and full sentences in your mutator/accessor tests.
*   No user input should be done in this program.

I am not supplying a sample output this week -- the above description is adequate.

Once your assignment is graded and returned, you can view the instructor solution here:

*   [Quiz List](/courses/7627/quizzes)

Your access code will be provided in your graded assignment comments.  Find the assignment in the list, click "Take Survey" and you will see the solution.  Even though it is called a "Quiz," it is actually just a solution; there is no need to submit anything, just open the quiz and see the solution.

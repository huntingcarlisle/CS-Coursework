/*
Hunter Carlisle | Foothill College Fall 2018 | Lab Six

One instance of class TripleString represents a grouping of three strings
*/

#include <iostream>
#include <string>
#include <sstream>
using namespace std;

// CLASS PROTOTYPES ------------------------------------------------------------
class TripleString
{
private:
   // INSTANCE VARIABLES
   string string1;
   string string2;
   string string3;

   // HELPERS
   bool validString(string theString);

public:
   // STATIC CONSTANTS
   static const int MIN_LEN = 1;
   static const int MAX_LEN;
   static const string DEFAULT_STRING;

   // CONSTRUCTORS
   TripleString();
   TripleString(string string1, string string2, string string3);

   // MUTATORS/ACCESSORS
   bool setString1(string string1);
   bool setString2(string string2);
   bool setString3(string string3);
   string getString1();
   string getString2();
   string getString3();
   string toString();
};

// STATIC CONSTANTS
//const int TripleString::MIN_LEN = 1;
const int TripleString::MAX_LEN = 50;
const string TripleString::DEFAULT_STRING = " (undefined) ";

// CLIENT ----------------------------------------------------------------------
int main()
{
   // Instantiate four or more TripleString objects
   cout << "Instantiating 4 TripleString objects...";
   TripleString object1, object2;
   TripleString object3("This", "is", "fun");
   TripleString object4("Invalid", "is", "invalidforsomanyreasonswhywouldyou"
                                          "enterastringthislongyoumaniac"
                                          "youknowwhatI'mnotevengoingtotry");
   cout << "DONE" << endl << endl;

    // Immediately display all objects
   cout << "Displaying 4 TripleString objects:" << endl;
   cout << object1.toString() << endl;
   cout << object2.toString() << endl;
   cout << object3.toString() << endl;
   cout << object4.toString() << endl << endl;

   // Mutate one or more members of every object
   cout << "Mutating 4 TripleString objects...";
   object1.setString1("We're not in undefined anymore.");
   object2.setString2("I'm a real string!");
   object3.setString3("better than fun");
   object4.setString3("not a great position to be in.");
   cout << "DONE" << endl << endl;

   // Display all objects a second time
   cout << "Displaying 4 mutated TripleString objects:" << endl;
   cout << object1.toString() << endl;
   cout << object2.toString() << endl;
   cout << object3.toString() << endl;
   cout << object4.toString() << endl << endl;

   // Do two explicit mutator tests
   cout << "Explicitly attempting to mutate 2 TripleString objects..." << endl;
   if(object1.setString1("Frankenstein")){  // valid string
      cout << "it's alive!" << endl;
   }  else {
      cout << "well, that was a huge waste of electricity." << endl;
   }
   if(object2.setString2("")){  // invalid string
      cout << "These are not the droids you are looking for." << endl;
   }  else {
      cout << "I find your lack of faith disturbing." << endl;
   }
   cout << "DONE" << endl << endl;

   // Make two accessor calls to demonstrate that they work
   cout << "Calling accessor methods on 2 TripleString objects:" << endl;
   cout << object1.getString1() << endl;
   cout << object2.getString2() << endl;
}

// CLASS METHODS ---------------------------------------------------------------
// CONSTRUCTORS
TripleString::TripleString()
{
    // constructor definition
    setString1(DEFAULT_STRING);
    setString2(DEFAULT_STRING);
    setString3(DEFAULT_STRING);
}

TripleString::TripleString(string theString1,
      string theString2, string theString3)
{
    // constructor definition
   if(!setString1(theString1))
      this->string1 = DEFAULT_STRING;
   if(!setString2(theString2))
      this->string2 = DEFAULT_STRING;
   if(!setString3(theString3))
      this->string3 = DEFAULT_STRING;
}

// HELPERS
bool TripleString::validString(string theString)
{
   return (theString.length() >= MIN_LEN && theString.length() <= MAX_LEN);
}

// MUTATORS
bool TripleString::setString1(string theString)
{
   if(validString(theString)) {
      string1 = theString;
      return true;
   } else {
      return false;
   }
}

bool TripleString::setString2(string theString)
{
   if(validString(theString)) {
      string2 = theString;
      return true;
   } else {
      return false;
   }
}

bool TripleString::setString3(string theString)
{
   if(validString(theString)) {
      string3 = theString;
      return true;
   } else {
      return false;
   }
}

// ACCESSORS
string TripleString::getString1()
{
   return string1;
}

string TripleString::getString2()
{
   return string2;
}

string TripleString::getString3()
{
   return string3;
}

string TripleString::toString()
{
   return getString1() + " | " + getString2() + " | " + getString3();
}


/* --------- PROGRAM RUN -------------------------------------------------------
Instantiating 4 TripleString objects...DONE

Displaying 4 TripleString objects:
 (undefined)  |  (undefined)  |  (undefined)
 (undefined)  |  (undefined)  |  (undefined)
This | is | fun
Invalid | is |  (undefined)

Mutating 4 TripleString objects...DONE

Displaying 4 mutated TripleString objects:
We're not in undefined anymore. |  (undefined)  |  (undefined)
 (undefined)  | I'm a real string! |  (undefined)
This | is | better than fun
Invalid | is | not a great position to be in.

Explicitly attempting to mutate 2 TripleString objects...
it's alive!
I find your lack of faith disturbing.
DONE

Calling accessor methods on 2 TripleString objects:
Frankenstein
I'm a real string!

Process finished with exit code 0

------------------------------------------------------------------------------*/
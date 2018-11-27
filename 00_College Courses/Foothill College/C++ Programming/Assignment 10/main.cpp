#include <string>
#include <iostream>
#include <sstream>
using namespace std;

// CLASS STUDENT PROTOTYPES ----------------------------------------------------
class Student
{
public:
   static const string DEFAULT_NAME;
   static const int DEFAULT_POINTS = 0;
   static const int MAX_POINTS = 1000;
   static const int SORT_BY_FIRST = 88;
   static const int SORT_BY_LAST = 98;
   static const int SORT_BY_POINTS = 108;

private:
   string firstName;
   string lastName;
   int totalPoints;
   static int sortKey;

public:
   Student();
   Student(string first, string last, int points);

   // ACCESSORS AND MUTATORS
   string getFirstName() { return firstName; }
   string getLastName() { return lastName; }
   int getPoints() { return totalPoints; }
   bool setFirstName(string first);
   bool setLastName(string last);
   bool setPoints(int pts);
   static bool setSortKey(int key);
   static int getSortKey() {return sortKey;}

   static int compareTwoStudents( Student firstStud, Student secondStud );
   string toString();

private:
   static bool validString( string testStr );
   static bool validPoints( int testPoints );
};

// CLASS STUDENT_ARRAY_UTILITIES PROTOTYPES ------------------------------------
class StudentArrayUtilities
{
public:
   static const int MAX_STUDENTS = 20;

private:
   Student theArray[MAX_STUDENTS];
   int numStudents;

public:
   StudentArrayUtilities();
   string toString(string title);
   void arraySort();
   double getMedianDestructive();
   bool addStudent(Student stud);
   Student removeStudent();
   int arraySearch( string keyLast);


private:
   bool floatLargestToTop(int top);
   static void mySwap(Student &a, Student &b);
};

// STATIC CONSTANTS ------------------------------------------------------------
const string Student::DEFAULT_NAME = "zz-error";
int Student::sortKey = SORT_BY_LAST;

// MAIN DEFINITION -------------------------------------------------------------
int main()
{
   int k;
   Student  myClass[] =
         {
               Student("smith","fred", 95),
               Student("bauer","jack",123),
               Student("jacobs","carrie", 195),  Student("renquist","abe",148),
               Student("3ackson","trevor", 108),  Student("perry","fred",225),
               Student("loceff","fred", 44),  Student("stollings","pamela",452),
               Student("charters","rodney", 295),  Student("cassar","john",321)
         };

   Student student;
   int arraySize = sizeof(myClass) / sizeof(myClass[0]);

   // instantiate an SAU object
   StudentArrayUtilities myStuds;

   // we can add stdunts manually and individually
   myStuds.addStudent( Student( "bartman", "petra", 102 ) );
   myStuds.addStudent( Student( "charters", "rodney", 295 ) );

   // if we happen to have an array available, we can add students in loop.
   for ( k = 0; k < arraySize; k++ )
      myStuds.addStudent( myClass[k] );

   cout << myStuds.toString( "Before: " );

   myStuds.arraySort();
   cout << myStuds.toString("After default sort: ");

   Student::setSortKey(Student::SORT_BY_FIRST);
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
      if (!myStuds.addStudent(Student("last", "first", 22)))
      {
         cout << "Full after " << k << " adds." << endl;
         break;
      }
   }
}

// STUDENT CLASS METHODS -------------------------------------------------------
// CONSTRUCTORS
Student::Student()
{
   firstName = DEFAULT_NAME;
   lastName = DEFAULT_NAME;
   totalPoints = DEFAULT_POINTS;
}

Student::Student( string last, string first, int points)
{
   if ( !setFirstName(first) )
      firstName = DEFAULT_NAME;
   if ( !setLastName(last) )
      lastName = DEFAULT_NAME;
   if ( !setPoints(points) )
      totalPoints = DEFAULT_POINTS;
}

// MUTATORS
bool Student::setFirstName(string first)
{
   if ( !validString(first) )
      return false;
   firstName = first;
   return true;
}

bool Student::setLastName(string last)
{
   if ( !validString(last) )
      return false;
   lastName = last;
   return true;
}

bool Student::setPoints(int pts)
{
   if ( !validPoints(pts) )
      return false;
   totalPoints = pts;
   return true;
}

bool Student::setSortKey(int key) {
   if (!(key == SORT_BY_FIRST || key == SORT_BY_LAST || key == SORT_BY_POINTS))
      return false;
   sortKey = key;
   return true;
}

// HELPERS
// returns comparison result of two Student objects based on sort key
int Student::compareTwoStudents( Student firstStud, Student secondStud )
{
   int result;
   if (sortKey == SORT_BY_FIRST)
   {
      result = firstStud.firstName.compare(secondStud.firstName);
   }
   else if (sortKey == SORT_BY_LAST)
   {
      result = firstStud.lastName.compare(secondStud.lastName);
   }
   else if (sortKey == SORT_BY_POINTS)
   {
      result = firstStud.totalPoints > secondStud.totalPoints;
   }
   return result;
}

// returns string representation of Student object
string Student::toString()
{
   string resultString;
   ostringstream cnvrtFirst, cnvrtLast, cnvrtPoints;

   cnvrtFirst << firstName;
   cnvrtLast << lastName;
   cnvrtPoints << totalPoints;

   resultString = " " + cnvrtLast.str() + ", " + cnvrtFirst.str()
                  + " points: " + cnvrtPoints.str()
                  + "\n";
   return resultString;
}

// returns true if string is a valid value
bool Student::validString( string testStr )
{
   if (testStr.length() > 0 && isalpha(testStr[0]))
      return true;
   return false;
}

// returns true if points is a valid value
bool Student::validPoints( int testPoints )
{
   if (testPoints >= 0 && testPoints <= MAX_POINTS)
      return true;
   return false;
}

// STUDENT_ARRAY_UTILITIES CLASS METHODS ---------------------------------------
// CONSTRUCTOR
StudentArrayUtilities::StudentArrayUtilities()
{
   numStudents = 0;
   for (int k = 0; k < MAX_STUDENTS ; k++)
   {
      theArray[k].setLastName("");
      theArray[k].setFirstName("");
      theArray[k].setPoints(0);
   }
}

// HELPERS
// returns a string representation of the Student array information
string StudentArrayUtilities::toString(string title)
{
   string output = title + "\n";

   for (int k = 0; k < numStudents; k++)
      output += " " + theArray[k].toString();

   return output;
}

// sorts the array in ascending order
void StudentArrayUtilities::arraySort()
{
   for (int k = 0; k < numStudents; k++)
      // compare with method def to see where inner loop stops
      if (!floatLargestToTop(numStudents - 1 - k))
         return;
}

// returns true if largest value in array is sorted to end of array
bool StudentArrayUtilities::floatLargestToTop( int top )
{
   bool changed = false;

   // compare with client call to see where the loop stops
   for (int k = 0; k < top; k++)
      if ( Student::compareTwoStudents(theArray[k], theArray[k + 1]) > 0 )
      {
         mySwap(theArray[k], theArray[k + 1]);
         changed = true;
      }
   return changed;
}

// swaps variable names for two student objects
void StudentArrayUtilities::mySwap(Student &a, Student &b)
{
   Student temp("", "", 0);

   temp = a;
   a = b;
   b = temp;
}

// returns index of matching Student object
int StudentArrayUtilities::arraySearch(string keyLast)
{
   for (int k = 0; k < numStudents; k++)
      if (theArray[k].getLastName() == keyLast )
         return k;  // found match, return index

   return -1;   // fell through - no match
}

// returns the median of the total scores of all Student objects in the array
double StudentArrayUtilities::getMedianDestructive()
{
   double medianPoints;
   int clientSortKey = Student::getSortKey();

   Student::setSortKey(Student::SORT_BY_POINTS);
   this->arraySort();

   if (numStudents == 0)
      medianPoints = 0.0;
   else if (numStudents % 2 != 0)
   {
      int medianIndex = ((numStudents+1)/2)-1;
      medianPoints = theArray[medianIndex].getPoints();
   }
   else
   {
      int higherIndex = numStudents / 2;
      int lowerIndex = higherIndex - 1;
      medianPoints = (theArray[lowerIndex].getPoints() +
                      theArray[higherIndex].getPoints()) / 2.0;
   }

   Student::setSortKey(clientSortKey);
   return medianPoints;
}

// returns true if Student object added to array
bool StudentArrayUtilities::addStudent( Student stud )
{
   if(numStudents == MAX_STUDENTS)
      return false;
   theArray[numStudents].setFirstName(stud.getFirstName());
   theArray[numStudents].setLastName(stud.getLastName());
   theArray[numStudents].setPoints(stud.getPoints());
   numStudents++;
   return true;
}

// removes and returns last Student object in array
Student StudentArrayUtilities::removeStudent()
{
   Student student;
   if(numStudents == 0)
      student = Student();
   else
   {
      student = theArray[numStudents - 1];
      theArray[numStudents - 1].~Student();
      numStudents--;
   }
   return student;
}


/* PROGRAM RUN -----------------------------------------------------------------
Before:
  bartman, petra points: 102
  charters, rodney points: 295
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
After default sort:
  bartman, petra points: 102
  bauer, jack points: 123
  cassar, john points: 321
  charters, rodney points: 295
  charters, rodney points: 295
  jacobs, carrie points: 195
  loceff, fred points: 44
  perry, fred points: 225
  renquist, abe points: 148
  smith, fred points: 95
  stollings, pamela points: 452
  zz-error, trevor points: 108
After sort by first:
  renquist, abe points: 148
  jacobs, carrie points: 195
  loceff, fred points: 44
  perry, fred points: 225
  smith, fred points: 95
  bauer, jack points: 123
  cassar, john points: 321
  stollings, pamela points: 452
  bartman, petra points: 102
  charters, rodney points: 295
  charters, rodney points: 295
  zz-error, trevor points: 108
Median of evenClass = 171.5
Removed  stollings, pamela points: 452
Removed  cassar, john points: 321
Removed  charters, rodney points: 295
Removed  charters, rodney points: 295
Removed  perry, fred points: 225
Removed  jacobs, carrie points: 195
Removed  renquist, abe points: 148
Removed  bauer, jack points: 123
Removed  zz-error, trevor points: 108
Removed  bartman, petra points: 102
Removed  smith, fred points: 95
Removed  loceff, fred points: 44
Empty after 12 removes.
Full after 20 adds.

Process finished with exit code 0
 ---------------------------------------------------------------------------- */
#include <string>
#include <iostream>
#include <sstream>
#include <array>
#include <iomanip>
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
   Student( string first, string last, int points);

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
   static string toString(string title, Student *data, int arraySize);
   static void arraySort(Student array[], int arraySize);
   static int arraySearch( Student array[], string keyLast, int arraySize );
   static int binarySearch(Student array[], string keyLast,
                           int firstIndex, int lastIndex);
   static double getMedianDestructive(Student array[], int arraySize);

private:
   static bool floatLargestToTop(Student data[], int top);
   static void mySwap(Student &a, Student &b);
};

// STATIC CONSTANTS ------------------------------------------------------------
const string Student::DEFAULT_NAME = "zz-error";
int Student::sortKey = SORT_BY_LAST;

// MAIN DEFINITION -------------------------------------------------------------
int main() {
   // Instantiates and tests Student/StudentArray objects per program spec
   Student evenClass[] = {
         Student("abe", "lincoln", 999), Student("donald", "trump", 14),
         Student("barack", "obama", 523), Student("james", "polk", 576),
         Student("theodore", "roosevelt", 678),
         Student("franklin", "roosevelt", 144),
         Student("james", "buchanan", 23), Student("william", "taft", 423),
         Student("john", "adams", 883), Student("ulysses", "grant", 345),
         Student("bill", "clinton", 15), Student("george", "bush", 542),
         Student("george", "washington", 911),
         Student("thomas", "jefferson", 899),
         Student("gerald", "ford", 333), Student("albert", "gore", 756)
   };
   Student oddClass[] = {
         Student("abe", "lincoln", 999), Student("donald", "trump", 14),
         Student("barack", "obama", 523), Student("james", "polk", 576),
         Student("theodore", "roosevelt", 678),
         Student("franklin", "roosevelt", 14),
         Student("james", "buchanan", 23), Student("william", "taft", 423),
         Student("john", "adams", 883), Student("ulysses", "grant", 345),
         Student("bill", "clinton", 15), Student("george", "bush", 542),
         Student("george", "washington", 911),
         Student("thomas", "jefferson", 899),
         Student("gerald", "ford", 333)
   };
   Student smallClass[] = {Student("hunter", "carlisle", 555)};
   Student* noClass = new Student[0]();

   int evenClassSize = sizeof(evenClass) / sizeof(evenClass[0]);
   int oddClassSize = sizeof(oddClass) / sizeof(oddClass[0]);
   int smallClassSize = sizeof(smallClass) / sizeof(smallClass[0]);
   int noClassSize = sizeof(noClass) / sizeof(noClass[0]);;

   cout << StudentArrayUtilities::toString("Before: ", evenClass,
                                           evenClassSize) << endl;

   StudentArrayUtilities::arraySort(evenClass, evenClassSize);
   cout << StudentArrayUtilities::toString(
         "Sorting by default ---------------\n"
         "After: ", evenClass, evenClassSize) << endl;

   Student::setSortKey(Student::SORT_BY_FIRST);

   StudentArrayUtilities::arraySort(evenClass, evenClassSize);
   cout << StudentArrayUtilities::toString(
         "Sorting by first name ---------------\n"
         "After: ", evenClass, evenClassSize) << endl;

   Student::setSortKey(Student::SORT_BY_POINTS);

   StudentArrayUtilities::arraySort(evenClass, evenClassSize);
   cout << StudentArrayUtilities::toString(
         "Sorting by total points ---------------\n"
         "After: ", evenClass, evenClassSize) << endl;

   std::cout << setprecision(1) << fixed;
   Student::setSortKey(Student::SORT_BY_FIRST);
   cout << "Median of evenClass = "
        << StudentArrayUtilities::getMedianDestructive(evenClass,
                                                       evenClassSize)
        << endl;
   if (Student::getSortKey() == Student::SORT_BY_FIRST) {
      cout << "Successfully preserved sort key." << endl;
   }

   cout << "Median of oddClass = "
        << StudentArrayUtilities::getMedianDestructive(oddClass,
                                                       oddClassSize)
        << endl;
   cout << "Median of smallClass = "
        << StudentArrayUtilities::getMedianDestructive(smallClass,
              smallClassSize)
        << endl;
   cout << "Median of noClass = "
        << StudentArrayUtilities::getMedianDestructive(noClass,
                                                       noClassSize) << endl;
}

// STUDENT CLASS METHODS -------------------------------------------------------
// CONSTRUCTORS
Student::Student()
{
   firstName = DEFAULT_NAME;
   lastName = DEFAULT_NAME;
   totalPoints = DEFAULT_POINTS;
}

Student::Student( string first, string last, int points)
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

bool Student::setSortKey(int key)
{
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

// returns a string representation of the Student array information
string StudentArrayUtilities::toString(string title,
      Student *data, int arraySize)
{
    string output = title + "\n";

    for (int k = 0; k < arraySize; k++)
        output += " " + data[k].toString();

    return output;
}

// sorts the array in ascending order
void StudentArrayUtilities::arraySort(Student array[], int arraySize)
{
    for (int k = 0; k < arraySize; k++)
        // compare with method def to see where inner loop stops
        if (!floatLargestToTop(array, arraySize - 1 - k))
            return;
}

// returns true if largest value in array is sorted to end of array
bool StudentArrayUtilities::floatLargestToTop(Student data[], int top)
{
    bool changed = false;

    // compare with client call to see where the loop stops
    for (int k =0; k < top; k++)
        if (  Student::compareTwoStudents(data[k], data[k + 1]) > 0 )
        {
            mySwap(data[k], data[k + 1]);
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
int StudentArrayUtilities::arraySearch(Student array[], string keyLast,
                                       int arraySize)
{
    for (int k = 0; k < arraySize; k++)
        if ( array[k].getLastName() == keyLast )
            return k;  // found match, return index

    return -1;   // fell through - no match
}

// returns last name of matching Student object
int StudentArrayUtilities::binarySearch(Student array[], string keyLast,
                                        int firstIndex, int lastIndex)
{
    int middleIndex, result;

    if (firstIndex > lastIndex)
        return -1;
    middleIndex = (firstIndex + lastIndex) / 2;
    result = keyLast.compare( array[middleIndex].getLastName() );

    if (result == 0)
        return middleIndex;   //found him!
    else if (result < 0)
        return binarySearch( array, keyLast, firstIndex, middleIndex-1);
    else
        return binarySearch( array, keyLast, middleIndex+1, lastIndex);
}

// returns the median of the total scores of all Student objects in the array
double StudentArrayUtilities::getMedianDestructive(Student array[],
      int arraySize)
{
    double medianPoints;
    int clientSortKey = Student::getSortKey();

    Student::setSortKey(Student::SORT_BY_POINTS);
    arraySort(array, arraySize);

    if (arraySize == 0)
       medianPoints = 0.0;
    else if (arraySize % 2 != 0)
    {
        int medianIndex = ((arraySize+1)/2)-1;
        medianPoints = array[medianIndex].getPoints();
    }
    else
    {
       int higherIndex = arraySize / 2;
       int lowerIndex = higherIndex - 1;
       medianPoints = (array[lowerIndex].getPoints() +
              array[higherIndex].getPoints()) / 2.0;
    }

    Student::setSortKey(clientSortKey);
    return medianPoints;
}


/* PROGRAM RUN -----------------------------------------------------------------
Before:
  abe lincoln points: 999
  donald trump points: 14
  barack obama points: 523
  james polk points: 576
  theodore roosevelt points: 678
  franklin roosevelt points: 144
  james buchanan points: 23
  william taft points: 423
  john adams points: 883
  ulysses grant points: 345
  bill clinton points: 15
  george bush points: 543
  george washington points: 911
  thomas jefferson points: 899
  gerald ford points: 333
  albert gore points: 756

Sorting by default ---------------
After:
  john adams points: 883
  james buchanan points: 23
  george bush points: 543
  bill clinton points: 15
  gerald ford points: 333
  albert gore points: 756
  ulysses grant points: 345
  thomas jefferson points: 899
  abe lincoln points: 999
  barack obama points: 523
  james polk points: 576
  theodore roosevelt points: 678
  franklin roosevelt points: 144
  william taft points: 423
  donald trump points: 14
  george washington points: 911

Sorting by first name ---------------
After:
  abe lincoln points: 999
  albert gore points: 756
  barack obama points: 523
  bill clinton points: 15
  donald trump points: 14
  franklin roosevelt points: 144
  george bush points: 543
  george washington points: 911
  gerald ford points: 333
  james buchanan points: 23
  james polk points: 576
  john adams points: 883
  theodore roosevelt points: 678
  thomas jefferson points: 899
  ulysses grant points: 345
  william taft points: 423

Sorting by total points ---------------
After:
  donald trump points: 14
  bill clinton points: 15
  james buchanan points: 23
  franklin roosevelt points: 144
  gerald ford points: 333
  ulysses grant points: 345
  william taft points: 423
  barack obama points: 523
  george bush points: 543
  james polk points: 576
  theodore roosevelt points: 678
  albert gore points: 756
  john adams points: 883
  thomas jefferson points: 899
  george washington points: 911
  abe lincoln points: 999

Median of evenClass = 794.5
Successfully preserved sort key.
Median of oddClass = 523.0
Median of smallClass = 555.0
Median of noClass = 0.0

Process finished with exit code 0
----------------------------------------------------------------------------- */
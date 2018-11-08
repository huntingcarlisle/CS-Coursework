/*
Hunter Carlisle | Foothill College Fall 2018 | Lab Two

This program takes user input and prints various expressions to console.
Inputs: User Last Name and Student ID
Print Output: Expressions per Assignment Spec
*/

#include <iostream>
using namespace std;

int main()
{
    // Initialize and Store Variables
    int numLet = 8;
    int myId = 20343101;
    int intResult;
    double doubleResult;

    // Evaluate and Print Expressions
    cout << "My family name is Carlisle" << endl;
    cout << "My student ID is 20343101" << endl;
    cout << "The number of characters in my last name is " << numLet << endl;
    cout << endl;
    intResult = myId % 17;
    cout << "Expression #1 ------------ : " << intResult << endl;
    intResult = (myId + 4) % 9;
    cout << "Expression #2 ------------ :: " << intResult << endl;
    doubleResult  = myId / (myId + 500.0);
    cout << "Expression #3 ------------ : " << doubleResult << endl;
    intResult = 1 + 2 + 3 + 4 + 5 + 6 + 7 + numLet;
    cout << "Expression #4 ------------ : " << intResult << endl;
    doubleResult  = 15000.0 / (80.0 + (double(myId - 123456) /
                                       ((numLet + 20) * (numLet + 20))));
    cout << "Expression #5 ------------ : " << doubleResult << endl;
    return 0;
}

/* --------- RUN ---------------------------------------
"C:\Users\hunterc\Dropbox\Code\CS-Coursework\Foothill College\C++ Programming\Assignment 2\cmake-build-debug\Assignment_2.exe"
My family name is Carlisle
My student ID is 20343101
The number of characters in my last name is 8

Expression #1 ------------ : 0
Expression #2 ------------ :: 0
Expression #3 ------------ : 0.999975
Expression #4 ------------ : 36
Expression #5 ------------ : 0.579814

Process finished with exit code 0
---------------------------------------------------------*/

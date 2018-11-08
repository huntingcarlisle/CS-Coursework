/*
Hunter Carlisle | Foothill College Fall 2018 | Lab Five

This program performs various text processing functions.
*/

#include <iostream>
#include <string>
#include <stdio.h>
#include <ctype.h>

using namespace std;


// Main Program
int main()
{
    // this case handles ages 10, 11, 12, 13, 14 and 15
    char ans = 'y';
    int errors = 6;
    int numTries = 5;
    int count = 1;
    if ( (ans == 'Y' && errors < 5)  ||  numTries < 10 )  // note uppercase 'Y'
        count++;
    cout << count++;
};


/* --------- RUN 1 ---------------------------------------

Please enter a SINGLE character to act as key:error
 error
Please enter a SINGLE character to act as key:123
 123
Please enter a SINGLE character to act as key:h
 h
Please enter a phrase or sentence >= 6:happy
 happy
Please enter a phrase or sentence >= 6:You didn't like my input?! What was wrong with that! Harrumph!
 You didn't like my input?! What was wrong with that! Harrumph!

String with key character, 'h' masked:
You didn't like my input?! W*at was wrong wit* t*at! Harrump*!

String with key character, 'h' removed:
You didn't like my input?! Wat was wrong wit tat! Harrump!

Number of occurrences of key character, 'h': 4

Process finished with exit code 0

---------------------------------------------------------*/


/* --------- RUN 2 ---------------------------------------
Please enter a SINGLE character to act as key:a
 a
Please enter a phrase or sentence >= 6: This is a test of your emergency broadcast system. DO NOT BE ALARMED. All is as it should be.
 This is a test of your emergency broadcast system. DO NOT BE ALARMED. All is as it should be.

String with key character, 'a' masked:
This is * test of your emergency bro*dc*st system. DO NOT BE ALARMED. All is *s it should be.

String with key character, 'a' removed:
This is  test of your emergency brodcst system. DO NOT BE ALARMED. All is s it should be.

Number of occurrences of key character, 'a': 4

Process finished with exit code 0

---------------------------------------------------------*/

/* --------- RUN 3 ---------------------------------------
Please enter a SINGLE character to act as key:z
 z
Please enter a phrase or sentence >= 6: Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair. Fuzzy Wuzzy wasn’t fuzzy, was he?
 Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair. Fuzzy Wuzzy wasn’t fuzzy, was he?

String with key character, 'z' masked:
Fu**y Wu**y was a bear. Fu**y Wu**y had no hair. Fu**y Wu**y wasn't fu**y, was he?

String with key character, 'z' removed:
Fuy Wuy was a bear. Fuy Wuy had no hair. Fuy Wuy wasn't fuy, was he?

Number of occurrences of key character, 'z': 14

Process finished with exit code 0

---------------------------------------------------------*/

/* --------- RUN 4 ---------------------------------------

Please enter a SINGLE character to act as key:t
 t
Please enter a phrase or sentence >= 6:There those thousand thinkers were thinking how did the other three thieves go through.
 There those thousand thinkers were thinking how did the other three thieves go through.

String with key character, 't' masked:
There *hose *housand *hinkers were *hinking how did *he o*her *hree *hieves go *hrough.

String with key character, 't' removed:
There hose housand hinkers were hinking how did he oher hree hieves go hrough.

Number of occurrences of key character, 't': 9

Process finished with exit code 0
---------------------------------------------------------*/
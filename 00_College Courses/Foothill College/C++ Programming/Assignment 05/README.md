Assignment 5 - Text Processing
==============================

Make sure you have read and understood

*   both **_m_**_**odules A**_ and _**B**_ this week, and
*   _**module 2R - Lab Homework Requirements**_

before submitting this assignment. Hand in only one program, please. 

#### Detecting a Key Character in a String

### Understand the Application

We would like to demonstrate our ability to control strings and use methods. 

There are times when a program has to search for and replace certain characters in a string with other characters.  This program will look for an individual character, called the **_key character_**, inside a _**target string**_.   It will then perform various functions such as replacing the key character with an asterisk (\*) wherever it occurs in the target string.  For example, if the key character were

'a'

 and the string were

"He who laughs last, laughs fast, faster, FASTEST."

then the operation of replacing the 'a' by an asterisk would result in the new string:

 "He who l\*ughs l\*st, l\*ughs f\*st, f\*ster, FASTEST."

As you can see, only the lower-case 'a' was detected and replaced.  _This is called "**case-sensitivity**" and this entire program spec is **case-sensitive**._

This was only one possible task we might perform.  Another would be to **_remove_** all instances of the key character rather than _**replace**_ each with an asterisk.  Yet a third might be to _**count**_ the number of key characters.  We are going to do it all.  
  
**Modifying vs. Rebuilding**  
  
Whenever we deal with strings, we have to decide whether we are going to modify an existing string or create a second string which has the desired changes.  We will not attempt to touch the original string in our operations.  Instead, we will declare a new string object and build that up in stages, replacing or removing the desired characters of the original string by simply taking action on the new string we are building.  When I say we "build" a string, I mean that we initialize the string to be empty, "", and then use _**concatenation**_ to replace it with ever-longer versions of itself.  This technique has some advantages that allow it to be used for a variety of purposes, so it's good to learn now.

For example, consider this statement, which appends an exclamation point to the end of a string, **myStr**:

   myStr = myStr + "!";

This statement uses the old value of **myStr** on the RHS, then completely throws away the old value on the LHS and replaces it with the new, longer, **string**.  This is similar to a more familiar kind of numeric statement:

   n = n + 3;

where we replace the old contents of **n** with new contents.

**The Methods**

We will be writing methods.  Some will get input from the user (which take no parameters) and others will take arguments:  the **string** and/or _**key character**_.  Depending on the method we write, it will return one of the following types: a **string**, a **char** or an **int**.   For example, one of the methods we write will take the _**key character**_ and the _**target string**_ as parameters and will return a new **string** which has all the occurrences of the key character replaced by asterisks.  Its signature would look like this:

    string maskCharacter(string theString, char keyCharacter)

We will be careful at all stages:  input methods will only deal with user input, and not attempt to do computation.  Computations will not do any input or output.

The exception is always **main()**.  In **main()** we may do input and output directly if we are not required to use a method to do so by the spec.  In our spec, this week, we will use input methods to get the input (not **main()**), but we will allow **main()** to do the output directly.

### The Program Spec

Ask the user to enter both a _**key character**_ and a _**target string**_ (phrase, sentence, etc.).  Then, show the user three things::

1.  The target string with the key character replaced by asterisks.
2.  The target string with the key character removed.
3.  The number of occurrences of the key character (case sensitive) in the target string.

*   This program does not loop for different strings.   Once it processes a string, the program ends.
*    Here, "**character**" means _**any**_ printable character.  They can be letters, numbers or even special symbols.
*   Each target input string should be complex with a mix of characters, special symbols, numbers to show how the program handles each category.

**Input Method Specs**

##### char getKeyCharacter()

> This method requests a single character from the user and continues to ask for it until the user gets it right:  this method will test to make sure the user only types one single character.  0, 2, 3 or more characters will be flagged as an error and the method will keep at the user until he types just one character.  You are not required to use a **char** as an input variable -- in fact, you cannot solve the problem using a char as input (you must think about this and make the appropriate choice here).  What matters is that a **char** is returned, as a functional return, to the client, **main()**.

##### string getString()

> This method requests a string from the user and continues to ask for it until the user gets it right:  this method will test to make sure the user only types a string that has at least 6 characters.  Make this minimum size a constant (**const**), and use that symbolic constant, not the literal (6) wherever it is needed. The acquired string will be returned as a functional return. 

**Processing Method Specs**

_You must write the methods below from scratch (based on the few available tools that I mention in the modules and the links to the allowable character and string methods provided in the module page "**A Nice Example**" ).   Do not rely on any other built-in or pre-existing methods that appear to provide any of this functionality for you.  There is a high value to you in practicing such logic._

##### string maskCharacter(string theString, char keyCharacter)

> This method will take both a string and a character as parameters and return a new string that has each occurrence of the key character replaced by an asterisk, '\*'.

##### string removeCharacter(string theString, char keyCharacter)

> This method will take both a string and a character as parameters and return a new string that has each occurrence of the key character removed, but all other characters left intact.

##### int countKey(string theString, char keyCharacter)

> This method will take both a string and a character as parameters, and return the number of key characters that appear in the string (case sensitive).

**Input Errors**

Whenever the user makes an input error, keep at them until they get it right. Do not return from an input method until you have acquired a legal value, even if it takes years ... .

**Test Run Requirements**:

Submit at least four runs.    In at least one of the four runs, intentionally commit input errors to demonstrate both kinds of illegal input described above.

#### Sample Output

Here is an example of a partial run sample:
```
/\* ---------------------- Sample run ---------------------------------------

Please enter a SINGLE character to act as key: sdfs
Please enter a SINGLE character to act as key:
Please enter a SINGLE character to act as key: d
Please enter a phrase or sentence >= 6 and <= 500 characters:
Please enter a phrase or sentence >= 6 and <= 500 characters: ,,
Please enter a phrase or sentence >= 6 and <= 500 characters: at
Please enter a phrase or sentence >= 6 and <= 500 characters: sdf sdaf ASDF ASDF
 sdf sdf (\*j ljsdf

String with key character, 'd' masked:
 s\*f s\*af ASDF ASDF s\*f s\*f (\*j ljs\*f

String with 'd' removed:
 sf saf ASDF ASDF sf sf (\*j ljsf

# of occurrences  of key character, 'd': 5
Press any key to continue . . .

(MORE RUNS REQUIRED BY STUDENT)


------------------------------------------------------------------------ \*/
```

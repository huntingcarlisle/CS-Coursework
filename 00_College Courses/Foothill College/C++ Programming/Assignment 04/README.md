Assignment 4 - Free Frozen Yogurt
=================================

Make sure you have read and understood

*   both **modules A** and **B** this week, and
*   **module 2R - Lab Homework Requirements**

before submitting this assignment. Hand in only one program, please. 

#### Single-Customer Rewards System

### Understand the Application

Foothill Fro-Yo, LLC, gives customers a stamp every time they purchase a yogurt.
  After they earn a certain number of stamps, they qualify for a free yogurt, 
which they may use toward the purchase of a single yogurt.

Usually 9 is the number of stamps that qualifies, but we will let this be a 
symbolic constant which we can change. But for the purposes of this section, 
let's say that 9_** stamps**_ earns a free yogurt.

The program will be an _**app**_ that runs at the point-of-purchase (cash 
register counter).  The customer or cashier will process a looping series of 
_**purchase transactions**_.  Normally, each transaction asks how many yogurts 
the customer wants to buy and then awards them one **_stamp_** for each yogurt.  

However, if, at the start of a new transaction, the system detects that the 
customer has previously earned 9 or more _**credits**_ (= _**stamps**_), 
the system will inform the operator (customer or cashier) and give the 
operator the option of using 9_** credits**_ toward a _**free yogurt**_.  

The customer may _**accept the free yogurt**_, in which case the number of 
stamps in his account is decreased by 9, and a single free yogurt is dispensed, 
or the customer _**declines**_, which turns this into a _**normal transaction**_, 
allowing the customer to purchase one or more yogurts, adding to the credits 
that the customer already has.

Besides offering a _**purchase transaction**_ each pass of the main execution 
loop, the only other choice is for the operator to _**shut down**_ the system for the day. 

So the main loop has two choices:  **P**:  process a **P**urchase, or **S**: **S**hut down.

Because we don't have arrays yet, this has to be a single-customer system.

### The Program Spec

Process transactions in a main loop.  Start the user's stamp balance at 0.  
Then enter that loop which starts by giving the user two choices at each pass:

*   **P** (process a **P**urchase)
*   **S** (**S**hut down.)

The user is allowed to enter a **_single character_** or _**an entire word**_, 
and the program continues until and unless the user has entered 
an **"s"**, "**S**", "**S**hut down", "**s**tratford", or any word beginning 
with an upper or lower case **'s'**,  in which case the program should end.  

If the user enters a word that starts with any character other than a **'P'** or **'S'** 
(upper or lower case), the letter is ignored and the main menu is repeated, starting a new loop.

**Specifics of the P Selection**

If the operators chooses** **"P"** **(or something compatible) the program 
checks to see how many credits the customer has. (Remember, in this simplified
 exercise, there is only _one customer_.)  If there are fewer than the qualifying
  number (set to 9), then a normal transaction is executed.  If there are 9 or 
  more credits in the customer's account, an award transaction is executed.

##### Normal Transaction

> Ask the user/operator how many yogurts are being purchased, and add this 
number to the customers account/wallet/stamps. At the end of the transaction, 
display the total/accumulated number of stamps earned so far, including the 
current transaction.

##### Award Transaction

> Tell the user/operator that the customer qualifies for a free yogurt.
> 
> 1.  If the user opts for a free yogurt, give them one yogurt, display the new, 
reduced total number of stamps available and end the transaction, moving on to 
the next pass.  To keep things simple, we will not allow purchase of multiple 
yogurts when an award yogurt is being redeemed.  We reduce the number of credits 
by 9 (or whatever the qualifying number is for our system).  We don't add any 
credits/stamps for the award yogurt.  Even if the user has, say, 24 stamps, 
they can only get one yogurt in a single transaction, and the new balance 
will be 24 - 9 = 15, allowing the user to get another free yogurt on the next transaction.
> 2.  If the user opts to not take the award, then the sequence of events 
turns into a _**Normal Transaction**_, in which the user can request to
 purchase one or more yogurts and the corresponding number of stamps is credited
  to the customer's balance.

**Input Errors**

Whenever the user makes an input error, cancel the transaction and proceed to 
the next loop pass (i.e., don't end the program).  Do not attempt to keep the
 user in some sort of micro user-input loop, forcing them to stay within that transaction.

Always check for invalid user input like an invalid character choice, a negative
 number or an out-of-range numeric value, before proceeding.  If the user 
 commits an error of any kind (a bad command letter such as '**T**' or an 
 out-of-range amount), print an error message and return to the top of the
  main loop which asks the user for another command: **P** or **S**.

There is one exception to the error check just described. When it is time 
for the user to enter a number, you can assume he does not type some non-numeric
 value.  You don't have to test for this kind of non-numeric error.

**Do Not Use Methods**

Even though we may have started reading about methods, don't use them for
 this assignment.  We haven't completed their study and you will likely lose
  points for incorrect usage.

**Test Run Requirements**:

Submit at least two runs that shows everything.  In each run, show 
_**several**_ cycles (passes) of the loop.  Specifically, in at least one 
run include _at least_ 6 purchase transactions and at least two free yogurts
 along with the invalid input.  Beyond that, make sure you demonstrate all 
 options. Also demonstrate the capacity to get either single letters or entire
  words from the user, showing at least one user-input error (an illegal choice)
   and one bad numeric input (out-of-range error).

A (partial) sample run is given at the bottom of this page.

_Use **symbolic constants**, not literals, for everything you can in this (and all) assignments._

#### Sample Output

Here is an example of a partial working run:

```
Menu:
  P (process Purchase)
  S (Shut down)

  Your Choice: p

How many yogurts would you like to buy ? 5

 You just earned 5 stamps and have a total of 5 to use.

Menu:
  P (process Purchase)
  S (Shut down)

  Your Choice: purchase

How many yogurts would you like to buy ? -4

 \*\*\* Invalid # yogurts. \*\*\*

Menu:
  P (process Purchase)
  S (Shut down)

  Your Choice: 6

 \*\*\* Use P or S, please. \*\*\*

Menu:
  P (process Purchase)
  S (Shut down)

  Your Choice: p

How many yogurts would you like to buy ? 6

 You just earned 6 stamps and have a total of 11 to use.

Menu:
  P (process Purchase)
  S (Shut down)

  Your Choice: p

You qualify for a free yogurt. Would you like to use your credits? (Y or N) n

How many yogurts would you like to buy ? 3

 You just earned 3 stamps and have a total of 14 to use.

Menu:
  P (process Purchase)
  S (Shut down)

  Your Choice: p

You qualify for a free yogurt. Would you like to use your credits? (Y or N) y

You have just used 9 credits and have 5 left.
Enjoy your free yogurt.
Menu:
  P (process Purchase)
  S (Shut down)


... etc.
```




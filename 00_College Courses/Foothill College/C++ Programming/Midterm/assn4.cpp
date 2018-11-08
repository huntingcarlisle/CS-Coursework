/*
Hunter Carlisle | Foothill College Fall 2018 | Lab Four

This program runs at the point-of-purchase (cash register counter)
 for Foothill Fro-Yo, LLC
*/

#include <iostream>
#include <string>
#include <sstream>
#include <stdio.h>
#include <ctype.h>

using namespace std;

int main()
{
    // Initialize Variables
    const int CREDITS_TO_QUALIFY = 9;
    const int MINIMUM_PURCHASE = 0;
    int stampCount = 0, purchasedYogurts;
    string runSelection, redemptionSelection;
    bool runSystem = true;

    // Program Loop
    while(runSystem)
    {
        startloop:
        cout << endl << "Menu:" << endl;
        cout << "    P (process Purchase)" << endl;
        cout << "    S (Shut down)" << endl << endl;
        cout << "    Your Choice: ";
        cin >> runSelection;
        if (runSelection[0] != 'P' &&
            runSelection[0] != 'p' &&
            runSelection[0] != 'S' &&
            runSelection[0] != 's')
        {
            cout << endl << "*** Use P or S, please. ***" << endl;
            goto startloop;
        }
        // Purchase Selection
        if (runSelection[0] == 'P' || runSelection[0] == 'p')
        {
            // Free Yogurt
            if (stampCount >= CREDITS_TO_QUALIFY)
            {
                cout << endl << "You qualify for a free yogurt. Would you like to "
                                "use your credits? (Y or N) ";
                cin >> redemptionSelection;
                if (redemptionSelection[0] != 'Y' &&
                    redemptionSelection[0] != 'y' &&
                    redemptionSelection[0] != 'N' &&
                    redemptionSelection[0] != 'n')
                {
                    cout << endl << "*** Use Y or N, please. ***" << endl;
                    goto startloop;
                }
                else if (redemptionSelection[0] == 'Y' ||
                         redemptionSelection[0] == 'y')
                {
                    stampCount -= CREDITS_TO_QUALIFY;
                    cout << endl << "You have just used " << CREDITS_TO_QUALIFY <<
                         " credits and have " << stampCount << " left." << endl;
                    cout << "Enjoy your free yogurt." << endl;
                    goto startloop;
                }

            }
            // Purchase Yogurt
            cout << endl << "How many yogurts would you like to buy? ";
            cin >> purchasedYogurts;
            if (purchasedYogurts <= MINIMUM_PURCHASE)
            {
                cout << endl << """*** Invalid # yogurts. ***""" << endl;
                goto startloop;
            }
            stampCount += purchasedYogurts;
            cout << endl << "You just earned " << purchasedYogurts <<
                 " stamps and have a total of " << stampCount << " to use."
                 << endl;

        }
            // Shutdown Selection
        else if (runSelection[0] == 'S' || runSelection[0] == 's')
        {
            runSystem = false;
        }
    }
}


/* --------- RUN 1 ---------------------------------------

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:p
 p

How many yogurts would you like to buy?5
 5

You just earned 5 stamps and have a total of 5 to use.

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:purchase
 purchase

How many yogurts would you like to buy?-4
 -4

*** Invalid # yogurts. ***

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:6
 6

*** Use P or S, please. ***

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:p
 p

How many yogurts would you like to buy?6
 6

You just earned 6 stamps and have a total of 11 to use.

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:p
 p

You qualify for a free yogurt. Would you like to use your credits? (Y or N)n
 n

How many yogurts would you like to buy?3
 3

You just earned 3 stamps and have a total of 14 to use.

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:p
 p

You qualify for a free yogurt. Would you like to use your credits? (Y or N)y
 y

You have just used 9 credits and have 5 left.
Enjoy your free yogurt.

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:s
 s

Process finished with exit code 0


---------------------------------------------------------*/


/* --------- RUN 2 ---------------------------------------


Menu:
    P

    P (process Purchase)
    S (Shut down)

    Your Choice:buy
 buy

*** Use P or S, please. ***

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:Purchase
 Purchase

How many yogurts would you like to buy?1
 1

You just earned 1 stamps and have a total of 1 to use.

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:process
 process

How many yogurts would you like to buy?0
 0

*** Invalid # yogurts. ***

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:p
 p

How many yogurts would you like to buy?123
 123

You just earned 123 stamps and have a total of 124 to use.

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:test
 test

*** Use P or S, please. ***

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:T
 T

*** Use P or S, please. ***

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:p
 p

You qualify for a free yogurt. Would you like to use your credits? (Y or N)n
 n

How many yogurts would you like to buy?15
 15

You just earned 15 stamps and have a total of 139 to use.

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:p
 p

You qualify for a free yogurt. Would you like to use your credits? (Y or N)Yes
 Yes

You have just used 9 credits and have 130 left.
Enjoy your free yogurt.

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:p
 p

You qualify for a free yogurt. Would you like to use your credits? (Y or N)zeb
 zeb

*** Use Y or N, please. ***

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:p
 p

You qualify for a free yogurt. Would you like to use your credits? (Y or N)No
 No

How many yogurts would you like to buy?1
 1

You just earned 1 stamps and have a total of 131 to use.

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:p
 p

You qualify for a free yogurt. Would you like to use your credits? (Y or N)Yes
 Yes

You have just used 9 credits and have 122 left.
Enjoy your free yogurt.

Menu:
    P (process Purchase)
    S (Shut down)

    Your Choice:Slow
 Slow

Process finished with exit code 0

---------------------------------------------------------*/
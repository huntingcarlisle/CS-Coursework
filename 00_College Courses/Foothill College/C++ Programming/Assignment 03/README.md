Assignment 3 - Recipe-to-Nutrition Converter  - Grade 14 out of 18
============================================

Make sure you have read and understood  

[Link to Assignment on Canvas](https://foothillcollege.instructure.com/courses/7627/assignments/186521)

*   both **_m_**_**odules A**_ and _**B**_ this week, and
*   _**module 2R - Lab Homework Requirements**_

before submitting this assignment. Hand in only one program, please. 

#### Nutritional Calculator

Let's write the bare bones of something that could turn into an app.  The user will select amounts of different ingredients that go into a recipe, and the program will give the nutritional value of that recipe.

You'll first have to do some simple research and collect information about the nutritional data of a few of your favorite food ingredients. You'll hard-code these numbers into the program framework that I supply, below. Then, you'll further modify the framework to make it more useful (details, below). Finally, you will run the program several times, giving a different recipe each time.

**_The Research_**: Among some useful sources of nutritional information is [http://nutritiondata.self.com (Links to an external site.)Links to an external site.](http://nutritiondata.self.com). Enter a food name (like "garbanzo beans") and find the closest match from the list you get (say "Chickpeas, boiled without salt").  Use the pull-down to get "Serving Size = 100 gm."  Then scroll down to find the nutrients you are interested in.  In some cases, you may have to refer to an additional page, say, if the nutrient happens to be too detailed for that site. For example, in my program, I selected "soluble fiber" as one of the nutrients, but [nutritiondata.self.com (Links to an external site.)Links to an external site.](http://nutritiondata.self.com) only gives _total_ fiber, so I had to look elsewhere e.g.,  ([http://www.proactivenutrition.net/fiber-content-of-foods/ (Links to an external site.)Links to an external site.](http://www.proactivenutrition.net/fiber-content-of-foods/) or a similar fiber-specific reference) and do some conversions to find out how much soluble fiber was in 100g of my ingredient.

_**A Simple Framework to Start**_: Here is a short program I wrote for you.  Study it carefully until you understand every line, and make sure it runs on your system.  You can't do the assignment until you first get this working and know how it works:
```c++
// CS 2A Lab 3 Framework

#include <iostream>
#include <string>
#include <sstream>
using namespace std;

// main client --------------------------------------------------------
int main()
{
   // food #1 constants
   const string FOOD_1_NAME = "avocado";
   const  int FOOD_1_CALORIES_P100G = 160;  // in calories
   const  double FOOD_1_SOL_FIBER_P100G = 1.75;   // in grams

   // food #2 constants
   const  string FOOD_2_NAME = "tomato";
   const  int FOOD_2_CALORIES_P100G = 18;  // in calories
   const  double FOOD_2_SOL_FIBER_P100G = .12;   // in grams

   // food #3 constants
   const  string FOOD_3_NAME = "buffalo mozzarella";
   const  int FOOD_3_CALORIES_P100G = 282;  // in calories
   const  double FOOD_3_SOL_FIBER_P100G = 0.;   // in grams

   const  string INDENT = "   ";

   string recipeName, userInputStr;
   int userInputInt;
   double totalSolFiber, totalCals;

   // initialize accumulator variables
   totalSolFiber  = 0.;
   totalCals =  0;

   // print menu
   cout << "---------- List of Possible Ingredients ---------" << endl;
   cout << INDENT << "Food #1: " << FOOD_1_NAME << endl;
   cout << INDENT << "Food #2: " << FOOD_2_NAME << endl;
   cout << INDENT << "Food #3: " << FOOD_3_NAME << endl << endl;    

   // name of recipe
   cout << "What are you calling this recipe? ";
   getline(cin, recipeName);

   // food #1 ---------------------------------------------------------
   cout << "How many grams of " << FOOD_1_NAME << "? ";
   getline(cin, userInputStr);
   istringstream(userInputStr) >> userInputInt; 

   // update accumulators
   totalCals += userInputInt * (FOOD_1_CALORIES_P100G / 100.);
   totalSolFiber  += userInputInt * (FOOD_1_SOL_FIBER_P100G / 100.);

   // food #2 ---------------------------------------------------------
   cout << "How many grams of " << FOOD_2_NAME << "? ";
   getline(cin, userInputStr);
   istringstream(userInputStr) >> userInputInt;

   // update accumulators
   totalCals += userInputInt * (FOOD_2_CALORIES_P100G / 100.);
   totalSolFiber  += userInputInt * (FOOD_2_SOL_FIBER_P100G / 100.);

   // food #3 ---------------------------------------------------------
   cout << "How many grams of " << FOOD_3_NAME << "? ";
   getline(cin, userInputStr);
   istringstream(userInputStr) >> userInputInt;

   // update accumulators
   totalCals += userInputInt * (FOOD_3_CALORIES_P100G / 100.);
   totalSolFiber  += userInputInt * (FOOD_3_SOL_FIBER_P100G / 100.);   

   // report results --------------------------------------------------
   cout << "\nNutrition for " << recipeName << "------------" << endl; 
   cout << INDENT << "Calories: " << totalCals << endl;
   cout << INDENT << "Soluble Fiber: " << totalSolFiber << " grams\n";

   return 0;
}
```
Here are two sample runs:
```
/\* -------------------------- run #1 ----------------------

---------- List of Possible Ingredients ---------
   Food #1: avocado
   Food #2: tomato
   Food #3: buffalo mozzarella

What are you calling this recipe? Michael's Simple Guacamole
How many grams of avocado? 200
How many grams of tomato? 350
How many grams of buffalo mozzarella? 0

Nutrition for Michael's Simple Guacamole------------
   Calories: 383
   Soluble Fiber: 3.92 grams
Press any key to continue . . .

----------------------------- run #2 -----------------------

---------- List of Possible Ingredients ---------
   Food #1: avocado
   Food #2: tomato
   Food #3: buffalo mozzarella

What are you calling this recipe? Michael's Simple Caprese
How many grams of avocado? 0
How many grams of tomato? 182
How many grams of buffalo mozzarella? 150

Nutrition for Michael's Simple Caprese------------
   Calories: 455.76
   Soluble Fiber: 0.2184 grams
Press any key to continue . . .

--------------------------------------------------------------- \*/
```
Notice that the user gets a list of _**three ingredients**_ and selects quantities of each for his/her recipe. 

*   **English Language Hint**:  An _**ingredient**_ is something you would buy and use in the recipe.  It could be a vegetable or a brand name of some pre-cooked mixture.  Examples of _**ingredients**_ are _**tomatoes**_, _**avocado**_, _**olive oil**_, _**Campbell's beef broth**_, _**sugar**_, _**garlic**_, _**split peas**_, _**soy beans**_, _**tofu**_, _**pasta**_, etc.

The program asks for every one of the ingredients for your recipe, so if one is not included in the recipe, the user has to answer "0" when prompted for the # of grams.  (This can only be avoided if you use loops to let the user select from the ingredient menu, but we're not ready for loops yet.) You can see how I provided ingredients that can make two very different dishes, depending on which ones the user chooses.

_**Your Assignment**_:  You will have some fun embellishing the above program as follows:

1.  Display a list of between _**four**_ and **_six_** ingredients to the console (instead of my _three_).
2.  Define between  _**four**_ and **_six nutrient constants_** (instead of my _two_).  I defined and computed _**calories**_ and _**soluble fiber**_, but you will define and compute _**four**_, which may include those two, or be four entirely different nutrients. **English Language Hint**:  A **_nutrient_** is something like _**calories**_, _**protein**_, _**fat**_, _**vitamin C**_, _**fiber**_.  These are compounds that are found in foods.
3.  Prompt for, and receive, the number of _**servings**_, e.g., two (2) or nine (9), and instead of giving the nutritional breakdown of the entire recipe, only state the nutritional value in a _single serving_.  **English Language Hint**:  A **_serving_** is how much you serve to one person.  If the _**recipe**_ says it "**serves seven**" that means that you follow the directions and amounts exactly, but when you are done, you **divide the food you made into seven equal portions**.  Each portion is one **_serving_**.
4.  Add error testing.  If the user enters an amount (grams) either < 0 or > 1500, end the program, instantly, with an error message.  If the user enters a number of servings < 1 or > 15, end the program, instantly with an error message.  These limits must be defined as _symbolic constants_ and those constants, not the literals, used throughout in the program.

You don't have to use my ingredients or nutrients, but you may.  Run the program at least five times entering different recipes, and making an input error in one of those five runs, exercising your error testing.  Vary the number of servings from run-to-run so you don't repeat the same number of servings in any two runs.  Submit all five runs with your source.

### What Your Program Will Look Like When Run

Your program will (in the following order during execution):

1.  ask for the name of the recipe,
2.  ask for the number of portions that this recipe serves,
3.  start a sequence of prompts for the number of grams of each food the user wants in this recipe and
4.  print the results -- that is, the nutritional values of each nutrient per serving.
5.  If step 2 or 3 gets an out-of-range value from the user, the program will end as described above.

### \------------SAMPLE RUN --------------------
```
List of Supplies (no user interaction here)
.....
.....
.....


Name of recipe?  answer
# servings?  answer

#grams of sugar?  92
#grams of honey?  291
#grams of donuts?  4
#grams of syrup?  12

... computing ...

The nutritional value per serving is blah blah ...
```
It will be interesting to see how many different recipes you can make using the same _**four**_ to **_six_** ingredients.

_Bon appétit_.

Once your assignment is graded and returned, you can view the instructor solution here:

*   [Quiz List](/courses/7627/quizzes)

Your access code will be provided in your graded assignment comments.  Find the assignment in the list, click "Take Survey" and you will see the solution.  Even though it is called a "Quiz," it is actually just a solution; there is no need to submit anything, just open the quiz and see the solution.

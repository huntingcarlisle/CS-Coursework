#!/usr/bin/env python3
from datetime import date
"""
Hunter Carlisle | Foothill College Fall 2018 | Lab One

This program takes user input and prints various expressions to console.
Inputs: User Last Name and Student ID
Print Output: Expressions per Assignment Spec
"""

# Get and Validate User Input
while True:
    family_name = input("Enter your family name: ")
    if (family_name.isalpha() and (len(family_name) in range(2, 15))):
        break
while True:
    student_id = input("Enter your student ID: ")
    if (student_id.isdigit() and (len(student_id) == 8)):
        break
n_let = len(family_name)
my_id = sum(int(digit) for digit in str(student_id))

# Evaluate and Store Expressions per Spec
expressions = ['{0:.2f}'.format(my_id / 2), my_id % 2, sum(range(2, n_let)),
               my_id + n_let, abs(n_let - my_id),
               '{0:.2f}'.format(my_id / (n_let + 1100)),
               bool((n_let % n_let) and (my_id * my_id)),
               bool(1 or (my_id / 0)), '{0:.2f}'.format(round(3.15, 1))]

# Print to Console
print("my_id is: " + str(my_id))
print("n_let is: " + str(n_let))
for index, value in enumerate(expressions, start = 1):
    print("expression {}: {}".format(str(index),
                                     str(value)))

print("Today's date is " + str(date.today()))

# Program Run
"""
/home/huntingcarlisle/coding/metaSlate-master/venvUbuntu/bin/python /home/huntingcarlisle/assignementOne/HunterCarlisleLab1.py
Enter your family name: Carlisle
Enter your student ID: 20343101
my_id is: 14
n_let is: 8
expression 1: 7.00
expression 2: 0
expression 3: 27
expression 4: 22
expression 5: 6
expression 6: 0.01
expression 7: False
expression 8: True
expression 9: 3.10
Today's date is 2018-10-02

Process finished with exit code 0
"""

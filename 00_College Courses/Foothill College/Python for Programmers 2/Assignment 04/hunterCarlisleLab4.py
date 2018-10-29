"""
Hunter Carlisle | Foothill College Fall 2018 | Lab Four

This application converts date in "mm/dd/yyyy" format to "month day, year" format.
"""

import re

# CONSTANT VARIABLES
DATE_PATTERN = re.compile(r"""
    ((?:(?:0[13578]|1[02])\/(?:0[1-9]|[12][0-9]|3[01])\/(?:[1-2][0-9]{3}))|
    (?:(?:0[469]|11)\/(?:0[1-9]|[12][0-9]|30)\/(?:[1-2][0-9]{3}))|
    (?:(?:02)\/(?:0[1-9]|1[0-9]|2[0-8])\/(?:[1-2][0-9]{3}))|
    (?:(?:02)\/(?:29)\/(?:(?:[1-2][0-9](?:04|08|[2468][048]|[13579][26]))|2000)))
    """, re.X)
MONTH_NAMES = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
TEST_LOOPS = 5


# METHODS
def date_converter():
    """Gets a valid date in 'mm/dd/yyyy' format and
        returns a date in 'Month Day, Year' format."""
    user_input = input("Enter a date (mm/dd/yyyy): ")
    if is_valid_date(user_input):
        return stringify_date(user_input)
    else:
        print("Invalid date entered.")
        raise SystemExit


def is_valid_date(user_input):
    """Validates a date string."""
    return re.match(DATE_PATTERN, user_input)


def stringify_date(user_date):
    """Inputs date in 'mm/dd/yyyy' format and
        returns date in 'Month Day, Year' format."""
    user_date_list = user_date.split("/")
    month_index = int(user_date_list[0]) - 1
    month_string = MONTH_NAMES[month_index]
    stringified_date = ('The converted date is: {} {}, {}'.format(month_string, user_date_list[1], user_date_list[2]))
    return stringified_date


def test_run():
    """Loops through a number of date inputs per assignment spec."""
    for i in range(TEST_LOOPS):
        print(date_converter())
        print()


test_run()

""" PROGRAM RUN
Enter a date (mm/dd/yyyy): 11/06/1989
The converted date is: November 06, 1989

Enter a date (mm/dd/yyyy): 12/25/1001
The converted date is: December 25, 1001

Enter a date (mm/dd/yyyy): 01/01/2999
The converted date is: January 01, 2999

Enter a date (mm/dd/yyyy): 02/29/1996
The converted date is: February 29, 1996

Enter a date (mm/dd/yyyy): 02/29/1997
Invalid date entered.

Process finished with exit code 0
"""

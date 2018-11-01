"""
Hunter Carlisle | Foothill College Fall 2018 | Lab Four

This application converts date in "mm/dd/yyyy" format to "month day, year" format.
"""

import re
import functools


members = ["555-2345 Foothill, Ann",
           "DeAnza, P. Bob",
           "552-4301 Fish, Mardy",
           "555-7666 Smith, Claire May"]
for i in members:
    res = re.search(r"([0-9-]*)\s*([A-Za-z]+),\s+(.*)",i)
    print(res.group(3) + " " + res.group(2) + " " + res.group(1))
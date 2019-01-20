"""
Hunter Carlisle | Foothill College Fall 2018 | Lab Five

This program takes a website URL and a regex list of topics.
It computes the number of instances of each topic
on the website, printing a simple yet complete report.
"""

import urllib.request
import urllib.parse
import re
from datetime import datetime

# CONSTANT VARIABLES
NAS_URL = 'http://www.nasonline.org/'
TOPICS = ["research", "climate", "evolution",
          "cultural", "leadership", "policy", "fake news"]
DATE = datetime.now().strftime("%Y-%m-%d")


# METHODS
def stringify_url(url):
    """Inputs a website URL
        Returns a string representation of the content"""
    return urllib.request.urlopen(url).read().decode("latin-1")


def create_occurrence_dict(website, topics):
    """Inputs website text and a list of topics.
        Returns a dictionary containing number of occurrences of each topic."""
    occurrence_dict = {}
    for term in topics:
        regex_term = r'(?i)\b' + re.escape(term) + r'\b'
        occurrence_dict[term] = str(len(re.findall(regex_term, website)))
    return occurrence_dict


def report_occurrences(occurrence_dict):
    """Inputs a dictionary of topics and occurrences
        Prints a report detailing dictionary records per program spec."""
    print(f'Today\'s date is {DATE}')
    for topic, occurrences in occurrence_dict.items():
        print(f'{topic} appears {occurrences} times.')


def main():
    """Runs program per spec."""
    try:
        website = stringify_url(NAS_URL)
        occurrences = create_occurrence_dict(website, TOPICS)
        report_occurrences(occurrences)
    except Exception as e:
        print(str(e))


main()

""" PROGRAM RUN
Today's date is 2018-11-07
research appears 8 times.
climate appears 4 times.
evolution appears 4 times.
cultural appears 8 times.
leadership appears 6 times.
policy appears 10 times.
fake news appears 0 times.

Process finished with exit code 0
"""
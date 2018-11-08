Python WWW API
--------------

Application: Web and Search
---------------------------

**_Make sure that you have read and understood_**

*   **_module Unit 6 _**
*   **Textbook reading:** _The Quick Python Book_, Third Ed._, _Naomi Ceder, Ch. 22.4
*   **_Helpful Python3 tutorial link:_**
    *   [**_urllib_**](https://docs.python.org/3/library/urllib.html)

**Understand the Application**

The National Academy of Science (NAS) marketing department is interested to get an accurate assessment on the coverage of publicized topics on the current website. The marketing strategy team is divided over which of a list of topics is most widely represented on the website.

You have been hired to put a decision on the business operations (bizops) table as to which topic is most represented on the NAS website.

Specifically we will write a Python3 program that takes the URL of the National Academy of Science and a list of topics.  For each topic of interest, your solution intelligence will compute the number of instances of each topic on the NAS website providing a simple yet complete report.

**The Program Spec**

Write a program that takes the NAS website url:  [http://www.nasonline.org,](http://www.nasonline.org/) downloads the HTML document, and decodes it into a string. 

Create a list of the topics under review which include:  research, climate, evolution, cultural and leadership.  To provide additional insight to the bizops team, include an additional topic of your selection to the review list. 

Determine the number of occurrences of each topic that appears on the webpage.

Provide a report summary that specifies the topic of interest and the number of times that the subject presents on the NAS website.

Import the [datetime ](https://docs.python.org/3/library/datetime.html)module to generate the date of your report run. Print this date in your run output.  

**Deliverable:  yournameLab5.py**  Your source code solution and a copy of the run pasted into your source submission file.  Be sure to comment out your run so that your **.py** file will still run in the grader test bed.   

**Test Run Requirements:** 

Here are some other tips and requirements:

1.    Topic list contains the list of subjects in the program spec (including a minimum of one additional insight subject presented by you i.e. a minimum of 6 topics).

2\.   The **urlopen()** response usually returns a special object called a _byte string_. In order to work with the response as a string, use the **decode()** method to convert it into a string with an encoding.  Use '_utf-8_' encoding.

3\.   Validate if there is an error opening the url or decoding it. 

4.    Generate a report summary that pairs the subject with the number of occurrences as measured by number of instances found of the topic on the website.

Here is a sample run:
```
Today's date is 2018-05-15  
research appears 5 times.  
...  
```


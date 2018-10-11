def mergeDictionaries (dictOne, dictTwo, dictThree):
    """
    Takes as input three dictionaries, and returns a single merged dictionary containing all values according to key in the input dictionaries.
    INPUTS: three dictionaries, containing unique keys (strings) and values (strings or lists of strings)
    OUTPUT: merged dictionary, containing all keys in input dictionaries and all values associated with any key across all dictionaries. If there is only one value, it is stored as a string. If there is more than one value, it is stored as a list of strings.
    """
    myDict = dictOne.copy()
    iterList = [dictTwo, dictThree]
    for item in iterList:
        for key in item:
            if key in myDict:
                while type(myDict[key]) is str:
                    myDict[key] = myDict[key].split(",")
                if type(item[key]) is str:
                    myDict[key].append(item[key])
                else:
                    myDict[key].extend(item[key])
            else:
                myDict[key] = item[key]
    return myDict

# test dictionaries
roommate1Shopping = {'fruit': 'apples', 'meat': 'chicken', 'vegetables': 'potatoes', 'drinks': ['beer','wine'], 'dessert': 'ice cream'}
roommate2Shopping = {'fruit': 'lemons', 'meat': 'hamburger', 'drinks': ['apple juice', 'orange juice', 'vodka']}
roommate3Shopping = {'fruit': ['oranges', 'bananas'], 'vegetables': ['lettuce', 'carrots'], 'drinks': 'milk'}


print(mergeDictionaries(roommate1Shopping, roommate2Shopping, roommate3Shopping))

"""
"/home/huntingcarlisle/PycharmProjects/Assignment 3/venv/bin/python" "/home/huntingcarlisle/PycharmProjects/Assignment 3/hcarlisle_assigntment3.py"
{'drinks': ['beer', 'wine', 'apple juice', 'orange juice', 'vodka', 'milk'], 'vegetables': ['potatoes', 'lettuce', 'carrots'], 'dessert': 'ice cream', 'meat': ['chicken', 'hamburger'], 'fruit': ['apples', 'lemons', 'oranges', 'bananas']}

Process finished with exit code 0
"""
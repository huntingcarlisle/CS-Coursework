def isIn(char, aStr):
    '''
#     char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    lengthAStr = len(aStr)
    if lengthAStr == 0:
        return False
    if char == aStr[(lengthAStr-1)//2]:
        return True
    else:
        if char > aStr[(lengthAStr-1)//2]:
            return isIn(char, aStr[(lengthAStr-1)//2:lengthAStr-1])
        elif char < aStr[lengthAStr//2]:
            return isIn(char, aStr[0:(lengthAStr-1)//2])
        else:
            return False

print(Test: isIn('w', 'chlmnnpqqrstvvwz'))

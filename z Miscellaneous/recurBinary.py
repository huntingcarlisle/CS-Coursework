def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    # Base Cases
    if aStr == '':
        return False
    if len(aStr) == 1:
        return char == aStr

    midIndex = len(aStr)//2
    midChar = aStr[midIndex]

    if char == midChar:
        return True
    elif char < midChar:
        return isIn(char, aStr[:midIndex])
    else:
        return isIn(char, aStr[midIndex+1:])


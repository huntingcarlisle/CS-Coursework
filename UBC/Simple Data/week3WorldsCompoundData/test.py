def spell(numToSpell):
    """
    Inputs an integer (numToSpell) and returns a string (spelledNum) containing the input spelled out in Engish
    """
    # Initialize variables
    spelledNum = ""

    # Handle zero and negative value inputs
    if numToSpell == 0:
        return 'zero'
    if numToSpell < 0:
        spelledNum= "negative "
        numToSpell = abs(numToSpell)

    # convert number to spelled out string
    if numToSpell < 1000:
        spelledNum += threeDigit (numToSpell)
        return spelledNum
    elif numToSpell < 1000000:
        spelledNum += threeDigit (numToSpell // 1000) + " thousand " + threeDigit (numToSpell % 1000)
        return spelledNum
    else:
        spelledNum += threeDigit ( numToSpell // 1000000 ) + " million " + \
        threeDigit ((numToSpell % 1000000) // 1000) + " thousand " + threeDigit ((numToSpell % 1000000) % 1000)
        return spelledNum


def threeDigit (threeDigitInteger):
    """
    Inputs a three digit integer and returns a string (threeDigitString) containing the input spelled out in Engish
    """
    threeDigitString = ""
    numberWords = { 1 :'one', 2 :'two', 3 :'three',4 :'four', 5 :'five', 6 :'six', 7 :'seven', 8 :'eight', 9 :'nine', 10 : 'ten', 11 : 'eleven', 12 :'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen', 20 : 'twenty', 30 : 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70 :'seventy', 80: 'eighty', 90: 'ninety'}

    # hundreds
    hundredsNumber = threeDigitInteger // 100
    if (hundredsNumber > 0):
        hundredsWord = numberWords[hundredsNumber]
        threeDigitString += hundredsWord + " hundred "
        threeDigitInteger -= hundredsNumber * 100

    # tens and units
    if ((threeDigitInteger % 100) < 20):
        threeDigitString += numberWords[(threeDigitInteger % 100)]
    else:
        tensNumber = threeDigitInteger // 10
        tensWord = numberWords[(tensNumber * 10)]
        threeDigitString += tensWord + " " + numberWords[(threeDigitInteger % 10)]
    return threeDigitString

######## TESTs function spell()  ###########
print (spell (123456789) )
print (spell (456678) )
print (spell (66) )
print (spell (-123456789) )
print (spell (-456678) )
print (spell (-418) )
print (spell (-13456678) )
print (spell (7) )
print (spell (10004) )



    #if spelledInteger > 1000 and spelledInteger < 1000000:
        # separate next three digits into their own string
        # call function on them
        #    append to words


    #elif spelledInteger < 1000000:

        # separate next three digits into their own string
        # call function on them
        #    append to words






    #return " ".join(words)





"""
if __name__ == '__main__':
    import doctest
    print(doctest.testmod(verbose=False))
"""
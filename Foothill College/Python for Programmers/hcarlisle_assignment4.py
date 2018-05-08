# This program spells out in english any integer between -999,999,999 and 999,999,999

def spell(numToSpell):
    """
    Inputs an integer between -1bn and 1bn and returns a string containing the input spelled out in Engish
    """
    spelledNum =""

    # Handle negative value inputs
    if numToSpell < 0:
        spelledNum += "negative "
        numToSpell = abs(numToSpell)

    # convert number to spelled out string
    if numToSpell == 0:
        spelledNum += "zero"
    elif numToSpell < 1000:
        spelledNum += threeDigit(numToSpell)
    elif numToSpell < 1000000:
        spelledNum += threeDigit(numToSpell // 1000) + " thousand " + threeDigit(numToSpell % 1000)
    else:
        spelledNum += threeDigit(numToSpell // 1000000) + " million " + \
        threeDigit((numToSpell % 1000000) // 1000) + " thousand " + threeDigit((numToSpell % 1000000) % 1000)
    return spelledNum


def threeDigit(threeDigitInteger):
    """
    Inputs an integer with no more than three digits and returns a string containing the input spelled out in Engish
    """
    numberWords = { 1 :'one', 2 :'two', 3 :'three',4 :'four', 5 :'five', 6 :'six', 7 :'seven', 8 :'eight', 9 :'nine', 10 : 'ten', \
    11 : 'eleven', 12 :'twelve', 13 : 'thirteen', 14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen', \
    20 : 'twenty', 30 : 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70 :'seventy', 80: 'eighty', 90: 'ninety'}
    threeDigitString = ""

    # hundreds
    hundredsNumber = threeDigitInteger // 100
    if (hundredsNumber > 0):
        threeDigitString += numberWords[hundredsNumber] + " hundred "
        threeDigitInteger = threeDigitInteger % 100

    # tens and units
    if ((threeDigitInteger) < 20):
        threeDigitString += numberWords[(threeDigitInteger)]
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
print (spell (0) )
print (spell (10004) )

"""

~/workspace/CS-Coursework/Foothill College/Python for Programmers/ (master) $ python hcarlisle_assignment4.py
one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine
four hundred fifty six thousand six hundred seventy eight
sixty six
negative one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine
negative four hundred fifty six thousand six hundred seventy eight
negative four hundred eighteen
negative thirteen million four hundred fifty six thousand six hundred seventy eight
zero
ten thousand four

"""



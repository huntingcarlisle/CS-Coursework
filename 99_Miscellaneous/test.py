# Paste your code into this box
s = 'abcdefghijklmnopqrstuvwxyz'

tempString = s[0]
checkChar = s[0]
bigString = ""

for i in range(1,len(s)):
    if s[i] >= checkChar:
        tempString += s[i]
        checkChar = s[i]
    else:
        if len(tempString) > len(bigString):
            bigString = tempString
            tempString = s[i]
            checkChar = s[i]
        else:
            tempString = s[i]
            checkChar = s[i]
if len(tempString) > len(bigString):
    print ("Longest substring in alphabetical order is: " + str(tempString))
else:
    print("Longest substring in alphabetical order is: " + str(bigString))
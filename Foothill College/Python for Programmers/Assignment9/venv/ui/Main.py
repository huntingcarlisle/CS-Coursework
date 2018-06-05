
## PASS TESTS

try:
    c1 = Card(5, 'c')
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

try:
    pass
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

try:
    c2 = Card(1, 's')
    c3 = Card(13, 'd')
    c4 = Card(9, 'h')
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

try:
    pass
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

print (c1)
print (c2)
print (c3)
print (c4)
print()
print (c1.getRank())
print (c2.getRank())
print (c3.getRank())
print (c4.getRank())
print()
print (c1.getSuit())
print (c2.getSuit())
print (c3.getSuit())
print (c4.getSuit())
print()
print (c1.bjValue())
print (c2.bjValue())
print (c3.bjValue())
print(c4.bjValue())
print()

## FAIL TESTS

try:
    c5 = Card('a','c')              # TypeError Rank
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

try:
    c6 = Card(1, 1)                 # TypeError Suit
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

try:
    c7 = Card(-1, 'c')              # ValueError Rank
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

try:
    c8 = Card(1, 'z')               # ValueError Suit
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

## RECORDING

'''
~/workspace/CS-Coursework/Foothill College/Python for Programmers/ (master) $ python hcarlisle_assignment6.py
Five of Clubs
Ace of Spades
King of Diamonds
Nine of Hearts

5
1
13
9

c
s
d
h

5
1
10
9

Rank must be an integer
Suit must be a one-character string
Rank must be between 1 and 13
Suit must be one of ['s', 'c', 'h', 'd']
'''

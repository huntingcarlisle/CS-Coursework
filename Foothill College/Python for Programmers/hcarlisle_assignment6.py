class Card(object):
    '''
    One object of class Card is a representation of one playing card from a standard 52 card deck
    '''
    ## CLASS VARIABLES

    ENGLISH_REPRESENTATION = { 1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King", 'c': "Clubs", 'd': "Diamonds", 'h': "Hearts", 's': "Spades"}

    ## CLASS METHODS

    def __init__(self, rank, suit):
        '''
        Initializes a Card object

        rank (integer[1,13]): the rank of the card, indicating 'Ace' through 'King'
        suit (character): the suit of the card, one of:
            - 'd' : diamonds
            - 'c' : clubs
            - 'h' : hearts
            - 's' : spades

        a Card object has two attributes:
            self.rank
            self.suit
        '''
        if type(rank) == int:
            if rank >= 1 and rank <= 13:
                self.rank = rank
            else:
                raise ValueError("Rank must be between 1 and 13")
        else:
            raise TypeError("Rank must be an integer")

        if type(suit) == str:
            if suit in ['s', 'h', 'c', 'd']:
                self.suit = suit
            else:
                raise ValueError("Suit must be one of ['s', 'c', 'h', 'd']")
        else:
            raise TypeError("Suit must be a one-character string")

    def getRank(self):
        '''
        Used to safely access self.rank outside of the class

        Returns: self.rank
        '''
        return self.rank

    def getSuit(self):
        '''
        Used to safely access self.suit outside of the class

        Returns: self.suit
        '''
        return self.suit

    def bjValue(self):
        '''
        Calculates the blackjack value of a card, a number

        Returns: the blackjack value of the card
        '''
        if self.rank > 10:
            return 10
        else:
            return self.rank

    def __str__(self):
        '''
        Returns: the name of the playing card spelled out
        '''
        return Card.ENGLISH_REPRESENTATION[self.rank] + " of " + Card.ENGLISH_REPRESENTATION[self.suit]

## PASS TESTS

try:
    c1 = Card(5, 'c')
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

try:
    c2 = Card(1, 's')
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

try:
    c3 = Card(13, 'd')
except ValueError as errorObject:
    print(errorObject)
except TypeError as errorObject:
    print(errorObject)

try:
    c4 = Card(9, 'h')
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

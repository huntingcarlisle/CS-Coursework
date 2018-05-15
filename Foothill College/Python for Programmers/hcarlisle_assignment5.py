class Card(object):
    '''
    One object of class Card is a representation of one playing card from a standard 52 card deck
    '''
    ## VARIABLES
    DICT = { 1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King", 'c': "Clubs", 'd': "Diamonds", 'h': "Hearts", 's': "Spades"}

    ## METHODS
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
        self.rank = rank
        self.suit = suit

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
        return Card.DICT[self.rank] + " of " + Card.DICT[self.suit]

c1 = Card(5, 'c')
c2 = Card(1, 's')
c3 = Card(13, 'd')
c4 = Card(9, 'h')
print (c1)
print (c2)
print (c3)
print (c4)
print (c1.getRank())
print (c2.getSuit())
print (c3.bjValue())
print(c4.bjValue())


'''
~/workspace/CS-Coursework/Foothill College/Python for Programmers/ (master) $ python hcarlisle_assignment5.py
Five of Clubs
Ace of Spades
King of Diamonds
Nine of Hearts
5
s
10
9
'''

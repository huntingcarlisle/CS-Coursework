from card import Card
import random

class Hand(object):
    """
    One object of class Hand represents a hand of playing cards drawn from an infinite number of standard 52-card decks
    """
    def __init__(self, numCardsInHand):
        """
        Initialize a Hand object

        numCardsInHand (integer): the number of randomly generated Card objects in the initial hand
        """
        self.hand = []
        if type(numCardsInHand) == int:
            for slot in range(numCardsInHand):
                self.hand.append(self.generateRandomCard())
        else:
            raise TypeError("Number of Cards must be an integer")

    def __str__(self):
        """ Return the string representation of the Hand. """
        handString = ""
        for card in self.hand:
            handString += str(card) + "\n"
        return handString

    def __len__(self):
        """ Return the length representation of the Hand. """
        return len(self.hand)

    def __getitem__(self, item):
        """ Implement evaluation of self[key] """
        return self.hand[item]

    def hitMe(self):
        """ Add one randomly generated Card to the Hand. """
        self.hand.append(self.generateRandomCard())

    def addCard(self, card):
        """ Add a specific Card to the Hand. """
        self.hand.append(card)

    def getHand(self):
        '''
        Safely access a copy of self.hand outside of the class.

        Return a COPY of self.hand
        '''
        return self.hand[:]

    def bjValue(self):
        """ Return the blackjack value for the entire Hand of cards. """
        bjTotal = 0
        for i in range(len(self.hand)):
            bjTotal += self.hand[i].bjValue()
        return bjTotal

    def generateRandomCard(self):
        """ Return a randomly generated card object. """
        cardRank = random.randint(1, 13)
        cardSuit = random.choice('schd')
        return Card(cardRank, cardSuit)

from card import Card
import random

class Hand(object):
    """
    One object of class Hand represents a hand of playing cards drawn from an infinite number of standard 52-card decks
    """
    def __init__(self, numCardsInHand):
        """
        REQUIRES: numCardsInHand must be a positive integer greater than zero
        EFFECTS: consumes numCardsInHand and populates a Hand Object with that number of Card objects
        """
        self.hand = []
        if type(numCardsInHand) == int:
            for slot in range(numCardsInHand):
                self.hand.append(self.generateRandomCard())
        else:
            raise TypeError("Number of Cards must be an integer")

    def hitMe(self):
        """
        :modifies: adds one randomly generated Card to the Hand
        """
        self.hand.append(self.generateRandomCard())

    def addTestCard(self, card):
        """
        :modifies: adds a specific test Card to the Hand
        """
        self.hand.append(card)

    def getHand(self):
        '''
        Used to safely access a copy of self.hand outside of the class

        Returns: a COPY of self.hand
        '''
        return self.hand[:]

    def bjValue(self):
        """
        :return: the blackjack value for the entire Hand of cards
        """
        bjTotal = 0
        for i in range(len(self.hand)):
            bjTotal += self.hand[i].bjValue()
        return bjTotal

    def __str__(self):
        """
        :return: the string representation of the Hand
        """
        handString = ""
        for card in self.hand:
            handString += str(card) + "\n"
        return handString

    def __len__(self):
        return len(self.hand)

    def __getitem__(self, item):
        return self.hand[item]

    def generateRandomCard(self):
        """
        :return: a randomly generated card object
        """
        cardRank = random.randint(1, 13)
        cardSuit = random.choice('schd')
        return Card(cardRank, cardSuit)

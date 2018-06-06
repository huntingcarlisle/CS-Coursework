from card import Card
from hand import Hand


class HandFile(object):
    """
    One object of class HandFile represents a text file containing the cards in a given Hand Object.
    """
    def __init__(self, hand):
        """
        Initialize a HandFile object, which is a text file containing the string representation of the cards in a Hand Object

        hand (Hand Object): contains zero or more Card Objects, to be stored as strings in the HandFile object
        """
        handFile = open("handOnDisk.txt", "w")
        for i in range(len(hand)):
            handFile.write(str(hand[i]) + "\n")
        handFile.close()

    def handFileToHandObject(self):
        """ Convert HandFile to Hand Object. """
        newHandFile = open("handOnDisk.txt", "r")
        newHand = Hand(0)
        for line in newHandFile:
            newHand.addCard(self.getCardFromStr(line))
        newHandFile.close()
        return newHand

    def getCardFromStr(self, cardStr):
        """ Convert card as String to Card Object. """
        cardList = cardStr.split()
        cardRank = self.strToCardValue(cardList[0])
        cardSuit = self.strToCardValue(cardList[2])
        return Card(cardRank, cardSuit)

    def strToCardValue(self, str):
        """ Convert string representation of card to Card object """
        CARD_REPRESENTATION = {v: k for k, v in Card.ENGLISH_REPRESENTATION.items()}
        return CARD_REPRESENTATION[str]

'''
# Example usage, see test_blackjack.py for full test suite
h1 = Hand(5)
hf1 = HandFile(h1)   # Go check out handOnDisk.txt if you would like!
h2 = hf1.handFileToHandObject()
print(str(h2) == str(h1))
'''

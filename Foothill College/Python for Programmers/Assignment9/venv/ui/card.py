class Card(object):
    """
    One object of class Card is a representation of one playing card from a standard 52 card deck
    """
    # CLASS VARIABLES

    ENGLISH_REPRESENTATION = {1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King", 'c': "Clubs", 'd': "Diamonds", 'h': "Hearts", 's': "Spades"}

    # CLASS METHODS

    def __init__(self, rank, suit):
        """
        Initialize a Card object

        rank (integer[1,13]): the rank of the card, indicating 'Ace' through 'King'
        suit (character): the suit of the card, one of:
            - 'd' : diamonds
            - 'c' : clubs
            - 'h' : hearts
            - 's' : spades

        a Card object has two attributes:
            self.rank
            self.suit
        """
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
        """
        Safely access self.rank outside of the class

        Returns: self.rank
        """
        return self.rank

    def getSuit(self):
        """
        Safely access self.suit outside of the class

        Returns: self.suit
        """
        return self.suit

    def bjValue(self):
        """
        Calculate the blackjack value of a card, a number

        Returns: the blackjack value of the card
        """
        if self.rank > 10:
            return 10
        else:
            return self.rank

    def __str__(self):
        """
        Returns: the name of the playing card spelled out
        """
        return Card.ENGLISH_REPRESENTATION[self.rank] + " of " + Card.ENGLISH_REPRESENTATION[self.suit]





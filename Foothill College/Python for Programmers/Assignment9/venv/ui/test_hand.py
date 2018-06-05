import unittest

from card import Card
from hand import Hand


class TestCard(unittest.TestCase):

    def setUp(self):
        """
        setUp function for Card unit tests
        """
        self.c1 = Card(5, 'c')
        self.c2 = Card(1, 's')
        self.c3 = Card(13, 'd')
        self.c4 = Card(9, 'h')

    def test_invalidInitSuit(self):
        """
        Unit test for Card.__init__ Suit errors
        """
        print("test_Card.invalidInitSuit")
        with self.assertRaises(TypeError):
            self.c6 = Card(1, 1)
        with self.assertRaises(ValueError):
            self.c8 = Card(1, 'z')

    def test_invalidInitRank(self):
        """
        Unit test for Card.__init__ Rank errors
        """
        print("test_Card.invalidInitRank")
        with self.assertRaises(TypeError):
            self.c5 = Card('a', 'c')
        with self.assertRaises(ValueError):
            self.c7 = Card(-1, 'c')

    def test_getRank(self):
        """
        Unit test for Card.getRank
        """
        print("test_Card.getRank")
        self.assertEqual(self.c1.getRank(), 5)
        self.assertEqual(self.c2.getRank(), 1)
        self.assertEqual(self.c3.getRank(), 13)
        self.assertEqual(self.c4.getRank(), 9)

    def test_getSuit(self):
        """
        Unit test for Card.getSuit
        """
        print("test_Card.getSuit")
        self.assertEqual(self.c1.getSuit(), 'c')
        self.assertEqual(self.c2.getSuit(), 's')
        self.assertEqual(self.c3.getSuit(), 'd')
        self.assertEqual(self.c4.getSuit(), 'h')

    def test_bjValue(self):
        """
        Unit test for Card.bjValue
        """
        print("test_Card.bjValue")
        self.assertEqual(self.c1.bjValue(), 5)
        self.assertEqual(self.c2.bjValue(), 1)
        self.assertEqual(self.c3.bjValue(), 10)
        self.assertEqual(self.c4.bjValue(), 9)

    def test_str(self):
        """
        Unit test for Card.__str__
        """
        print("test_Card.str")
        self.assertEqual(str(self.c1), "Five of Clubs")
        self.assertEqual(str(self.c2), "Ace of Spades")
        self.assertEqual(str(self.c3), "King of Diamonds")
        self.assertEqual(str(self.c4), "Nine of Hearts")

class TestHand(unittest.TestCase):

    def setUp(self):
        """
        setUp function for Hand unit tests
        """
        # Randomly Generated Hand Objects for Testing
        self.h1 = Hand(3)
        self.h2 = Hand(2)
        self.h3 = Hand(10)
        # Manually Generated Hand Objects for Testing
        self.h4 = Hand(0)
        self.h4.addTestCard(Card(5, 'c'))
        self.h4.addTestCard(Card(1, 's'))
        self.h4.addTestCard(Card(13, 'd'))
        self.h4.addTestCard(Card(9, 'h'))
        self.h5 = Hand(0)
        self.h5.addTestCard(Card(5, 'c'))
        self.h5.addTestCard(Card(5, 'c'))
        self.h6 = Hand(0)
        self.h6.addTestCard(Card(13, 'd'))
        self.h6.addTestCard(Card(13, 'd'))
        self.h7 = Hand(0)

    def test_invalidInit(self):
        """
        Unit test for Hand.__init__
        """
        print("test_Hand.invalidInit")
        with self.assertRaises(TypeError):
            self.h8 = Hand('a')

    def test_generateRandomCard(self):
        """
        Unit test for Hand.generateRandomCard
        """
        print("test_Hand.generateRandomCard")
        self.c5 = Hand(0).generateRandomCard()
        self.assertTrue(1 <= self.c5.getRank() <= 13 and self.c5.getSuit() in 'schd')
        self.c6 = Hand(0).generateRandomCard()
        self.assertTrue(1 <= self.c6.getRank() <= 13 and self.c6.getSuit() in 'schd')
        self.c7 = Hand(0).generateRandomCard()
        self.assertTrue(1 <= self.c7.getRank() <= 13 and self.c7.getSuit() in 'schd')
        self.c8 = Hand(0).generateRandomCard()
        self.assertTrue(1 <= self.c8.getRank() <= 13 and self.c8.getSuit() in 'schd')

    def test_hitMe(self):
        """
        Unit test for Hand.hitMe
        """
        print("test_Hand.hitMe")
        self.h1.hitMe()
        self.assertEqual(len(self.h1), 4)
        self.h2.hitMe()
        self.assertEqual(len(self.h2), 3)
        self.h3.hitMe()
        self.assertEqual(len(self.h3), 11)
        self.h3.hitMe()
        self.assertEqual(len(self.h3), 12)
        self.h4.hitMe()
        self.assertEqual(len(self.h4), 5)
        self.h5.hitMe()
        self.assertEqual(len(self.h5), 3)
        self.h6.hitMe()
        self.assertEqual(len(self.h6), 3)
        self.h7.hitMe()
        self.assertEqual(len(self.h7), 1)

    def test_bjValue(self):
        """
        Unit test for Hand.bjValue
        """
        print("test_Hand.bjValue")
        self.assertEqual(self.h4.bjValue(), 25)
        self.assertEqual(self.h5.bjValue(), 10)
        self.assertEqual(self.h6.bjValue(), 20)
        self.assertEqual(self.h7.bjValue(), 0)

    def test_str(self):
        """
        Unit test for Hand.__str__
        """
        print("test_Hand.str")
        self.assertEqual(str(self.h4), "Five of Clubs\nAce of Spades\nKing of Diamonds\nNine of Hearts\n")
        self.assertEqual(str(self.h5), "Five of Clubs\nFive of Clubs\n")
        self.assertEqual(str(self.h6), "King of Diamonds\nKing of Diamonds\n")
        self.assertEqual(str(self.h7), "")


if __name__ == '__main__':
    unittest.main()

"""
===== OUTPUT =====
...........
test_Card.bjValue
test_Card.getRank
test_Card.getSuit
test_Card.invalidInitRank
test_Card.invalidInitSuit
test_Card.str
test_Hand.bjValue
test_Hand.generateRandomCard
test_Hand.hitMe
----------------------------------------------------------------------
test_Hand.invalidInit
test_Hand.str
Ran 11 tests in 0.001s

OK
"""



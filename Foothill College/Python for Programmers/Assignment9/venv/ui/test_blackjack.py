"""
This program contains all units tests for the Card, Hand, and HandFile classes.
"""

import unittest

from card import Card
from hand import Hand
from handfile_extracredit import HandFile


class TestCard(unittest.TestCase):

    def setUp(self):
        """setUp function for Card unit tests """
        self.c1 = Card(5, 'c')
        self.c2 = Card(1, 's')
        self.c3 = Card(13, 'd')
        self.c4 = Card(9, 'h')

    def test_invalidInitSuit(self):
        """ Unit test for Card.__init__ Suit errors """
        with self.assertRaises(TypeError):
            self.c6 = Card(1, 1)
        with self.assertRaises(ValueError):
            self.c8 = Card(1, 'z')

    def test_invalidInitRank(self):
        """ Unit test for Card.__init__ Rank errors """
        with self.assertRaises(TypeError):
            self.c5 = Card('a', 'c')
        with self.assertRaises(ValueError):
            self.c7 = Card(-1, 'c')

    def test_getRank(self):
        """ Unit test for Card.getRank """
        self.assertEqual(self.c1.getRank(), 5)
        self.assertEqual(self.c2.getRank(), 1)
        self.assertEqual(self.c3.getRank(), 13)
        self.assertEqual(self.c4.getRank(), 9)

    def test_getSuit(self):
        """ Unit test for Card.getSuit """
        self.assertEqual(self.c1.getSuit(), 'c')
        self.assertEqual(self.c2.getSuit(), 's')
        self.assertEqual(self.c3.getSuit(), 'd')
        self.assertEqual(self.c4.getSuit(), 'h')

    def test_bjValue(self):
        """ Unit test for Card.bjValue """
        self.assertEqual(self.c1.bjValue(), 5)
        self.assertEqual(self.c2.bjValue(), 1)
        self.assertEqual(self.c3.bjValue(), 10)
        self.assertEqual(self.c4.bjValue(), 9)

    def test_str(self):
        """ Unit test for Card.__str__ """
        self.assertEqual(str(self.c1), "Five of Clubs")
        self.assertEqual(str(self.c2), "Ace of Spades")
        self.assertEqual(str(self.c3), "King of Diamonds")
        self.assertEqual(str(self.c4), "Nine of Hearts")


class TestHand(unittest.TestCase):

    def setUp(self):
        """ setUp function for Hand unit tests """
        # Randomly Generated Hand Objects for Testing
        self.h1 = Hand(3)
        self.h2 = Hand(2)
        self.h3 = Hand(10)
        # Manually Generated Hand Objects for Testing
        self.h4 = Hand(0)
        self.h4.addCard(Card(5, 'c'))
        self.h4.addCard(Card(1, 's'))
        self.h4.addCard(Card(13, 'd'))
        self.h4.addCard(Card(9, 'h'))
        self.h5 = Hand(0)
        self.h5.addCard(Card(5, 'c'))
        self.h5.addCard(Card(5, 'c'))
        self.h6 = Hand(0)
        self.h6.addCard(Card(13, 'd'))
        self.h6.addCard(Card(13, 'd'))
        self.h7 = Hand(0)

    def test_invalidInit(self):
        """ Unit test for Hand.__init__ """
        with self.assertRaises(TypeError):
            self.h8 = Hand('a')

        self.h8 = Hand(3)
        self.h8str = str(self.h8)
        self.h9 = Hand(2)
        self.assertEqual(self.h8str, str(self.h8)) # to make sure that the creation of h9 didn't effect h8

    def test_generateRandomCard(self):
        """ Unit test for Hand.generateRandomCard """
        self.c5 = Hand(0).generateRandomCard()
        self.assertTrue(1 <= self.c5.getRank() <= 13 and self.c5.getSuit() in 'schd')
        self.c6 = Hand(0).generateRandomCard()
        self.assertTrue(1 <= self.c6.getRank() <= 13 and self.c6.getSuit() in 'schd')
        self.c7 = Hand(0).generateRandomCard()
        self.assertTrue(1 <= self.c7.getRank() <= 13 and self.c7.getSuit() in 'schd')
        self.c8 = Hand(0).generateRandomCard()
        self.assertTrue(1 <= self.c8.getRank() <= 13 and self.c8.getSuit() in 'schd')

    def test_addCard(self):
        """ Unit test for Hand.addCard."""
        self.assertEqual(len(self.h6), 2)
        self.h6.addCard(Card(5, 'c'))
        self.assertEqual(len(self.h6), 3)
        self.assertTrue(self.h6[2].getRank() == 5 and self.h6[2].getSuit() == 'c')
        self.assertEqual(len(self.h7), 0)
        self.h7.addCard(Card(9, 's'))
        self.assertEqual(len(self.h7), 1)
        self.assertTrue(self.h7[0].getRank() == 9 and self.h7[0].getSuit() == 's')

    def test_hitMe(self):
        """ Unit test for Hand.hitMe """
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
        """ Unit test for Hand.bjValue """
        self.assertEqual(self.h4.bjValue(), 25)
        self.assertEqual(self.h5.bjValue(), 10)
        self.assertEqual(self.h6.bjValue(), 20)
        self.assertEqual(self.h7.bjValue(), 0)

    def test_str(self):
        """ Unit test for Hand.__str__ """
        self.assertEqual(str(self.h4), "Five of Clubs\nAce of Spades\nKing of Diamonds\nNine of Hearts\n")
        self.assertEqual(str(self.h5), "Five of Clubs\nFive of Clubs\n")
        self.assertEqual(str(self.h6), "King of Diamonds\nKing of Diamonds\n")
        self.assertEqual(str(self.h7), "")


class TestHandFile(unittest.TestCase):

    def test_handFileToHandObject(self):
        """ Unit test for HandFile.handFileToHandObject. """
        self.h1 = Hand(0)
        self.h1.addCard(Card(5, 'c'))
        self.h1.addCard(Card(1, 's'))
        self.h1.addCard(Card(13, 'd'))
        self.h1.addCard(Card(9, 'h'))
        self.hf1 = HandFile(self.h1)
        self.assertEqual(str(self.hf1.handFileToHandObject()), str(self.h1))

    def test_getCardFromStr(self):
        """ Unit test for Handfile.getCardFromStr. """
        self.assertEqual(str(HandFile.getCardFromStr(HandFile(Hand(0)), "Eight of Spades")), str(Card(8, 's')))

    def test_strToCardValue(self):
        """ Unit test for HandFile.strToCardValue."""
        self.assertEqual(HandFile.strToCardValue(HandFile(Hand(0)), "Eight"), 8)
        self.assertEqual(HandFile.strToCardValue(HandFile(Hand(0)), "Ace"), 1)
        self.assertEqual(HandFile.strToCardValue(HandFile(Hand(0)), "Queen"), 12)

    def test_runMethodOnReadBackHandObject(self):
        """ Test that read-back Hand object is a valid hand object """
        self.h1 = Hand(1)
        self.hf1 = HandFile(self.h1)
        self.h2 = self.hf1.handFileToHandObject()
        self.assertTrue(self.h2[0].getSuit() in 'schd' and 1 <= self.h2[0].getRank() <= 13)


if __name__ == '__main__':
    unittest.main(verbosity=2)

"""
===== OUTPUT =====
test_bjValue (__main__.TestCard)
Unit test for Card.bjValue ... ok
test_getRank (__main__.TestCard)
Unit test for Card.getRank ... ok
test_getSuit (__main__.TestCard)
Unit test for Card.getSuit ... ok
test_invalidInitRank (__main__.TestCard)
Unit test for Card.__init__ Rank errors ... ok
test_invalidInitSuit (__main__.TestCard)
Unit test for Card.__init__ Suit errors ... ok
test_str (__main__.TestCard)
Unit test for Card.__str__ ... ok
test_addCard (__main__.TestHand)
Unit test for Hand.addCard. ... ok
test_bjValue (__main__.TestHand)
Unit test for Hand.bjValue ... ok
test_generateRandomCard (__main__.TestHand)
Unit test for Hand.generateRandomCard ... ok
test_hitMe (__main__.TestHand)
Unit test for Hand.hitMe ... ok
test_invalidInit (__main__.TestHand)
Unit test for Hand.__init__ ... ok
test_str (__main__.TestHand)
Unit test for Hand.__str__ ... ok
test_getCardFromStr (__main__.TestHandFile)
Unit test for Handfile.getCardFromStr. ... ok
test_handFileToHandObject (__main__.TestHandFile)
Unit test for HandFile.handFileToHandObject. ... ok
test_runMethodOnReadBackHandObject (__main__.TestHandFile)
Test that read-back Hand object is a valid hand object ... ok
test_strToCardValue (__main__.TestHandFile)
Unit test for HandFile.strToCardValue. ... ok

----------------------------------------------------------------------
Ran 16 tests in 0.002s

OK
"""

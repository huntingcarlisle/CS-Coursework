import unittest

from hand import Hand
from card import Card

class TestHand(unittest.TestCase):

    def setUp(self):
        ## Card Objects for Testing
        self.c1 = Card(5, 'c')
        self.c2 = Card(1, 's')
        self.c3 = Card(13, 'd')
        self.c4 = Card(9, 'h')
        ## Hand Objects for Testing
        self.h1 = Hand(3)
        self.h2 = Hand(2)
        self.h3 = Hand(10)
        self.h4 = Hand()
        self.h4.addTestCard(self.c1)
        self.h4.addTestCard(self.c2)
        self.h4.addTestCard(self.c3)
        self.h4.addTestCard(self.c4)
        self.h5 = Hand()
        self.h5.addTestCard(self.c1)
        self.h5.addTestCard(self.c1)

    def test_invalidInit(self):
        print("test_invalidInit")
        with self.assertRaises(TypeError):
            self.h6 = Hand('a')

    def test_generateRandomCard(self):
        self.h7 = Hand(1)
        self.assertTrue(1 <= self.h7[0].getRank() <= 13 and self.h7[0].getSuit() in 'schd')

    def test_hitMe(self):
        print("test_hitMe")
        self.h1.hitMe()
        self.assertEqual(len(self.h1), 4)
        self.h2.hitMe()
        self.assertEqual(len(self.h2), 3)
        self.h3.hitMe()
        self.assertEqual(len(self.h3), 11)
        self.h3.hitMe()
        self.assertEqual(len(self.h3), 12)

    def test_bjValue(self):
        print("test_bjValue")
        self.assertEqual(self.h4.bjValue(), 25)
        self.assertEqual(self.h5.bjValue(), 10)

    def test_str(self):
        print("test_str")
        self.assertEqual(str(self.h4), "Five of Clubs\nAce of Spades\nKing of Diamonds\nNine of Hearts\n")
        self.assertEqual(str(self.h5), "Five of Clubs\nFive of Clubs\n")


if __name__ == '__main__':
    unittest.main()




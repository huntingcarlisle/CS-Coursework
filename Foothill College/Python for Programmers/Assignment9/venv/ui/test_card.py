import unittest

from card import Card


class TestCard(unittest.TestCase):

    def setUp(self):
        self.c1 = Card(5, 'c')
        self.c2 = Card(1, 's')
        self.c3 = Card(13, 'd')
        self.c4 = Card(9, 'h')

    def test_invalidInitSuit(self):
        print("test_invalidInitSuit")
        with self.assertRaises(TypeError):
            self.c6 = Card(1, 1)
        with self.assertRaises(ValueError):
            self.c8 = Card(1, 'z')

    def test_invalidInitRank(self):
        print("test_invalidInitRank")
        with self.assertRaises(TypeError):
            self.c5 = Card('a', 'c')
        with self.assertRaises(ValueError):
            self.c7 = Card(-1, 'c')

    def test_getRank(self):
        print("test_getRank")
        self.assertEqual(self.c1.getRank(), 5)
        self.assertEqual(self.c2.getRank(), 1)
        self.assertEqual(self.c3.getRank(), 13)
        self.assertEqual(self.c4.getRank(), 9)

    def test_getSuit(self):
        print("test_getSuit")
        self.assertEqual(self.c1.getSuit(), 'c')
        self.assertEqual(self.c2.getSuit(), 's')
        self.assertEqual(self.c3.getSuit(), 'd')
        self.assertEqual(self.c4.getSuit(), 'h')

    def test_bjValue(self):
        print("test_bjValue")
        self.assertEqual(self.c1.bjValue(), 5)
        self.assertEqual(self.c2.bjValue(), 1)
        self.assertEqual(self.c3.bjValue(), 10)
        self.assertEqual(self.c4.bjValue(), 9)

    def test_str(self):
        print("test_str")
        self.assertEqual(str(self.c1), "Five of Clubs")
        self.assertEqual(str(self.c2), "Ace of Spades")
        self.assertEqual(str(self.c3), "King of Diamonds")
        self.assertEqual(str(self.c4), "Nine of Hearts")


if __name__ == '__main__':
    unittest.main()

# ===== OUTPUT =====
# ......
# test_bjValue
# ----------------------------------------------------------------------
# test_getRank
# Ran 6 tests in 0.001s
# test_getSuit
#
# test_invalidInitRank
# OK
# test_invalidInitSuit
# test_str

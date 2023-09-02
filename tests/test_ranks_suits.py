import unittest

from utils.constants import RANKS, SUITS

class TestRanksSuits(unittest.TestCase):
    def test_ranks(self):
        self.assertEqual(RANKS, ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])

    def test_suits(self):
        self.assertEqual(SUITS, ["Hearts", "Diamonds", "Spades", "Clubs"])

if __name__ == '__main__':
    unittest.main()
    
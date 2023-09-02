import unittest
import sys
sys.path.append('..')

from core.card import Card
from core.deck import Deck
from utils.constants import RANKS, SUITS

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_52_cards(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_reshuffle_if_needed(self):
        self.deck.cards = []
        self.deck.reshuffle_if_needed()
        self.assertEqual(len(self.deck.cards), 52)

    def test_deal_raises_exception(self):
        self.deck.cards = []
        with self.assertRaises(Exception):
            self.deck.deal()

    def test_shuffle_cards(self):
        self.deck.shuffle_cards()
        self.assertNotEqual(self.deck.cards, [Card(rank, suit) for rank in RANKS for suit in SUITS])

if __name__ == '__main__':
    unittest.main()
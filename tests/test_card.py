import unittest

from core.card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.heart_card = Card("A", "Hearts")
        self.number_card = Card("2", "Spades")

    def test_card_rank(self):
        self.assertEqual(self.heart_card.rank, "A")

    def test_card_suit(self):
        self.assertEqual(self.heart_card.suit, "Hearts")

    def test_card_str(self):
        self.assertEqual(str(self.heart_card), "A ♥")

    def test_card_str_not_equal(self):
        self.assertNotEqual(str(self.heart_card), "A ♠")

    def test_card_str_number(self):
        self.assertEqual(str(self.number_card), "2 ♠")

    def test_card_str_number_not_equal(self):
        self.assertNotEqual(str(self.number_card), "2 ♥")
    
if __name__ == '__main__':
    unittest.main()
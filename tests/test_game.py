import unittest

from core.game import Game
from core.card import Card
from core.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        player = Player("Player")
        dealer = Player("Dealer")
        self.game = Game(player, dealer)

    def test_player_reset(self):
        self.game.player.add_card(Card("A", "Hearts"))
        self.game.player.add_card(Card("2", "Spades"))
        self.game.player.reset()
        self.assertEqual(self.game.player.hand, [])

    def test_player_hit_card(self):
        self.game.player_hit_card(self.game.player)
        self.assertEqual(len(self.game.player.hand), 1)

    def test_player_hit_blackjack(self):
        self.game.player.value = 20
        self.assertEqual(self.game.player_hit_card(self.game.player), False)

    def test_player_stay(self):
        self.assertEqual(self.game.player_stay(), False)

    def test_player_exceed_21(self):
        self.game.player.score = 10
        self.game.player.value = 23
        self.game.determine_winner()
        self.assertEqual(self.game.player.score, 0)

    def test_player_equal_dealer_20(self):
        self.game.player.value = 20
        self.game.dealer.value = 20
        self.game.player.score = 10
        self.game.determine_winner()
        self.assertEqual(self.game.player.score, 10)

    def test_player_equal_dealer_21(self):
        self.game.player.value = 21
        self.game.dealer.value = 21
        self.game.player.score = 10
        self.game.determine_winner()
        self.assertEqual(self.game.player.score, 10)

    def test_player_equal_dealer_22(self):
        self.game.player.value = 22
        self.game.dealer.value = 22
        self.game.player.score = 10
        self.game.determine_winner()
        self.assertEqual(self.game.player.score, 0)

    def test_player_blackjack(self):
        self.game.player.value = 21
        self.game.player.hand = [Card("A", "Hearts"), Card("K", "Hearts")]
        self.game.player.score = 10
        self.game.determine_winner()
        self.assertEqual(self.game.player.score, 25)

    def test_player_lose(self):
        self.game.player.value = 20
        self.game.dealer.value = 21
        self.game.player.score = 10
        self.game.determine_winner()
        self.assertEqual(self.game.player.score, 0)

    def test_player_win(self):
        self.game.player.value = 21
        self.game.dealer.value = 20
        self.game.player.score = 10
        self.game.determine_winner()
        self.assertEqual(self.game.player.score, 20)

    
if __name__ == '__main__':
    unittest.main()
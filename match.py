from player import Player
from game import Game

class Match:
    def __init__(self):
        self.player = Player("player 1")
        self.dealer = Player("dealer")

    def start(self):
        while self.take_user_game_input() == "y":
            game = Game(self.player, self.dealer)
            game.start()

        print(f"Your final score is {self.player.score}!")

    def take_user_game_input(self):
        return input(f"Would you like to start a game? Y/N\n >>> ").lower()
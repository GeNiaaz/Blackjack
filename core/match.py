from core.player import Player
from core.game import Game
from utils.constants import USER_GAME_INPUT_FIRST_GAME_MSG, USER_GAME_INPUT_MSG, USER_INPUT_CARD_INVALID_MSG
from interface.ui import Ui

class Match:
    def __init__(self):
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    def start(self):
        is_game_on = True
        is_first_game = True
        game = Game(self.player, self.dealer)
        while is_game_on:
            user_input_game = self.take_user_game_input(is_first_game)
            game.reset_players()
            match user_input_game:
                case 'y':
                    game.start()
                    is_first_game = False
                case 'n':
                    is_game_on = False
                case _:
                    Ui.clear_screen()
                    Ui.user_input_invalid()

        Ui.skip_line()
        Ui.display_game_end_msg(self.player)

    def take_user_game_input(self, is_first_game: bool) -> str:
        if is_first_game:
            return input(USER_GAME_INPUT_FIRST_GAME_MSG).lower()
        else:
            return input(USER_GAME_INPUT_MSG).lower()
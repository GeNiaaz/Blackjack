from core.player import Player
from core.round import Round
from utils.constants import USER_INPUT_FIRST_ROUND_MSG, USER_ROUND_INPUT_MSG
from interface.ui import Ui

class Game:
    def __init__(self):
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    def start(self) -> None:
        is_game_on = True
        is_first_game = True
        game = Round(self.player, self.dealer)
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
            return input(USER_INPUT_FIRST_ROUND_MSG).lower()
        else:
            return input(USER_ROUND_INPUT_MSG).lower()
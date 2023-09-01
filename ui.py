from player import Player
from string_builder import StringBuilder
from constants import USER_INPUT_CARD_MSG, USER_INPUT_CARD_INVALID_MSG, USER_GAME_END_MSG, \
CARDS_RESHUFFLED, SUITS_SYMBOLS, PLAYER_EQUAL_TO_DEALER_MSG, PLAYER_BLACKJACK_MSG, \
PLAYER_LOSES_MSG, PLAYER_WINS_MSG
import os

class Ui:
    def __display_to_terminal(output: str) -> None:
        print(output)

    def clear_screen() -> None:
        # os.system('clear')
        ...

    def display_player_hand(player: Player) -> str:
        output = StringBuilder()
        
        output.add(f"{player.name}'s Hand: ")
        for card in player.hand:
            output.add(f"{card.rank} {SUITS_SYMBOLS[card.suit]} | ")

        output.add(f"total value: {player.value}")

        Ui.__display_to_terminal(output)

    def display_initial_dealer_hand(dealer: Player) -> str:
        output = StringBuilder()
        
        output.add(f"{dealer.name}'s Hand: ")
        first_card = dealer.hand[0]
        output.add(f"{first_card.rank} {SUITS_SYMBOLS[first_card.suit]} | ")
        output.add("X X |")

        Ui.__display_to_terminal(output)

    def take_user_input_card() -> str:
        return input(USER_INPUT_CARD_MSG).lower()
    
    def user_input_invalid() -> None:
        output = StringBuilder()

        output.add(USER_INPUT_CARD_INVALID_MSG)
        Ui.__display_to_terminal(output)

    def display_player_score(player: Player) -> str:
        output = StringBuilder()

        output.add(f"{player.name}'s Score: {player.score}")
        Ui.__display_to_terminal(output)

    def display_game_end_msg(player: Player) -> str:
        output = StringBuilder()

        output.add(f"{player.name}'s ")
        output.add(USER_GAME_END_MSG)
        output.add(f"{player.score}")
        Ui.__display_to_terminal(output)

    def display_cards_reshuffled() -> str:
        output = StringBuilder()

        output.add(CARDS_RESHUFFLED)
        Ui.__display_to_terminal(output)

    def skip_line():
        print("")

    def display_player_exceed_21_msg() -> str:
        output = StringBuilder()

        output.add(PLAYER_LOSES_MSG)
        Ui.__display_to_terminal(output)

    def display_player_equal_to_dealer_msg() -> str:
        output = StringBuilder()

        output.add(PLAYER_EQUAL_TO_DEALER_MSG)
        Ui.__display_to_terminal(output)

    def display_player_blackjack_msg() -> str:
        output = StringBuilder()

        output.add(PLAYER_BLACKJACK_MSG)
        Ui.__display_to_terminal(output)

    def display_dealer_exceed_21_msg() -> str:
        output = StringBuilder()

        output.add(PLAYER_WINS_MSG)
        Ui.__display_to_terminal(output)

    def display_player_greater_than_dealer_msg() -> str:
        output = StringBuilder()

        output.add(PLAYER_WINS_MSG)
        Ui.__display_to_terminal(output)

    def display_dealer_greater_than_player_msg() -> str:
        output = StringBuilder()

        output.add(PLAYER_LOSES_MSG)
        Ui.__display_to_terminal(output)

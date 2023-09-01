from player import Player
from string_builder import StringBuilder

class Ui:
    def __display_to_output(output: str):
        print(output)

    def display_player_hand(player: Player) -> str:
        output = StringBuilder()
        
        output.add(f"{player.name}'s Hand: ")
        for card in player.hand:
            output.add(f"{card.rank} of {card.suit}, ")

        Ui.__display_to_output(output)

    def display_initial_dealer_hand(dealer: Player) -> str:
        output = StringBuilder()
        
        output.add(f"{dealer.name}'s initial Hand: ")
        first_card = dealer.hand[0]
        output.add(f"{first_card.rank} of {first_card.suit}, ")
        output.add("Hidden Card")

        Ui.__display_to_output(output)
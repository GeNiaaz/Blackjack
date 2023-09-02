from core.player import Player
from core.deck import Deck
from utils.constants import DEALER_HIT_THRESHOLD, BLACKJACK_VALUE, POINTS_DEFEAT, POINTS_VICTORY, POINTS_BLACKJACK_VICTORY, NUM_CARDS_FOR_BLACKJACK
from interface.ui import Ui

class Round:
    def __init__(self, player, dealer):
        self.deck = Deck()
        self.player = player
        self.dealer = dealer
        self.reset_players()

    def reset_players(self):
        self.player.reset()
        self.dealer.reset()

    def start(self):
        # deal 2 cards to dealer
        self.dealer.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())

        # deal 2 cards to player
        self.player.add_card(self.deck.deal())
        self.player.add_card(self.deck.deal())

        # player turns
        player_has_turn = self.player.value < BLACKJACK_VALUE
        while player_has_turn:
            Ui.clear_screen()
            Ui.skip_line()
            Ui.display_initial_dealer_hand(self.dealer)
            Ui.display_player_hand(self.player)
            Ui.skip_line()
            
            player_choice = Ui.take_user_input_card()
            is_player_input_valid = False
            while not is_player_input_valid:
                match player_choice:
                    case "y":
                        player_has_turn = self.player_hit_card(self.player)
                        is_player_input_valid = True
                    case "n":
                        player_has_turn = self.player_stay()
                        is_player_input_valid = True
                    case _:
                        Ui.user_input_invalid()
                        player_choice = Ui.take_user_input_card()
            
        self.dealer_turn()
        self.determine_winner()
        Ui.skip_line()

    def player_hit_card(self, player: Player) -> bool:
        player.add_card(self.deck.deal())
        return not self.player.value >= BLACKJACK_VALUE

    def player_stay(self):
        return False

    def dealer_turn(self):
        if self.player.value > BLACKJACK_VALUE:
            return
        while self.dealer.value < DEALER_HIT_THRESHOLD:
            self.dealer.add_card(self.deck.deal())
        
    def determine_winner(self):
        Ui.clear_screen()
        Ui.skip_line()
        Ui.display_player_hand(self.dealer)
        Ui.display_player_hand(self.player)
        Ui.skip_line()
        
        if self.player.value > BLACKJACK_VALUE:
            self.player_exceed_21()
        elif self.dealer.value == self.player.value:
            self.player_equal_to_dealer()
        elif self.player.value == BLACKJACK_VALUE and self.player.get_num_cards_in_hand() == NUM_CARDS_FOR_BLACKJACK:
            self.player_blackjack()
        elif self.dealer.value > BLACKJACK_VALUE:
            self.dealer_exceed_21()
        elif self.player.value > self.dealer.value:
            self.player_greater_than_dealer()
        elif self.dealer.value > self.player.value:
            self.dealer_greater_than_player()
        else:
            ...

        Ui.display_player_score(self.player)

    def player_exceed_21(self):
        Ui.display_player_exceed_21_msg()
        self.player.score -= POINTS_DEFEAT

    def player_equal_to_dealer(self):
        Ui.display_player_equal_to_dealer_msg()
    
    def player_blackjack(self):
        Ui.display_player_blackjack_msg()
        self.player.score += POINTS_BLACKJACK_VICTORY

    def dealer_exceed_21(self):
        Ui.display_dealer_exceed_21_msg()
        self.player.score += POINTS_VICTORY

    def player_greater_than_dealer(self):
        Ui.display_player_greater_than_dealer_msg()
        self.player.score += POINTS_VICTORY

    def dealer_greater_than_player(self):
        Ui.display_dealer_greater_than_player_msg()
        self.player.score -= POINTS_DEFEAT

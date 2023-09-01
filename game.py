from player import Player
from deck import Deck
from constants import DEALER_HIT_THRESHOLD
from ui import Ui

class Game:
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
        while True:
            Ui.display_player_hand(self.player)
            Ui.display_initial_dealer_hand(self.dealer)
            
            player_choice = input("Do you want to Hit or Stay? \n>>> ").lower()
            if player_choice == "hit":
                self.player.add_card(self.deck.deal())
                if self.player.value > 21:
                    break
            elif player_choice == "stay":
                break
            
        self.dealer_turn()
        self.determine_winner()


    def dealer_turn(self):
        if self.player.value > 21:
            return
        while self.dealer.value < DEALER_HIT_THRESHOLD:
            self.dealer.add_card(self.deck.deal())
        
    def determine_winner(self):
        Ui.display_player_hand(self.player)
        Ui.display_player_hand(self.dealer)
        
        if self.player.value > 21:
            print(f"Player got {self.player.value} and loses! \nPlayer loses 10 points")
            self.player.score -= 10
        elif self.dealer.value == self.player.value:
            print("It's a Push!")
        elif self.player.value == 21:
            print(f"Player scores Blackjack and wins! \nPlayer gains 15 points")
            self.player.score += 15
        elif self.dealer.value > 21:
            print(f"Dealer got {self.dealer.value} and player wins! \nPlayer gains 10 points")
        elif self.player.value > self.dealer.value:
            print(f"Player got {self.player.value} while dealer got {self.dealer.value} and player wins! \nPlayer gains 10 points")
            self.player.score += 10
        elif self.dealer.value > self.player.value:
            print(f"Dealer got {self.dealer.value} while player got {self.player.value} and wins! \nPlayer loses 10 points")
            self.player.score -= 10
        else:
            print("It's a Push!")

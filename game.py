from player import Player
from deck import Deck
from constants import DEALER_HIT_THRESHOLD

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player()

    def start(self):
        # deal 2 cards to dealer
        self.dealer.add_card(self.deck.deal())
        self.dealer.add_card(self.deck.deal())

        # deal 2 cards to player
        self.player.add_card(self.deck.deal())
        self.player.add_card(self.deck.deal())

        # player turns
        while True:
            print("Player's Hand:", [card.rank + " of " + card.suit for card in self.player.hand])
            print("Dealer's Hand:", [self.dealer.hand[0].rank + " of " + self.dealer.hand[0].suit, "Hidden Card"])
            
            player_choice = input("Do you want to Hit or Stay? ").lower()
            if player_choice == "hit":
                self.player.add_card(self.deck.deal())
                if self.player.score > 21:
                    break
            elif player_choice == "stay":
                break
            
        self.dealer_turn()
        self.determine_winner()


    def dealer_turn(self):
        if self.player.score > 21:
            return
        while self.dealer.score < DEALER_HIT_THRESHOLD:
            self.dealer.add_card(self.deck.deal())

    def display_hand(self,):
        print("Player's Hand:", [card.rank + " of " + card.suit for card in self.player.hand])
        print("Dealer's Hand:", [card.rank + " of " + card.suit for card in self.dealer.hand])

        
    def determine_winner(self):
        # self.display_hand(self.player)
        # self.display_hand(self.dealer)
        self.display_hand()
        
        if self.player.score > 21:
            print("Player scores {self.player.score} and loses! \nPlayer loses 10 points")
            self.player.score -= 10
        elif self.dealer.score < 21 and self.dealer.score < self.player.score:
            print("Player scores {self.player.score} and wins! \nPlayer gains 10 points")
            self.player.score += 10
        elif self.dealer.score == 21 and self.dealer.score < self.player.score:
            print("Player scores Blackjack and wins! \nPlayer gains 15 points")
            self.player.score += 15
        elif self.dealer.score > self.player.score:
            print("Dealer scores {self.dealer.score} and wins! \nPlayer loses 10 points")
            self.player.score -= 10
        else:
            print("It's a Push!")
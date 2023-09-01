import random
from constants import RANKS, SUITS, NUMBER_OF_CARDS, SHUFFLE_THRESHOLD
from card import Card
from ui import Ui

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        self.shuffle_cards()
    
    def shuffle_cards(self):
        random.shuffle(self.cards)

    def reshuffle_if_needed(self):
        if len(self.cards) <= SHUFFLE_THRESHOLD:
            self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
            self.shuffle_cards()
            Ui.display_cards_reshuffled()

    def deal(self):
        if self.cards:
            drawn_card = self.cards.pop()
            self.reshuffle_if_needed()
            return drawn_card
        else:
            return None
import random
from utils.constants import RANKS, SUITS, SHUFFLE_THRESHOLD
from core.card import Card
from interface.ui import Ui

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        self.shuffle_cards()
    
    def shuffle_cards(self) -> None:
        random.shuffle(self.cards)

    def reshuffle_if_needed(self) -> None:
        if len(self.cards) <= SHUFFLE_THRESHOLD:
            self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
            self.shuffle_cards()
            Ui.display_cards_reshuffled()

    def deal(self) -> Card:
        if self.cards:
            drawn_card = self.cards.pop()
            self.reshuffle_if_needed()
            return drawn_card
        else:
            raise Exception("Deck reshuffling failed.")
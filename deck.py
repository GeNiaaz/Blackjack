import random
from constants import RANKS, SUITS, NUMBER_OF_CARDS, SHUFFLE_THRESHOLD
from card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        self.shuffle_cards()
    
    def shuffle_cards(self):
        if len(self.cards) < SHUFFLE_THRESHOLD or len(self.cards) == NUMBER_OF_CARDS:
            random.shuffle(self.cards)

    def deal(self):
        if self.cards:
            self.shuffle_cards()
            return self.cards.pop()
        else:
            return None
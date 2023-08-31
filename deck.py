import random
from constants import RANKS, SUITS
from card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        random.shuffle(self.cards)
    
    def deal(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None
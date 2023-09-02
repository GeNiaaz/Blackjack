from utils.constants import SUITS_SYMBOLS

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.rank} {SUITS_SYMBOLS[self.suit]}"
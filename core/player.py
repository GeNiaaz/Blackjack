from utils.constants import ROYALTY_SUITS, ROYALTY_VALUE, ACE_VALUE, ACE_THRESHOLD, ACE_REMAINING_VALUE, ACE_SUIT
from core.card import Card

class Player:
    def __init__(self, name: str):
        self.hand = []
        self.value = 0
        self.score = 0
        self.name = name

    def reset(self) -> None:
        self.hand = []
        self.value = 0
        self.ace_present = False

    def get_num_cards_in_hand(self) -> int:
        return len(self.hand)
    
    # upper bounded at 50, no point using double ended list
    def add_card(self, card: Card) -> None:
        self.hand.append(card)
        self.calculate_value(card)

    def calculate_value(self, card: Card) -> None:
        drawn_card_rank = card.rank
        if drawn_card_rank.isdigit():
            self.value += int(drawn_card_rank)
        elif drawn_card_rank in ROYALTY_SUITS:
            self.value += ROYALTY_VALUE
        elif drawn_card_rank in ACE_SUIT:
            self.value += ACE_VALUE
            if self.value < ACE_THRESHOLD:
                self.value += ACE_REMAINING_VALUE

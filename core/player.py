from utils.constants import ROYALTY_SUITS, ROYALTY_VALUE, ACE_VALUE, ACE_THRESHOLD, ACE_REMAINING_VALUE, ACE_SUIT

class Player:
    def __init__(self, name):
        self.hand = []
        self.value = 0
        self.score = 0
        self.name = name

    def reset(self):
        self.hand = []
        self.value = 0
        self.ace_present = False

    def get_num_cards_in_hand(self):
        return len(self.hand)
    
    # upper bounded at 50, no point using double ended list
    def add_card(self, card):
        self.hand.append(card)
        self.calculate_value(card)

    def calculate_value(self, card):
        drawn_card_rank = card.rank
        if drawn_card_rank.isdigit():
            self.value += int(drawn_card_rank)
        elif drawn_card_rank in ROYALTY_SUITS:
            self.value += ROYALTY_VALUE
        elif drawn_card_rank in ACE_SUIT:
            self.value += ACE_VALUE
            if self.value < ACE_THRESHOLD:
                self.value += ACE_REMAINING_VALUE

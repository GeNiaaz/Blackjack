from constants import ROYALTY_SUITS, ROYALTY_VALUE

class Player:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.ace_present = False
    
    # upper bounded at 50, no point using double ended list
    def add_card(self, card):
        self.hand.append(card)
        self.calculate_value(card)

    def calculate_value(self, card):
        curr_card_rank = card.rank
        if curr_card_rank.isdigit():
            self.value += int(curr_card_rank)
        elif curr_card_rank in ROYALTY_SUITS:
            self.value += ROYALTY_VALUE
        elif curr_card_rank == "A":
            self.ace_present = True
            self.value += 1

        if self.value < 12 and self.ace_present:
            total += 10 
            
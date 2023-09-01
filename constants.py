RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["Hearts", "Diamonds", "Spades", "Clubs"]
ROYALTY_SUITS = ["J", "Q", "K"]
ACE_SUIT = ["A"]
SUITS_SYMBOLS = {"Hearts": "♥", "Diamonds": "♦", "Spades": "♠", "Clubs": "♣"}
NUMBER_OF_CARDS = len(RANKS) * len(SUITS)

# numerical values
ROYALTY_VALUE = 10
ACE_VALUE = 1   
BLACKJACK_VALUE = 21
SHUFFLE_THRESHOLD = 14
ACE_THRESHOLD = 12
ACE_REMAINING_VALUE = 10
DEALER_HIT_THRESHOLD = 16
POINTS_BLACKJACK_VICTORY = 15
POINTS_VICTORY = 10
POINTS_DEFEAT = 10

# messages
USER_INPUT_CARD_MSG = f"Do you want to hit? Y/N\n>>> "
USER_INPUT_CARD_INVALID_MSG = f"Invalid input, please try again.\n"
USER_GAME_INPUT_FIRST_GAME_MSG = f"Would you like to start the game? Y/N\n >>> "
USER_GAME_INPUT_MSG = f"Would you like to play another round? Y/N\n >>> "
USER_GAME_END_MSG = f"final score is "
CARDS_RESHUFFLED = f"Draw pile less than 15, cards have been reshuffled."
PLAYER_EQUAL_TO_DEALER_MSG = f"It's a Push!"
PLAYER_BLACKJACK_MSG = f"Player gets Blackjack and wins 15 points"
PLAYER_WINS_MSG = f"Player wins 10 points"
PLAYER_LOSES_MSG = f"Player loses 10 points"
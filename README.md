## Blackjack

The game is a 1 player game versus the dealer (bot). The interface resets with every action from the user.

The idea of Blackjack is to score higher than a Dealer’s hand without exceeding twenty-
one. Cards count their value, except face cards (jacks, queens, kings) count for ten, and aces count for one. If you beat the Dealer, you get 10 points. If you get Blackjack (21 with just two cards) and beat the Dealer, you get 15 points.

The game starts by giving two cards (from a standard 52 card deck) to the Dealer (one face down) and two cards to the player. The player decides whether to Hit (get another card) or Stay. The player can continue to hit as many if desired. If the player exceeds 21 before staying, it is a loss (-10 points). If the player does not exceed 21, it becomes the dealer’s turn. The Dealer adds cards until 16 is exceeded. When this occurs, if the dealer also exceeds 21 or if his total is less than the player’s, he loses. If the dealer total is greater than the player total (and under 21), the dealer wins. If the dealer and player have the same total, it is a Push (no points added or subtracted).

#### Game vs Round
- A Round is one that ends when the player either chooses to stay or the player's cards total value ≥ 21
- A Game is made up of multiple Rounds whereby the points accumulated in each round are tabulated. 
When the player chooses not to play another round, the final Game score is tabulated and displayed
to the player before the Game ends.

### Usage
1. Type `python3 main.py` in the main directory to start the Game
2. Follow the on-screen instructions to play the Game

### Running tests
1. `python3 -m unittest discover -v tests`
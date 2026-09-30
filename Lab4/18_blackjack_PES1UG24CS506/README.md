# Terminal Blackjack

**Name:** Ujwal Sanikam  
**SRN:** PES1UG24CS506  

## Overview
This project is an interactive, terminal-based Blackjack game written in Python. It features a persistent betting system, dynamic hand evaluations, and robust error handling to ensure uninterrupted gameplay.

## How to Run
Ensure you have Python installed on your system. Navigate to the project directory and run the main script:
```bash
python main.py
```

## Game Rules & Mechanics

- **Card Values:** Number cards are worth their printed face value, and face cards (J, Q, K) are each worth 10.
- **Ace Scoring:** Aces dynamically count as either 11 or 1. They initially count as 11, but if drawing a card pushes your total over 21, the Ace automatically reduces to 1 to prevent a bust.
- **Player Actions:** During your turn, you can input `h` to Hit (draw another card), `s` to Stand (keep your current hand and pass to the dealer), or `q` to Quit the application.
- **Dealer Rules:** Once the player stands, the dealer reveals their hidden card. The dealer is required to keep hitting until their total reaches 17 or higher.
- **Outcomes:**

- **Win:** You win if your final total is higher than the dealer's without exceeding 21, or if the dealer goes over 21 (busts).
- **Bust:** If your hand exceeds 21 at any point, you immediately bust and lose the round.
- **Lose:** You lose if the dealer achieves a valid hand with a higher total than yours.
- **Push:** If you and the dealer end up with the exact same total, it is a tie (push) and no chips are exchanged.

## Betting & Chip Balance

- Players begin a new game session with a starting balance of 100 chips.
- Before any cards are dealt, you must place a wager. The bet must be a whole number between 1 and your current total chip balance.
- Winning adds your wagered amount to your total, losing (or busting) subtracts the wager, and a push leaves your balance untouched.
- Your updated chip balance carries over from round to round. The game ends if you choose to stop playing or if your chip balance drops to 0.

## Lab Updates & Added Features
The following improvements and bug fixes were integrated into this final version:

- **Dynamic Ace Calculation:** Resolved a logic flaw where Aces were permanently hardcoded to a value of 11. The calculation now accurately tracks Aces and converts them to 1s when necessary to yield the best valid hand.
- **Persistent Betting System:** Replaced the static 10-chip win/loss logic with a dynamic wagering system that scales with the player's balance and choices.
- **Bust Resolution Fix:** Patched a bug where a player busting bypassed the chip deduction logic. Busting now correctly subtracts the player's wager and cleanly concludes the round.
- **Strict Error Handling:** Implemented robust `try/except` blocks to catch non-numeric or empty betting inputs. Invalid game commands are now safely caught and re-prompted instead of causing unexpected behavior.
- **Empty Deck Safety:** Introduced a secure drawing mechanism. If the deck ever runs out of cards during an extended session, it automatically re-initializes and reshuffles a fresh deck.
- **UI Polish:** Enhanced the terminal feedback to explicitly display drawn cards, reveal the dealer's final calculated total, and provide clear end-of-round summaries detailing the match result and updated bankroll.

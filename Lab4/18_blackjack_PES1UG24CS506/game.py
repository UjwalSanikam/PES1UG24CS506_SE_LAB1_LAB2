from cards import Deck, hand_value

class Blackjack:
    def __init__(self):
        self.chips = 100

    def show(self, player, dealer, hide=True):
        shown_dealer = ["??"] if hide else [f"{r}{s}" for r, s in dealer]
        print("\nDealer:", " ".join(shown_dealer))
        if not hide:
            print(f"Dealer Total: {hand_value(dealer)}")
            
        print("Player:", " ".join(f"{r}{s}" for r, s in player), "=", hand_value(player))
        print()

    def draw_card(self, deck):
        card = deck.draw()
        if not card:  # Handle deck exhaustion safely
            print("\n[Deck empty! Reshuffling...]")
            deck.__init__()  # Re-initialize and shuffle a new deck
            card = deck.draw()
        return card

    def round(self):
        print(f"\n--- New Round ---")
        print(f"Current balance: {self.chips} chips")
        
        while True:
            try:
                bet_input = input(f"Place your bet (1-{self.chips}): ").strip()
                if not bet_input:
                    print("Input cannot be empty.")
                    continue
                bet = int(bet_input)
                if 1 <= bet <= self.chips:
                    break
                else:
                    print(f"Invalid bet. You must bet between 1 and {self.chips}.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        deck = Deck()
        player = [self.draw_card(deck), self.draw_card(deck)]
        dealer = [self.draw_card(deck), self.draw_card(deck)]
        self.show(player, dealer)

        while hand_value(player) < 21:
            key = input("[h]it [s]tand [q]uit: ").strip().lower()
            if key == "q":
                return False
            elif key == "s":
                break
            elif key == "h":
                card = self.draw_card(deck)
                player.append(card)
                print(f"\n-> You drew: {card[0]}{card[1]}")
                self.show(player, dealer)
                
                if hand_value(player) > 21:
                    print("Result: Bust! You went over 21.")
                    self.chips -= bet
                    print(f"Updated Balance: {self.chips} chips")
                    return True
            else:
                print("Invalid input. Please enter 'h', 's', or 'q'.")
                
        while hand_value(dealer) < 17:
            print("\n-> Dealer hits...")
            dealer.append(self.draw_card(deck))

        self.show(player, dealer, hide=False)
        pv, dv = hand_value(player), hand_value(dealer)
        
        print(f"Final Totals -> Player: {pv} | Dealer: {dv}")
        
        if dv > 21:
            self.chips += bet
            print("Result: Dealer busts. Player wins!")
        elif pv > dv:
            self.chips += bet
            print("Result: Player wins!")
        elif pv < dv:
            self.chips -= bet
            print("Result: Dealer wins.")
        else:
            print("Result: Push (Tie).")
            
        print(f"Updated Balance: {self.chips} chips")
        return True

    def run(self):
        print("Blackjack — starting chips:", self.chips)
        while self.chips > 0:
            if not self.round():
                break
            
            if self.chips > 0:
                while True:
                    replay = input("\nPlay again? [y/n]: ").strip().lower()
                    if replay in ['y', 'n']:
                        break
                    print("Invalid input. Please enter 'y' or 'n'.")
                if replay != "y":
                    break

        if self.chips <= 0:
            print("\nYou're out of chips! Game over.")
        else:
            print(f"\nYou walked away with {self.chips} chips. Thanks for playing!")
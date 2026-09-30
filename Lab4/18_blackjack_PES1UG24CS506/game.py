from cards import Deck, hand_value


class Blackjack:
    def __init__(self):
        self.chips = 100

    def show(self, player, dealer, hide=True):
        shown_dealer = ["??"] if hide else [f"{r}{s}" for r, s in dealer]
        print("Dealer:", " ".join(shown_dealer))
        print("Player:", " ".join(f"{r}{s}" for r, s in player),
              "=", hand_value(player))

    def round(self):
        print(f"Current balance: {self.chips} chips")
        while True:
            try:
                bet = int(input(f"Place your bet (1-{self.chips}): "))
                if 1 <= bet <= self.chips:
                    break
                else:
                    print(f"Invalid bet. You must bet between 1 and {self.chips}.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

        deck = Deck()
        player = [deck.draw(), deck.draw()]
        dealer = [deck.draw(), deck.draw()]
        self.show(player, dealer)

        while hand_value(player) < 21:
            key = input("[h]it [s]tand [q]uit: ").strip().lower()
            if key == "q":
                return False
            if key == "s":
                break
            if key == "h":
                player.append(deck.draw())
                self.show(player, dealer)
                if hand_value(player) > 21:
                    print("Bust.")
                    self.chips -= bet  # Subtract dynamic bet on bust
                    return True
                    
        while hand_value(dealer) < 17:
            dealer.append(deck.draw())

        self.show(player, dealer, hide=False)
        pv, dv = hand_value(player), hand_value(dealer)
        
        if dv > 21 or pv > dv:
            self.chips += bet  # Add dynamic bet on win
            print("Player wins.")
        elif pv < dv:
            self.chips -= bet  # Subtract dynamic bet on loss
            print("Dealer wins.")
        else:
            print("Push.")  # Balance remains unchanged
        return True

    def run(self):
        print("Blackjack — starting chips:", self.chips)
        while self.chips > 0:
            if not self.round():
                return
            if input("Play again? [y/n]: ").strip().lower() != "y":
                return

import random

class Coin:
    def __init__(self):
        self.sideup = "Heads"

    def toss_the_coin(self):
        outcome = random.randint(1, 100)  # Random number between 1 and 100

        if outcome <= 45:
            self.sideup = "Heads"
        elif outcome <= 90:
            self.sideup = "Tails"
        elif outcome <= 95:
            self.sideup = "Upright on the table"
        elif outcome <= 99:
            self.sideup = "Disappeared in a rabbit hole"
        else:
            self.sideup = "Lost in a wormhole"

    def get_sideup(self):
        return self.sideup

# Main function
def main():
    my_coin = Coin()

    print("Before tossing, the coin shows:", my_coin.get_sideup())

    print("Tossing the coin...")
    my_coin.toss_the_coin()

    print("Now the coin shows:", my_coin.get_sideup())

# Run the main function
main()

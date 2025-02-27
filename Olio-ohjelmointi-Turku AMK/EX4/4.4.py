class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    def eat_ordinary(self):
        if self.balance >= 2.95:
            self.balance -= 2.95

    def eat_luxury(self):
        if self.balance >= 5.90:
            self.balance -= 5.90

    def deposit_money(self, amount: float):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount


# pää funktio
if __name__ == "__main__":
    # Step 1: Create LunchCards
    peter_card = LunchCard(20)
    grace_card = LunchCard(30)

    # peter luxury lounas, grace normi lounas
    peter_card.eat_luxury()
    grace_card.eat_ordinary()

    # printtaa balanssit
    print("Peter:", peter_card)
    print("Grace:", grace_card)

    # peter deposittaa 20, grace syö luxury lounaan
    peter_card.deposit_money(20)
    grace_card.eat_luxury()

    # printtaa balanssit
    print("Peter:", peter_card)
    print("Grace:", grace_card)

    # peter syö 2 normi, grace deposittaa 50
    peter_card.eat_ordinary()
    peter_card.eat_ordinary()
    grace_card.deposit_money(50)

    # printtaa balanssit
    print("Peter:", peter_card)
    print("Grace:", grace_card)

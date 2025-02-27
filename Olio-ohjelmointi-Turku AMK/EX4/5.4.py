class PaymentTerminal:
    def __init__(self):
        self.funds = 1000  
        self.ordinaries = 0  
        self.luxuries = 0 

    def eat_ordinary(self, payment: float):
        price = 2.95
        if payment >= price:
            self.funds += price
            self.ordinaries += 1
            return payment - price 
        return payment  

    def eat_luxury(self, payment: float):
        price = 5.90
        if payment >= price:
            self.funds += price
            self.luxuries += 1
            return payment - price 
        return payment  

    def eat_ordinary_lunchcard(self, card: "LunchCard"):
        price = 2.95
        if card.balance >= price:
            card.balance -= price
            self.ordinaries += 1
            return True
        return False  

    def eat_luxury_lunchcard(self, card: "LunchCard"):
        price = 5.90
        if card.balance >= price:
            card.balance -= price
            self.luxuries += 1
            return True
        return False  

    def deposit_money_to_card(self, card: "LunchCard", amount: float):
        """Deposits money onto a LunchCard and increases terminal funds."""
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount")
        card.deposit_money(amount)
        self.funds += amount  

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    def deposit_money(self, amount: float):
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount")
        self.balance += amount

if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(5)

    print(card)  #balanssi
    exactum.deposit_money_to_card(card, 20)  # tallettaa 20
    print(card)  # päivitetty balanssi

    print("Funds available at the terminal:", exactum.funds)

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
    

class PaymentTerminal:
    def __init__(self):
        self.funds = 1000  # aloitus 1000 euro
        self.ordinaries = 0
        self.luxuries = 0

    def eat_ordinary(self, payment: float):
        price = 2.95
        if payment >= price:
            self.funds += price
            self.ordinaries += 1
            return payment - price  # palauttaa muutoksen
        return payment  # jos ei tarpeeksi, palauttaa koko määrän

    def eat_luxury(self, payment: float):
        price = 5.90
        if payment >= price:
            self.funds += price
            self.luxuries += 1
            return payment - price  
        return payment  

    def eat_ordinary_lunchcard(self, card: LunchCard):
        price = 2.95
        return card.subtract_from_balance(price)

    def eat_luxury_lunchcard(self, card: LunchCard):
        price = 5.90
        return card.subtract_from_balance(price)

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        if amount > 0:
            card.deposit_money(amount)
            self.funds += amount
            
if __name__ == "__main__":
    # Test Part 1
    card = LunchCard(10)
    print(card) 
    result = card.subtract_from_balance(8)
    print("Payment successful:", result)  
    print(card)  
    result = card.subtract_from_balance(4)
    print("Payment successful:", result)  
    print(card) 

    #Part2
    """ exactum = PaymentTerminal()

    change = exactum.eat_ordinary(10)
    print("The change returned was", change)

    change = exactum.eat_ordinary(5.9)
    print("The change returned was", change)

    change = exactum.eat_luxury(5.9)
    print("The change returned was", change)

    print("Funds available at the terminal:", exactum.funds)
    print("Ordinary lunches sold:", exactum.ordinaries)
    print("Luxury lunches sold:", exactum.luxuries) """

    #Part 3
    """ exactum = PaymentTerminal()

    change = exactum.eat_ordinary10)
    print("The change returned was", change)

    card = LunchCard(7)

    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_ordinary_lunchcard(card)
    print("Payment successful:", result)

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials) """

    #Part4
    """ exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_luxury_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials) """

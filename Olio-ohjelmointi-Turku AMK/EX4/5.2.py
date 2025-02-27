class PaymentTerminal:
    def __init__(self):
        self.funds = 1000  
        self.ordinaries = 0  # normi lounaita myyty
        self.luxuries = 0  # luxury lounaita myyty

    def eat_ordinary(self, payment: float):
        price = 2.95
        if payment >= price:
            self.funds += price
            self.ordinaries += 1
            return payment - price 
        return payment  # jos ei tarpeeksi, palauttaa koko määrän

    def eat_luxury(self, payment: float):
        price = 5.90
        if payment >= price:
            self.funds += price
            self.luxuries += 1
            return payment - price  # palauttaa takaisin saatavan määrän
        return payment 

if __name__ == "__main__":
    exactum = PaymentTerminal()

    change = exactum.eat_ordinary(10)
    print("The change returned was", change)

    change = exactum.eat_ordinary(5.9)
    print("The change returned was", change)

    change = exactum.eat_luxury(5.9)
    print("The change returned was", change)

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.ordinaries)
    print("Special lunches sold:", exactum.luxuries)

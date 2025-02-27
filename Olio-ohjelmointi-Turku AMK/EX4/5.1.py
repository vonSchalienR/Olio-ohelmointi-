class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def __str__(self):
        return f"Balance {self.balance:.0f}" 

    def deposit_money(self, amount: float):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True 
        return False  

if __name__ == "__main__":
    card = LunchCard(10)
    print(card)

    result = card.subtract_from_balance(8)
    print("Payment successful:", result)
    print(card)

    result = card.subtract_from_balance(4)
    print("Payment successful:", result)
    print(card)

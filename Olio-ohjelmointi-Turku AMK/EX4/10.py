class BankAccount:
    def __init__(self, owner, account_number, balance):
        self.__owner = owner 
        self.__account_number = account_number 
        self.__balance = balance  
    
    def deposit(self, amount: float):
        self.__balance += amount  # talletus tilille
        self.__service_charge()  # service maksu taletuksen jälkeen
    
    def withdraw(self, amount: float):
        if amount <= self.__balance:  # tarkistaa onko balanssia tarpeeksi
            self.__balance -= amount 
            self.__service_charge() 
        else:
            print("Insufficient funds") 
    
    def balance(self):
        return self.__balance  
    
    def __service_charge(self):
        self.__balance -= self.__balance * 0.01

account = BankAccount("Randy Riches", "12345-6789", 1000)
account.withdraw(100)
print(account.balance()) 

account.deposit(100)
print(account.balance())  
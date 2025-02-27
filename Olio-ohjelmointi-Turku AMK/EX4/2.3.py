class NumberStats:
    def __init__(self):
        # lukujen määrä on 0
        self.numbers = 0
        self.total_sum = 0

    def add_number(self, number: int):
        # lisää lukumäärän 1 ja päivittää summan
        self.numbers += 1
        self.total_sum += number

    def count_numbers(self):
        # palauttaa lukujen määrän
        return self.numbers

    def get_sum(self):
        # palauttaa summan
        return self.total_sum

    def average(self):
        # palauttaa keskiarvon
        if self.numbers == 0:
            return 0
        return self.total_sum / self.numbers

if __name__ == "__main__":
    stats = NumberStats()
    
    print("Please give a number(-1 to stop):")
    while True:
        user_input = int(input())
        if user_input == -1:
            break
        stats.add_number(user_input)
    
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())

class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.total_sum = 0

    def add_number(self, number: int):
        self.numbers += 1
        self.total_sum += number

    def get_sum(self):
        return self.total_sum

    def average(self):
        if self.numbers == 0:
            return 0
        return self.total_sum / self.numbers


if __name__ == "__main__":
    total_stats = NumberStats()
    even_stats = NumberStats()
    odd_stats = NumberStats()
    
    print("Please give a number (-1 to stop):")
    while True:
        user_input = int(input())
        if user_input == -1:
            break
        
        total_stats.add_number(user_input)
        
        # even vai odd numero?
        if user_input % 2 == 0:
            even_stats.add_number(user_input)
        else:
            odd_stats.add_number(user_input)
    
    print("Total sum of numbers:", total_stats.get_sum())  # lukujen summa
    print("Mean of numbers:", total_stats.average())  # keskiarvo
    print("Sum of even numbers:", even_stats.get_sum())  # Summa even numbers
    print("Sum of odd numbers:", odd_stats.get_sum())  # Summa odd numbers

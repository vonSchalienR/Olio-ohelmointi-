class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.total_sum = 0

    def add_number(self, number: int):
        self.numbers += 1
        self.total_sum += number

    def count_numbers(self):
        return self.numbers

    def get_sum(self):
        return self.total_sum

        # keskiarvo
    def average(self):
        if self.numbers == 0:
            return 0
        return self.total_sum / self.numbers

if __name__ == "__main__":
    # Part 1 test prints:
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    
    # Part 2 test prints:
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
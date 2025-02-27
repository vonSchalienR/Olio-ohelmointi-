class NumberStats:
    def __init__(self):
        #no need to add any new varibales here, just change the
        #initialization of the self.numbers variable.
        self.numbers = 0

    def add_number(self, number: int):
        # kasvattaa numeroa yhdellä, aina kun numero lisätään
        self.numbers += 1

    def count_numbers(self):
        # palauttaa lisättyjen numeroiden arvon
        return self.numbers

if __name__ == "__main__":
    # Part 1 test prints:
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
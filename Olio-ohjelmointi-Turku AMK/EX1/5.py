def count_negative_integers(numbers):
    """
    Counts and returns the number of negative integers in the given list.
    """
    return sum(1 for num in numbers if num < 0)

def count_even_integers(numbers):
    """
    Counts and returns the number of even integers in the given list.
    """
    return sum(1 for num in numbers if num % 2 == 0)

def read_integers():
    """
    Reads integers from the user repeatedly until 0 is entered.
    Returns a list of all entered integers (excluding the 0).
    """
    numbers = []
    print("Enter integers (enter 0 to stop):")
    
    while True:
        num = int(input("Enter an integer: "))
        if num == 0:
            break
        numbers.append(num)
    
    return numbers

def main():
    numbers = read_integers()
    negative_count = count_negative_integers(numbers)
    even_count = count_even_integers(numbers)
    
    print(f"\nNumber of negative integers entered: {negative_count}")
    print(f"Number of even integers (parilliset luvut) entered: {even_count}")

# Call the main function
main()

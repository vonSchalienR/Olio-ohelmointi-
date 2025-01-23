def count_negative_integers():
    """
    Reads integers repeatedly until the user enters 0.
    Counts and returns the number of negative integers entered.
    """
    negative_count = 0
    print("Enter integers (enter 0 to stop):")
    
    while True:
        num = int(input("Enter an integer: "))
        if num == 0:
            break
        if num < 0:
            negative_count += 1
    
    return negative_count

def main():
    negative_count = count_negative_integers()
    print(f"\nNumber of negative integers entered: {negative_count}")

# Call the main function
main()

import random

def roll_die():
    """
    Returns a random number between 1 and 6 (inclusive).
    """
    return random.randint(1, 6)

# Call the function and print the result
result = roll_die()
print(f"The rolled number is: {result}")

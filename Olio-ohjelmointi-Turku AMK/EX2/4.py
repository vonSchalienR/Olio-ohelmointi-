def factorials(n: int):
    fact_dict = {}
    fact = 1  # Start with factorial of 1
    for i in range(1, n + 1):
        fact *= i  # Calculate factorial iteratively
        fact_dict[i] = fact
    return fact_dict

# Example usage:
k = factorials(5)
print(k[1])  # Output: 1
print(k[3])  # Output: 6
print(k[5])  # Output: 120

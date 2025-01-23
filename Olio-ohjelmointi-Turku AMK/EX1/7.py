def calculate_terms_and_sums(max_value):
    """
    Calculates the number of terms, the sum of terms, and the sum of squared terms
    for the arithmetic progression (AP) 3, 6, 9, ..., up to max_value.
    """
    # Common difference (d) = 3, first term (a) = 3
    a = 3
    d = 3

    # Calculate the number of terms (n)
    n = max_value // a  # Integer division gives the number of terms

    # Calculate the sum of the terms (S_n = n/2 * (2a + (n-1)d))
    sum_of_terms = (n / 2) * (2 * a + (n - 1) * d)

    # Calculate the sum of squared terms (Sum = 3^2 + 6^2 + 9^2 + ...)
    sum_of_squared_terms = sum((a + (i - 1) * d) ** 2 for i in range(1, n + 1))

    return n, sum_of_terms, sum_of_squared_terms


def main():
    max_value = int(input("Enter the maximum value for the AP: "))
    
    n, sum_of_terms, sum_of_squared_terms = calculate_terms_and_sums(max_value)
    
    print(f"\nNumber of terms in the AP: {n}")
    print(f"Sum of the terms: {sum_of_terms}")
    print(f"Sum of the squared terms: {sum_of_squared_terms}")


# Call the main function
main()

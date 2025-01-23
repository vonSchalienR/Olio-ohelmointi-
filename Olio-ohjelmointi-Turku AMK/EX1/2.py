import random

# Initialize empty lists
number_list = []
string_list = []

# Get numbers from the user
print("Enter 10 numbers:")
for i in range(10):
    number = int(input(f"Enter number {i+1}: "))
    number_list.append(number)

# Get strings from the user
print("\nEnter 10 strings:")
for i in range(10):
    string = input(f"Enter string {i+1}: ")
    string_list.append(string)

# Print both lists
print("\nOriginal number list:", number_list)
print("Original string list:", string_list)

# Fill the number list with randomly generated numbers
number_list = [random.randint(1, 100) for _ in range(10)]

# Print the new number list
print("\nRandomly generated number list:", number_list)

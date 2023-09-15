# Program to check if a number is positive, even, and divisible by 3

# Take input from the user
number = int(input("Enter a number: "))

# Check if the number is positive, even, and divisible by 3
is_positive = number > 0
is_even = number % 2 == 0
is_divisible_by_3 = number % 3 == 0

# Combine the conditions using logical operators
if is_positive and is_even and is_divisible_by_3:
    print("The number satisfies all conditions.")
else:
    print("The number does not satisfy all conditions.")

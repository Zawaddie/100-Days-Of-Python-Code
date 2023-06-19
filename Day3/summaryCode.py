# Testing Input Function and String Operations

# Input function with an argument
name = input("Enter your name: ")

# Result of an input function
age = input("Enter your age: ")
age_next_year = int(age) + 1

# Input function prohibited operations
number = input("Enter a number: ")
# Uncomment the line below to test a prohibited operation
# result = number * 2

# Type casting
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2

# String operation
greeting = "Hello, " + name + "!"
length = len(greeting)

# Replication
symbol = input("Enter a symbol: ")
replicated_symbol = symbol * 5

# str() function
decimal = float(input("Enter a decimal number: "))
decimal_str = str(decimal)

# Print the results
print(greeting)
print("Next year, you will be", age_next_year, "years old.")
print("The sum of the two numbers is", sum)
print("The length of the greeting is", length)
print("The replicated symbol is", replicated_symbol)
print("The decimal number as a string is", decimal_str)

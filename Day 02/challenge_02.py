#Arithmetic Operators and their precedence

# Take input from the user
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

# Perform arithmetic operations
addition =        num_1 +  num_2
subtraction =     num_1 -  num_2
multiplication =  num_1 *  num_2
division =        num_1 /  num_2
exponentiation =  num_1 ** num_2

# Print the results
print("Addition: ", addition)
print("Subtraction: ", subtraction)
print("Multiplication: ", multiplication)
print("Division: ", division)
print("Exponentiation: ", exponentiation)

#aurgmented assignment operator
num_3 = 10
num_3 += 5
print(num_3)
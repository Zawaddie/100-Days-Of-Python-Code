# Testing Strings, String Operators, Formatted Strings, and String Methods

# String Input
name = input("Enter your name: ")

# String Operators
greeting = "Hello, " + name + "!"
length = len(name)

# Formatted Strings
age = int(input("Enter your age: "))
output = f"{name}, you are {age} years old."

# String Methods
capitalized_name = name.capitalize()
uppercase_name = name.upper()
lowercase_name = name.lower()
reversed_name = name[::-1]

# Print the results
print(greeting)
print("The length of your name is:", length)
print(output)
print("Capitalized name:", capitalized_name)
print("Uppercase name:", uppercase_name)
print("Lowercase name:", lowercase_name)
print("Reversed name:", reversed_name)


# define and use methods
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius * self.radius
    
    def calculate_circumference(self):
        return 2 * 3.14 * self.radius

# Create an instance of the Circle class
circle = Circle(5)

# Access and invoke methods on the instance
area = circle.calculate_area()
circumference = circle.calculate_circumference()

# Print the results
print("Area:", area)
print("Circumference:", circumference)


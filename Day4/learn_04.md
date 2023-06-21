# On Day 4
In this day, i focussed on: Strings, formated strings in python, String methods

## Strings 
single (‘ ‘) or double (“ “) quotes defines strings 
A multi-line string surrounded with tripe quotes (“””). 
We can get individual characters in a string using square brackets []. 

       description = ‘Age is a number’
       description[1]   # returns the 2ndcharacter
       description[-1]  # returns the 1st character from the end 
       description[-2]  # returns the 2nd character from the end

Slicing a string using a similar notation: 

       description[1:5] #returns all the characters starting from the index position of 1 to 5 (but excluding 5).

with start index left out, 0 will be assumed. 
with end index left out, the length of the string will be assumed. 

## String Operators
The + (plus) sign applied to strings becomes a Concantenation Operator. 

         print(string + string)

The * (asteric) applied to a string and number  becomes a Replacation Operator.

         print(string * number)
         print(number * string)

A number less than or equal to zero produces an empty string

## Formatted Strings
Formatted strings(f- strings) are a way to embed expressions inside string literals in Python. They provide a way to create strings that include variables, expressions, and even function calls. 

They allow the easy combining of variables and expressions with string literals without the need for explicit type conversions or concatenation operations. 

The syntax for formatted strings in Python is to prefix the string with the letter f or F, and then enclose the expressions or variables within curly braces {} to dynamically place your input strings.

The expressions inside the curly braces are evaluated at runtime and their values are inserted into the resulting string.

        name = "Mackena"
        age = 25
        message = f"Hello, {name}! You are {age} years old."
        print(message)


Formatted strings also support various formatting options, such as specifying the number of decimal places for floating-point numbers, padding, alignment, and more. 

You can include these options within the curly braces after the variable or expression, using a colon : as the separator.

Example to format a floating-point number with 2 decimal places.

        f"Value: {value:.2f}" 

To check if a string contains a character (or a sequence of characters), we use the in 
operator: 

       name = "mackena"
       contains = "kena" in name
       print(contains)

## String Methods
Methods are functions that are associated with objects. They are defined within the scope of a class and are used to perform operations on instances (objects) of that class. Methods are a way to encapsulate functionality and behavior within an object-oriented programming paradigm.

### buit-in methods:
are pre-defined in the Python language and are available for use without requiring any additional code or imports
        message.upper() # to convert to uppercase
        message.lower() # to convert to lowercase
        message.title() # to capitalize the first letter of every word
        message.find(‘k’) # returns the index of the first occurrence of k (or -1 if not found) 
        message.replace(‘k’, ‘q’) 

### user_defined methods:
Example: if you define a class called Circle, you might define methods such as calculate_area(), calculate_circumference(), and display_info(), which are specific to the behavior and properties of circles.

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

### Self Parameter in methods: 
It's a reference to the instance of the class itself. It allows methods to access and manipulate the instance's attributes and perform actions specific to that instance.

## Challenge_04
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old, except use f-strings instead of the + operator to print the resulting output message.
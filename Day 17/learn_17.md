# On Day 17

# Functions in Python:

A function is a named block of reusable code that performs a specific task or calculates a result. Functions allow you to break down your program into smaller, modular units, making your code more organized, readable, and reusable. They provide a way to encapsulate a set of instructions that can be called multiple times from different parts of a program.

### Function Definition: 

A function is defined using the def keyword, followed by the function name, parentheses ( ), and a colon :. The function body is indented below the definition.

### Function Parameters: 

Functions can take input values, called parameters or arguments, which are specified within the parentheses during the function definition. Parameters are optional and can be used to pass values into the function for processing.

### Return Statement: 

Functions can optionally return a value using the return statement. This allows the function to compute a result and pass it back to the calling code. If no return statement is used, the function returns None by default.

### Function Call: 

To execute a function and run the code inside it, you need to call the function by using its name followed by parentheses ( ). If the function has parameters, you can pass values inside the parentheses.

### Code Reusability: 

Functions allow you to encapsulate a specific task or a set of instructions that can be reused multiple times throughout your program. This promotes code reuse, modularity, and maintainability.

## Uses Cases:
there are a number of applications of functions.
     - Breaking down complex tasks into smaller, manageable parts.
     - Encapsulating commonly used code to avoid repetition.
     - Enhancing code organization and readability.
     - Promoting code reuse and modularity.
     - Implementing algorithms and logic as reusable units.
     - Abstracting functionality and hiding implementation details.
     - Separating concerns and achieving a clean code structure.
     

## Challenge_17: Word Frequency Counter

Write a Python program that takes a text string as input and counts the frequency of each word in the text. Your program should perform the following steps:

        1. Define a function called word_frequency_counter that takes a text string as a parameter.
        2. Inside the function, split the text string into a list of words using the split() method.
        3. Create an empty dictionary called word_frequency to store the frequency of each word.
        4. Iterate over the list of words and update the word_frequency dictionary accordingly. If a word is encountered for the first time, add it as a key in the dictionary with a value of 1. If the word is already present in the dictionary, increment its value by 1.
        5 Return the word_frequency dictionary from the function
        6. Prompt the user to enter a text string.
        7. Call the word_frequency_counter function with the user's input as an argument.
        8. Print the word frequency dictionary.

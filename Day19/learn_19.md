# On Day 19

# List comprehensions:
These provide a concise and elegant way to create new lists based on existing iterables, such as lists, strings, or tuples, with a compact syntax.  
They allow you to combine loops and conditional statements in a single line to generate a new list.

The general syntax:

        new_list = [expression for item in iterable if condition]
        
### expression: 
Represents the transformation or operation to be performed on each item from the iterable. It can be a simple value, a calculation, or a function call.

### item: 
Represents each item in the iterable that will be processed by the expression.

### iterable: 
Refers to the original sequence or collection of items, such as a list or string.

### condition (optional): 
Specifies an optional filtering condition. The expression is only applied to items that satisfy the condition.

List comprehensions are often used to perform simple operations on each item in a list and filter out specific elements. They can make your code more concise and readable compared to traditional loops.

## Usage of list comprehensions:
### 1. Squaring each number in a list:

            numbers = [1, 2, 3, 4, 5]
            squared = [x**2 for x in numbers]
            print(squared)  # Output: [1, 4, 9, 16, 25]

### 2. Filtering even numbers from a list:

            numbers = [1, 2, 3, 4, 5]
            evens = [x for x in numbers if x % 2 == 0]
            print(evens)  # Output: [2, 4]

### 3.Creating a new list from characters in a string:

            text = "Hello, World!"
            letters = [c.lower() for c in text if c.isalpha()]
            print(letters)  # Output: ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']

List comprehensions offer a concise and efficient way to manipulate and transform data in Python, making your code more expressive and readable.

## Nested List Comprehensions: 
List comprehensions can be nested within each other to handle multi-dimensional data structures. This allows you to create complex lists or perform operations on nested elements.

        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        flattened = [x for row in matrix for x in row]
        print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

## Multiple Iterables: 
You can use multiple iterables in a single list comprehension by using the zip() function or nested loops. This allows you to combine elements from multiple lists or perform operations on corresponding elements. 

        names = ['Alice', 'Bob', 'Charlie']
        ages = [25, 30, 35]
        person_data = [(name, age) for name, age in zip(names, ages)]
        print(person_data)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Dictionary Comprehensions: 
Similar to list comprehensions, you can create dictionaries using dictionary comprehensions. This enables you to quickly create dictionaries based on an iterable, with expressions defining the key-value pairs. 

        numbers = [1, 2, 3, 4, 5]
        square_dict = {x: x**2 for x in numbers}
        print(square_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

## Generator Expressions: 
If you only need to iterate over the generated elements without storing them all in memory, you can use generator expressions instead of list comprehensions. Generator expressions are similar to list comprehensions, but they create a generator object, which produces the values on-the-fly as you iterate over them. This can be more memory-efficient for large datasets. 

    numbers = [1, 2, 3, 4, 5]
    squared_gen = (x**2 for x in numbers)
    for num in squared_gen:
        print(num)  # Output: 1, 4, 9, 16, 25

## Conditional Expressions: 
List comprehensions can include conditional expressions that allow you to specify different expressions based on conditions. This enables you to apply different transformations or filtering based on specific criteria.

        numbers = [1, 2, 3, 4, 5]
        result = [x if x % 2 == 0 else x**2 for x in numbers]
        print(result)  # Output: [1, 2, 9, 4, 25]

## Challenge_19: Vowel Counter

Write a Python program that prompts the user to enter a sentence and counts the occurrence of each vowel (a, e, i, o, u) in the sentence. 

The program should use a list comprehension to create a list of tuples, where each tuple contains a vowel and its corresponding count. The list should be sorted in descending order of vowel frequency.

    - Ask the user to enter a sentence.
    - Use a list comprehension to create a list of tuples, where each tuple contains a vowel and its count in the sentence.
    - Sort the list in descending order of vowel frequency.
    - Display the vowels along with their counts.

## Challenge: Sentence Reversal

Write a Python program that prompts the user to enter a sentence and reverses the order of the words in the sentence using a list comprehension. The program should then display the reversed sentence.

        - Ask the user to enter a sentence.
        - Use a list comprehension to split the sentence into individual words.
        - Create a new list comprehension to reverse the order of the words.
        - Join the reversed words back into a sentence using the join() method.
        - Display the reversed sentence.
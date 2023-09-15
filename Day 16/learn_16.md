# On Day 16

## Data Structures: SETS
In Python, a set is an unordered collection of unique elements. 
It is a built-in data structure that is used to store multiple items in a single variable. Sets are mutable, meaning you can add or remove elements from them.

### Key features of sets in Python:

    1. Uniqueness: 
    Sets only contain unique elements. If you try to add a duplicate element to a set, it will be ignored.

    2. Unordered: 
    Sets do not maintain any specific order of elements. When you iterate over a set, the order in which elements are retrieved may vary.

    3. Mutable: 
    You can add and remove elements from a set after it is created.

    4. Operations: 
    Sets support various operations such as union, intersection, difference, and symmetric difference, which allow you to combine, compare, or modify sets.

    5. No Indexing: 
    Unlike lists or tuples, sets do not support indexing. You cannot access elements in a set using their positions.

To create a set, you can use curly braces {} or the set() constructor.

         fruits = {'apple', 'banana', 'orange'}
         
Here, fruits is a set containing three unique elements.

You can perform operations on sets using methods or operators:

        add() method to add an element to a set
        the | operator for set union
        remove(), 
        discard(), 
        & operator for set intersection
        - operator for set difference.

Sets are useful when you want to store a collection of unique elements and perform set-related operations efficiently. 

### use cases:
 - to remove duplicates from a list
 - check for membership, 
 - perform mathematical set operations.

## Challenge_16:  Finding Common Elements
Write a Python program that takes two sets of numbers and finds the common elements between them. Your program should perform the following steps:

        1. Create two sets of numbers called set1 and set2.
        2. Print both sets of numbers.
        3. Find the common elements between set1 and set2.
        4. Print the common elements.
        5. combine the two sets into a list.
        6. remove the duplicates using set
        7. print the new list without duplicates





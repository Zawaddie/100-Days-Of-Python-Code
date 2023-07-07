# On Day 15

# Data Structures: TUPLES
Atuple is an ordered, immutable collection of elements. It is represented by a sequence of values enclosed in parentheses ( ), separated by commas. 
Tuples can contain elements of different data types, such as integers, floats, strings, or even other tuples.
Tuples are commonly used to represent collections of related values, where the order and immutability of the elements are important. 

### Key characteristics of tuples:

           1. Order: 
           Tuples maintain the order of elements, meaning the elements are stored and retrieved in the same order they were added.

           2.Immutability: 
           Tuples are immutable, which means once a tuple is created, its elements cannot be modified. You cannot add, remove, or change individual elements of a tuple. However, you can create a new tuple by concatenating or slicing existing tuples.

           3. Heterogeneous: 
           Tuples can contain elements of different data types. For example, a tuple can contain an integer, followed by a string, and then a floating-point number.

           4. Indexing: 
          You can access individual elements in a tuple using indexing. 

           5. Tuple Packing and Unpacking: 
           Tuple packing is the process of creating a tuple by separating values with commas. Tuple unpacking is the process of assigning values from a tuple to multiple variables simultaneously.

           6. Immmutable and Hashable: 
           Tuples are immutable, making them suitable for use as keys in dictionaries and elements in sets. Since they cannot be modified, tuples have a fixed hash value, which ensures they can be used in data structures that require hashable objects.


### Use cases:
 - scenarios such as returning multiple values from a function, 
 - representing coordinates or points in space 
 - grouping related data together

## Challenge_15: Student Grade Calculation
Write a Python program that calculates the grade for a given student based on their test scores. Your program should perform the following steps:

        1. Create a tuple called test_scores that contains a set of test scores for a student.
        2. Print the test scores.
        3. Calculate the average score by summing up all the scores and dividing by the total number of scores.
        4. Determine the grade based on the average score using the following grading scale:
                    90 and above: A
                    80-89: B
                    70-79: C
                    60-69: D
                    Below 60: F
        5.Print the calculated average score and the corresponding grade.


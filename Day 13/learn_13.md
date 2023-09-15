# On Day 13

## 2D lists:
A 2D list is a list of lists where each element of the main list is a sublist. 
It allows you to store and manipulate data in a 2D grid-like structure. 
Each element in the grid corresponds to a row and column position.

In Python, you can create a 2D list by initializing a list of lists. 

            matrix = [                 # A 2D list with 3 rows and 4 columns
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]
            ]

Each sublist represents a row, and the elements within each sublist represent the values in each column.

You can access individual elements in a 2D list by specifying the row and column indices. For example, to access the element in the second row and third column of the matrix, you can use matrix[1][2] (indices start from 0).

## Iterating over the elements in the 2D list
You can also iterate over a 2D list using nested loops. 
The outer loop iterates over the rows, and the inner loop iterates over the columns. 

            for row in matrix:
                for element in row:
                    print(element, end=' ')
                print()                  # Print a newline after each row

This code will print each element of the 2D list, row by row.

## 2D lists use cases:
Useful for representing grid-like structures such as game boards, matrices, tables, and more. 
They provide a flexible way to organize and work with data in multiple dimensions.



## Sorting in Lists:
Sorting in lists refers to the process of arranging the elements in a list in a specific order. By default, the sorting is done in ascending order, but you can also specify a custom order based on your requirements.

You can sort a list using the built-in sort() method of the list object. 
The sort() method modifies the original list in-place, re-ordering its elements. 
You can use the sorted() function to create a new sorted list while leaving the original list unchanged.

Sorting a list in ascending order using the sort() method:

                numbers = [4, 2, 1, 3, 5]
                numbers.sort()
                print(numbers)            # Output: [1, 2, 3, 4, 5]

Using the sorted() function to create a new sorted list:

                numbers = [4, 2, 1, 3, 5]
                sorted_numbers = sorted(numbers)
                print(sorted_numbers)         # Output: [1, 2, 3, 4, 5]

By default, both sort() and sorted() use the natural order of the elements, which works well for numeric values and alphanumeric strings. 

For more complex objects or custom sorting criteria, you can provide a key parameter that specifies a function to extract a comparison key from each element.
To sort a list of strings based on their lengths, you can use the len() function as the key parameter:

                names = ['John', 'Alice', 'Mike', 'Sarah']
                names.sort(key=len)
                print(names)  # Output: ['John', 'Mike', 'Alice', 'Sarah']

Sorting in Python allows you to order the elements of a list according to your needs. It is commonly used for tasks such as organizing data, searching for specific values, and preparing data for further processing or presentation.


## Challenge_13a: Matrix Operations
Write a Python program that performs the following operations on a 2D list (matrix):

    1. Create a 3x3 matrix called matrix and initialize it with integer values.
    2. Print the matrix in a visually appealing format, with each row on a separate line.
    3. Calculate and print the sum of all the elements in the matrix.
    4. Calculate and print the sum of each row in the matrix.
    5. Calculate and print the sum of each column in the matrix.
    6. Find and print the maximum value and its position (row and column) in the matrix.
    7. Find and print the minimum value and its position in the matrix.
    8. Transpose the matrix (rows become columns, and columns become rows) and print the transposed matrix.
you can use nested loops and appropriate indexing to access elements in the matrix and perform the calculations.

## Challenge_13b: Sorting Student Scores
Write a Python program that takes a list of student scores and sorts them in ascending order. Your program should perform the following steps:

    1. Create a list called 'scores' that contains a set of student scores.
    2. Print the original list of scores.
    3. Sort the scores in ascending order using any sorting algorithm of your choice.
    4. Print the sorted list of scores.
Your program should output both the original and sorted lists of scores.

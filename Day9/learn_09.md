# On Day 09

## FLOW CONTROL: Loops
## Nested loop:

Nested loops refer to the situation where one loop is present inside another loop. In Python, you can have loops within loops, creating a nested structure. This allows you to perform repeated iterations at multiple levels.

The outer loop executes its iterations, and for each iteration, the inner loop executes its own iterations. This nesting can be done with for loops or while loops.

example"

                    for i in range(3):
                        for j in range(2):
                            print(f"({i}, {j})")

In this example, the outer loop iterates three times, and for each iteration, the inner loop iterates two times. The print statement inside the inner loop will be executed a total of six times, printing the coordinate pairs (i, j).


# Challenge 09: Pattern Printing

Write a Python program that takes a positive integer n as input and prints a pattern consisting of n rows and n columns. The pattern should be a square shape with alternating characters 'X' and 'O'.

# PATTERN PRINTING:

# Prompt the user to enter a positive integer n.
# Use nested loops to iterate over the rows and columns.
# Inside the nested loops, determine whether to print 'X' or 'O' based on the row and column indices.
# Print the character for each position in the pattern.
# After each row, print a newline character to move to the next row.



n = int(input("Enter a positive integer: "))     # Prompt the user to enter a positive integer

def print_pattern(n):
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print('X', end=' ')
            else:
                print('O', end=' ')
        print()
print_pattern(n)                                  # Call the function to print the pattern




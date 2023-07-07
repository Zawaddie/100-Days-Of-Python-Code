# Step 1: Create a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Step 2: Print the matrix
print("Matrix:")
for row in matrix:
    print(" ".join(str(element) for element in row))

# Step 3: Calculate and print the sum of all elements
total_sum = sum(sum(row) for row in matrix)
print("Sum of all elements:", total_sum)

# Step 4: Calculate and print the sum of each row
row_sums = [sum(row) for row in matrix]
print("Sum of each row:", row_sums)

# Step 5: Calculate and print the sum of each column
column_sums = [sum(row[i] for row in matrix) for i in range(len(matrix[0]))]
print("Sum of each column:", column_sums)

# Step 6: Find and print the maximum value and its position
max_value = max(max(row) for row in matrix)
max_position = [(i, row.index(max_value)) for i, row in enumerate(matrix) if max_value in row]
print("Maximum value:", max_value)
print("Position(s):", max_position)

# Step 7: Find and print the minimum value and its position
min_value = min(min(row) for row in matrix)
min_position = [(i, row.index(min_value)) for i, row in enumerate(matrix) if min_value in row]
print("Minimum value:", min_value)
print("Position(s):", min_position)

# Step 8: Transpose the matrix and print the transposed matrix
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Transposed matrix:")
for row in transposed_matrix:
    print(" ".join(str(element) for element in row))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Print both sets of numbers
print("Set 1:", set1)
print("Set 2:", set2)

# Find the common elements between the sets
common_elements = set1.intersection(set2)

# Print the common elements
print("Common Elements:", common_elements)

# convert the two sets into lists
list1 = list(set1)
list2 = list(set2)

print("List 1:", list1)
print("List 2:", list2)

combined_list = list1 + list2
print("Combined List:", combined_list)

# Convert the  combined list to a set to remove duplicates
unique_elements = set(combined_list)

# Convert the set back to a list
newList = list(unique_elements)

# Print the new list without duplicates
print(newList)

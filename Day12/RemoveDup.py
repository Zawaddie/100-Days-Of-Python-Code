## a program to remove duplicates from a list

numbers = [2,6,3,5,8,9,8,10,13,15,2,2,8,8,5,2]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
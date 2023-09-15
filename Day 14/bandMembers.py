# Step 1: Create an empty list named beatles
beatles = []
print("step 1:", beatles)

# Step 2: Add members of the band using append()
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("step 2:", beatles)

# Step 3: Prompt the user to add more members using a for loop and append()
for _ in range(2):
    member = input("Enter a band member's name: ")
    beatles.append(member)
print("step 3:", beatles)

# Step 4: Remove Stu Sutcliffe and Pete Best using del
del beatles[3:5]
print("step 4:", beatles)

# Step 5: Add Ringo Starr to the beginning of the list using insert()
beatles.insert(0, "Ringo Starr")
print("step 5:", beatles)

# Print the final list
print(beatles)

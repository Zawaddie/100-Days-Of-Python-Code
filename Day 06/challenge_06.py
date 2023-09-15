# Program to determine the category of a given score

score = int(input("Enter your score: "))

if score >= 90:
    if score >= 95:
        print("Excellent!")
    else:
        print("Good job!")
elif score >= 80:
    print("Well done!")
elif score >= 70:
    print("Keep it up!")
elif score >= 60:
    print("Average!")
else:
  print("Needs improvement.")
           

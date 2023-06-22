while True:
    try:
        # Prompt the user to enter a numerical grade
        grade = int(input("Enter the numerical grade (0-100): "))
        
        # Validate the input to ensure it is within the valid range
        if 0 <= grade <= 100:
            # Use conditional statements to determine the letter grade
            if grade >= 90:
                letter_grade = "A"
            elif grade >= 80:
                letter_grade = "B"
            elif grade >= 70:
                letter_grade = "C"
            elif grade >= 60:
                letter_grade = "D"
            else:
                letter_grade = "F"
            
            # Print the corresponding letter grade
            print("The corresponding letter grade is:", letter_grade)
            
            # Break out of the loop since valid input was received
            break
        else:
            # Display an error message for invalid input
            print("Invalid input! Please enter a numerical grade between 0 and 100.")
    except ValueError:
        # Display an error message for invalid input
        print("Invalid input! Please enter a numerical grade.")

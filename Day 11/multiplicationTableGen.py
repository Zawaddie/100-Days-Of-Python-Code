while True:
    try:
        number = int(input("Enter a number: ")) # Prompt the user to enter a number

        if number > 0:                         # Validate the input to ensure it is a positive integer
            for i in range(1, 11):             # Generate the multiplication table using a for loop
                product = number * i
                print(f"{number} x {i} = {product}")

            break                              # Break out of the loop since valid input was received
        else:
            print("Invalid input! Please enter a positive integer.")  # Display an error message for invalid input
    except ValueError:
        print("Invalid input! Please enter a number.")          # Display an error message for invalid input

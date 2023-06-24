## NUMBER GUESSING GAME 02 :

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize a variable to keep track of the number of attempts
attempts = 0

# Start the game loop
while True:
    # Prompt the user to enter a guess
    guess = int(input("Guess a number between 1 and 100: "))

    # Increment the number of attempts
    attempts += 1

    # Compare the guess to the secret number and provide feedback
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the number correctly in", attempts, "attempts.")
        break


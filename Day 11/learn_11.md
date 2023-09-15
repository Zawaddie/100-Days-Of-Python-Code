# On Day 11

## Flow Control Challenges:

## 01: Grade Classifier 01
Write a Python program that prompts the user to enter a numerical grade between 0 and 100, and then prints the corresponding letter grade based on the following grading scale:

                90 and above: A
                80 to 89: B
                70 to 79: C
                60 to 69: D
                Below 60: F
Your program should validate the input to ensure it is within the valid range (0 to 100) and handle any invalid input appropriately.

## Solution 01
Use a while loop to repeatedly prompt the user for input until a valid numerical grade is entered. Use a try-except block to catch any ValueError that may occur if the user enters a non-integer value.

Inside the loop, validate the input to ensure it is within the valid range of 0 to 100. 
If the input is valid, Use nested conditional statements (if, elif, and else) to determine the corresponding letter grade based on the given grading scale.
Print the letter grade to the console.

Display an error message and continue the loop until a valid input is provided if the input is invalid.

## 02: Grade Classifier 02
write a python program that prompts the user to enter his score in five subjects,and displays each subject with its grade, the overall mean, overall grade and total marks. grading scale:

                90 and above: A
                80 to 89: B
                70 to 79: C
                60 to 69: D
                Below 60: 
your program should validate the input to ensure it is within the valid range (0 to 100) and handle any invalid input appropriately.

## 03: Number Guessing Game
Write a Python program that generates a random number between 1 and 100 and asks the user to guess the number. The program should provide feedback to the user after each guess, indicating whether the guessed number is too high, too low, or correct.

The program should continue prompting the user for guesses until they guess the correct number. Once the correct number is guessed, the program should display the number of attempts it took the user to guess correctly.

To make the game more interesting, you can provide hints such as "Warmer" or "Colder" based on the proximity of the guessed number to the actual number.


## pseudocode 03
        - import the random module to generate a random number.
        - Use the randint() function to generate a random number between 1 and 100 and store it in the secret_number variable.
        - Initialize a variable called 'attempts' to keep track the number of attempts made by the user.
        - Start the game loop using a while loop that continues until the user guesses the correct number. 
        - Inside the loop, prompt the user to enter a guess and convert it to an integer using the int() function.
        - After each guess, increment the attempts variable by 1.
        - Compare the guess to the secret number using conditional statements (if, elif, else) 
        - Provide feedback to the user based on whether the guess is too low, too high, or correct.   
        - If the guess is correct, break out of the loop and display the number of attempts it took to guess correctly.


## 04: Challenge: Multiplication Table Generator
Write a Python program that prompts the user to enter a number, and then generates the multiplication table for that number up to 10.

Your program should validate the input to ensure it is a positive integer. If the input is invalid, display an error message and prompt the user again.

## pseudocode 04
        - Use a while loop to repeatedly prompt the user for input until a valid positive integer is entered. 
        - Use a try-except block to catch any ValueError that may occur if the user enters a non-integer value.
        - Inside the loop, validate the input to ensure it is a positive integer.  
        - If the input is valid, use a for loop to iterate from 1 to 10 (inclusive) and generate the multiplication table for the given number. 
        - Calculate the product by multiplying the current number with the input number, and then print each equation using formatted strings.
        - If the input is invalid, display an error message and continue the loop until a valid input is provided.
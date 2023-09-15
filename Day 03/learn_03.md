# On Day 03
Ifocussed on basic input/output. it was a day of learning how to talk to a computer!!!

## INTERACT WITH A USER
A program can ask a user to enter data, read the data entered by a user and return the same data to a running program. This make the program  trullyinteractive.

         

## input() 
Reads data entered by a user and returns the same data to the running program.

Can be:

         - without an argument
         - with an argument

For input() without an argument the fuction is invoked without arguments. The function switches the console into input mode by displaying a blinking cursor that helps the user to input some keystrokes and hitting enter when done.The inputed data is set to the program and manipilated by the program.

            print("what is your name?: ")
            name = input()
            print("Hi " + name)

For input() with an argument, the input() is invoked with one argument ie a string containing the message to the user and it is stored in a variable. The message is is displayed on the console takes in the user input and when called from the programt throgh print() the input is displayed on the console.
The purpose of this is to simplify the code:
 
            name= input("what is your name?: ")
            print("Hi " + name)

## Typecasting/Type conversions
The result of an input() is always a string containing all the characters the user enters from the keyboard even if they contain numbers. These results cant be used in arithmetic operations.

Hence the use of the simple functions to convert the string output into an integer, float and boolean respectively.

           int(string)
           float(string)
           bool(string)
       
str() is used to convert other data types into a string.

           year_of_birth = input(" enter year of birth")
           age = 2023 - int(year_of_birth)
           print(age)

## more on input()
The print() can accept an expresiion as an argument, so I dont have to first store an expression into a variable.

            length = float(input("enter the length: "))
            width = float(input("enter the width: "))
            print("the area is: " ,(length*width))

           

## challenge_03

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. 

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
Print out that many copies of the previous message on separate lines. 


# On Day 5
Logical and comparison operators.

## COMPARISON OPERATORS
            a > b    (greater than)
            a >= b   (greater than or equal to)
            a < b    (less than)
            a <= b   (less or equal to)
            a == b   (equals)
            a != b   (not equals)

## LOGICAL OPERATORS
logical operators are used to combine and manipulate logical values (Boolean values) to evaluate conditions and make decisions in your code.

         and: 
         returns True if both operands are True, and False otherwise. It evaluates the expressions from left to right and stops as soon as it finds a False value.

         or: 
         returns True if at least one of the operands is True, and False if both operands are False. It evaluates the expressions from left to right and stops as soon as it finds a True value.

         not: 
         a unary operator that returns the opposite of the operand's logical value. If the operand is True, not returns False, and if the operand is False, not returns True.

Here's an example to illustrate the usage of logical operators:

         if has_high_income and has_good_credit: 
         ...
         if has_high_income or has_good_credit: 
         ...
         is_day = True
         is_night = not is_day

Consider three variables: x, y, and z. 
We use logical operators to evaluate different conditions:

         x < y and y < z 

uses the and operator to check if both conditions are true. Since x < y and y < z are both true, the result is True.

         x > y or y < z 

uses the or operator to check if at least one of the conditions is true. Since y < z is true, the result is True.

         not (x == y) 
uses the not operator to negate the logical value of x == y. Since x is not equal to y, the result is True.

Logical operators are useful for:
      - creating conditional statements, 
      - making comparisons, and 
      - combining multiple conditions to control the program's flow based on logical evaluations.

## Challenge_05
write a program that allows the user to enter their weights in the kilograms or pounds and then converts the user weight input to the othr unit.

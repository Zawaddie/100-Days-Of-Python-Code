# On Day 06

# CONDITIONAL STATEMENTS:
 When you want to execute some code only if a certain condition is met, you can use a conditional statement:
            If-
            if-else
            if-elif-else

## A single if statement:
If the condition evaluates to True, the perform_if_condition_true statement is executed, and the conditional statement comes to an end;
If the condition evaluates to False, the perform_if_condition_false statement is executed, and the conditional statement comes to an end.

            if true_or_not:        # condition
                do_this_if_true    # Executed if the condition is True.
            
for instance:            
           
            x = 20

            if x == 20: 
                print("x is equal to 20")  

 ## Multiple if statements:
Includes a number of 'if' statements and each 'if' statement is tested separately.
            x = 20

            if x > 5:                         # 1st condition 
                print("x is greater than 5")  # Executed if the 1st condition is True.

            if x < 20:                        # 2nd condition 
                print("x is less than 20")    # Executed if the 2nd condition is True.

            if x == 20:                       # 3rd condition   
                print("x is equal to 20")     # Executed if condition three is True.

## An if-else statement:
condition is evaluated whether true or false, if true first action is performed , else  the second action is performed.

            if true_or_false_condition:
                perform_if_condition_true
            else:
                perform_if_condition_false
for instance:
          
             x = 20

             if x < 20: 
                 print("x is less than 20") 

             else:
                 print("x is greater than or equal to 20")

## multiple if statements followed by an else:
 Each 'if' is tested separately and then he body of 'else' is executed if the last 'if' is evaluated as False.           
             x = 20

             if x > 5: 
                 print("x is greater than 5")  

             if x < 20: 
                 print("x is less than 20")  

             if x == 20: 
                 print("x is equal to 20")  

             else:
                 print("the number is unaccepted!!")

## The if-elif-else statement:
The program checks the conditions of the subsequent elif blocks, If the condition for if is False.  The first elif block that is True will be executed. If all the conditions are False, the else block will be executed.
               
             x = 20

            if x == 20:                     # True
                print("x == 20")

             if x > 15:                     # False
                print("x > 15")

            elif x > 20:                     # False
                    print("x > 20")

            elif x > 5:                  # True
                print("x > 5")

            else:
                print("else will not be executed")

I
## Nested Conditional statements:
                
            x = 10

            if x > 5: # True
                if x == 6: # False
                    print("nested: x == 6")
                elif x == 10: # True
                    print("nested: x == 10")
                else:
                    print("nested: else")
            else:
                 print("else")



## Nested if-else statements
Now let's discuss two special cases of the conditional statement.

First, consider the case where the instruction placed after the if is another if.

Let's write the same in Python. Consider carefully the code here:


            if the_weather_is_good:
                if nice_restaurant_is_found:
                    have_lunch()
                else:
                    eat_a_sandwich()
            else:
                if tickets_are_available:
                    go_to_the_theater()
                else:
                    go_shopping()

Here are two important points:

this use of the if statement is known as nesting; remember that every else refers to the if which lies at the same indentation level; you need to know this to determine how the ifs and elses pair up;
consider how the indentation improves readability, and makes the code easier to understand and trace.
The elif statement
The second special case introduces another new Python keyword: elif. As you probably suspect, it's a shorter form of else if.

elif is used to check more than just one condition, and to stop when the first statement which is true is found.

Our next example resembles nesting, but the similarities are very slight. Again, we'll change our plans and express them as follows: If the weather is fine, we'll go for a walk, otherwise if we get tickets, we'll go to the theater, otherwise if there are free tables at the restaurant, we'll go for lunch; if all else fails, we'll stay home and play chess.

Have you noticed how many times we've used the word otherwise? This is the stage where the elif keyword plays its role.

Let's write the same scenario using Python:


            if the_weather_is_good:
                go_for_a_walk()
            elif tickets_are_available:
                go_to_the_theater()
            elif table_is_available:
                go_for_lunch()
            else:
                play_chess_at_home()
            
The way to assemble subsequent if-elif-else statements is sometimes called a cascade.

Notice again how the indentation improves the readability of the code.

Some additional attention has to be paid in this case:

you mustn't use else without a preceding if;
else is always the last branch of the cascade, regardless of whether you've used elif or not;
else is an optional part of the cascade, and may be omitted;
if there is an else branch in the cascade, only one of all the branches is executed;
if there is no else branch, it's possible that none of the available branches is executed.
This may sound a little puzzling, but hopefully some simple examples will help shed more light.
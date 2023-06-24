# On Day 06

# FLOW CONTROL: 
 Flow control in Python refers to the mechanisms and constructs that allow you to control the execution flow of your program. It enables you to dictate which statements are executed and in what order, based on certain conditions or criteria. 
 
 Flow control helps you create logic, make decisions, and perform different actions depending on specific conditions.

 Thus, by utilizing different flow control mechanisms, you can create programs that make decisions, repeat tasks, handle errors, and control the logical flow of your code based on specific conditions and requirements.

 ## FLOW CONTROL: Conditional statements:
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

            elif x > 5:                      # True
                print("x > 5")

            else:
                print("else will not be executed")

I
## Nested Conditional statements:
NESTING in 'if' statements refers to the practice of including one or more 'if' statements within another 'if' statement. This allows for the creation of more complex conditional structures and the evaluation of multiple conditions in a hierarchical manner.

By nesting 'if' statements, you can specify different sets of conditions to be evaluated based on the outcome of the outer condition. The inner 'if' statements are only executed if the corresponding outer condition is true. This allows for the creation of more fine-grained and specific logic in your code.             
            x = 20

            if x > 5: # True
                if x == 6: # False
                    print("nested: x == 6")
                elif x == 10: # True
                    print("nested: x == 10")
                else:
                    print("nested: else")
            else:
                 print("else")


# challenge_06: 
Write a Python program that prompts the user to enter a numerical grade between 0 and 100, and then prints the corresponding congraturatory message based on the following grading scale:

                90 and above: good job ( >=95 excellent )
                80 to 89: well done
                70 to 79: keep it up
                60 to 69: average
                Below 60: needs improvement

# On day 23

## OOP basic concept Summary:

1. Attributes are the characteristics or properties of an object that store data within objects.
In OOP, there are two types of attributes: 

            instance attributes 
            class attributes.

2. Instance attributes are specific to each object instance. They are defined within the methods of a class, typically in the __init__ method. Each object has its own set of instance attributes.
3. Class attributes are shared among all instances of a class. They are defined directly within the class body, outside any methods. Class attributes are the same for all objects of that class.
4. Instance attributes are accessed using the self parameter within methods, while class attributes are accessed using the class name.
5. Instance attributes can hold different values for each object, allowing objects to have unique states.

6. Class attributes have the same value across all objects of a class and are useful for storing data that is common to all instances.
7. Instance attributes are usually defined and accessed within instance methods, while class attributes are often used within class methods or accessed directly using the class name.
8. When accessing attributes, Python searches for the attribute first in the instance's namespace (instance attributes), then in the class's namespace (class attributes).


## Challenge_23: BankAccountClass
Create a class called BankAccount that represents a bank account. The class should have the following attributes and methods:

 1. Attributes:  
    account_number: a unique identifier for the bank account
        balance: the current balance of the bank account
        
2. Methods:  
deposit(amount): adds the specified amount to the account balance

   withdraw(amount): subtracts the specified amount from the account balance

   get_balance(): returns the current account balance as a string
        
3. Instructions:  
- Define the BankAccount class with the required attributes and methods.
- Implement the deposit() method to add the specified amount to the balance
- Implement the withdraw() method to subtract the specified amount from the balance, but only if there are sufficient funds.
- Implement the get_balance() method to return the current balance as a string.
- Create an object of the BankAccount class.
- Test the behavior of the methods by making deposits, withdrawals, and checking the balance.
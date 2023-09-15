# On Day 21 

# OOP Concepts: classes, objects, attributes, methods
OOP is a programming paradigm that organizes code around the concept of objects, which are instances of classes.  
OOP provides a way to structure and design code by modeling real-world objects and their interactions.

Classes, objects, attributes, and methods form the building blocks of OOP in Python. They allow you to create reusable and modular code, model real-world entities, and implement complex behaviors and interactions. 

Objects are created from classes, which serve as blueprints or templates for defining their structure and behavior.  
Each object has its own state (data or attributes) and behavior (methods or functions). 

The attributes represent the properties or characteristics of the object, while the methods define the actions or operations that the object can perform.

## Classes:

A class is a blueprint or template for creating objects. It defines the common attributes and behaviors that objects of that class will have. 

Classes are created using the class keyword followed by the class name. 

    class MyClass:

Inside a class, you can define attributes (variables) and methods (functions) that belong to the class.

## Objects:

An object is an instance of a class. It represents a specific entity or concept based on the class definition.

Objects are created by calling the class as if it were a function.

    my_object = MyClass()

Each object has its own unique identity and can have its own set of attribute values. However, all objects of the same class share the same set of methods defined in the class.

## Attributes:

Attributes are the characteristics or properties of an object. They store data associated with an object and define its state.
There are two types of attributes in Python classes:

    Instance attributes: 
    These are specific to each object instance and are defined inside the '__init__ ' method of the class. Instance attributes are accessed using the self keyword within methods of the class.

    Class attributes: 
    These are shared among all instances of the class. They are defined directly within the class body, outside any methods. Class attributes are accessed using the class name or an instance of the class.

## Methods:

Methods are functions defined within a class that perform specific actions or operations on objects of that class.
Like attributes, there are two types of methods in Python classes:

    Instance methods: 
    These methods operate on individual object instances and have access to the instance's attributes using the self parameter.

    Class methods: 
    These methods operate on the class itself rather than individual instances. They are defined using the @classmethod decorator and have access to class-level attributes and methods.

Attributes and methods are accessed using dot notation.

    my_object.attribute 
    (retrieves the value of the attribute from the object)
    
    my_object.method() 
    (calls the method on the object)

## The __init__ method 
It's a special method/constructor. 
It is automatically called when an object of a class is created. 
The purpose of the __init__ method is to initialize the attributes of the object.

The __init__ method is defined within a class.

Syntax:


            def __init__(self, parameter1, parameter2, ...):
                   # Initialization code

        Name: 
        The method name is always __init__. It should always be spelled with two underscores on each side.

        Parameters: 
        The self parameter is required as the first parameter. It represents the instance of the class being created. You can also define additional parameters to accept values that will be used to initialize the attributes of the object.

        Initialization: 
        Inside the __init__ method, you can write code to initialize the attributes of the object based on the provided values. Typically, this is done by assigning the parameter values to the corresponding instance attributes using dot notation (self.attribute = parameter).

The __init__ method allows you to set up the initial state of the object by assigning values to its attributes. Whenever an object is created from the class, the __init__ method is automatically called, ensuring that the object is properly initialized.

By defining the __init__ method and providing the necessary parameters, you can create objects with different initial attribute values. This allows for greater flexibility and customization when working with objects of a class.

Example usage:

        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        person1 = Person("Alice", 25)
        person2 = Person("Bob", 30)

        print(person1.name, person1.age)  # Output: Alice 25
        print(person2.name, person2.age)  # Output: Bob 30

The __init__ method is used to initialize the 'name' and 'age 'attributes of the Person objects. When creating 'person1' and 'person2', the values passed as arguments are used to set the respective attributes for each object.

The __init__ method is a powerful tool in Python classes. It allows you to customize object initialization and ensure that objects start with the desired initial state.

## Challenge_21:
Create a class called Rectangle that represents a rectangle shape. 

1. Attributes:
    width: representing the width of the rectangle
    height: representing the height of the rectangle

2. Methods:
    get_area(): calculates and returns the area of the rectangle
    get_perimeter(): calculates and returns the perimeter of the rectangle
  
3. Instructions:
- Define the Rectangle class with the required attributes and methods.
- Implement the 'get_area()' method to calculate the area of the rectangle using the formula: 'area = width * height.'
- Implement the 'get_perimeter()' method to calculate the perimeter of the rectangle using the formula: perimeter = 2 * (width + height).
- Create an object of the Rectangle class and assign appropriate values to its attributes.
- Call the 'get_area()' and 'get_perimeter()' methods on the object and print the results.
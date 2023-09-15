# OnDay 24:

# Inheritance in OOP:
A key concept of OOP that allows a class to inherit properties and behaviors from another class. 
The class that inherits from another class is the Child class. The class from which the derived class inherits is the  parent class.

Inheritance provides:

1. Code Reusability: 
Allows you to define common attributes and methods in a base class and reuse them in multiple derived classes. Helps avoid code duplication and promotes modular design.

2. Hierarchy and Organization: 
Allows you to create a hierarchy of classes, where derived classes inherit attributes and behaviors from their parent classes. This helps organize and structure code by representing relationships and specialization.

2. Overriding and Extension: 
Child classes can override methods and attributes inherited from the parent class, providing their own implementation or modifying the existing behavior. This allows customization and extension of functionality.

To define inheritance in Python, you specify the base class in parentheses after the derived class name when defining the class. The derived class inherits all the attributes and methods of the base class. Here's the syntax:

            class ParentClass:
                # parent class definition

            class ChildClass(ParentClass):
                # Derived class definition
            
The 'ChildClass' inherits from 'ParentClass'. The child class can access and use the attributes and methods of the parent class, and it can also define its own additional attributes and methods.


# Method Overriding:
-A feature of inheritance that allows a derived class to provide its own implementation of a method inherited from the parent class.
- When a method is called on an object, Python first checks if the method is defined in the derived class. If found, it uses the implementation from the derived class.
- Allows the derived class to modify the behavior of an inherited method to suit its specific requirements.
- It is accomplished by defining a method in the derived class with the same name as the method in the parent class, effectively replacing the inherited method.

# Challenge 24:
Create a base class called Animal with:
1. Attributes:
name: representing the name of the animal

2. Methods:
speak(): prints a generic message indicating that the animal is making a sound
Create two derived classes called Dog and Cat that inherit from the Animal class. Each derived class should have its own unique sound and implement the speak() method to print the specific sound of the animal.

3. Instructions:
- Define the Animal class with the name attribute and the speak() method.
- Implement the speak() method in the Animal class to print a generic message.
- Define the Dog class that inherits from the Animal class.
- Implement the speak() method in the Dog class to print the sound "Woof!"
- Define the Cat class that inherits from the Animal class.
- Implement the speak() method in the Cat class to print the sound "Meow!"
- Create instances of the Dog and Cat classes and test the speak() method for each instance.
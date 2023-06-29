# On Day 12:

# Data strustures in python:
Are containers that hold and organize data in a specific format, allowing for efficient storage, retrieval, and manipulation of data. Python provides several built-in data structures that can be used to store and manage collections of related data.

There are both built-in data structures provided by the language itself and non-built-in data structures that can be implemented by the programmer or imported from external libraries. 

Built-in Data Structures:Lists,Tuples,Sets,Dictionaries,Strings,Arrays,Other numeric types: Integers, floats, complex numbers, etc.

Non-Built-in Data Structures:(Linked Lists,Stacks,Queues,Trees,Graphs,Hash Tables,Heaps, Tries, Deques)

# Data Structures: LISTS
A commonly used data structure that allows you to store and manipulate a collection of items. 

Features:

     1. A defined by enclosing a comma-separated sequence of items within square brackets ([])
          
             myList = [1, 2, 3, 4, 5].

     2. They are mutable/can be modify their elements after creation. 

     3. Elements in a list are ordered and can be accessed using their index. The first element has 
        an index of 0. 
          
             myList[0]       # returns the first element.

     4. The length of a list can be obtained using the len() function.
            
             length = len(myList).

     5. Supports slicing, allowing you to access a subset of elements. Slicing is done using the 
      colon (:) operator. 
      
             myList[1:4]          #returns a new list containing elements from index 1 to 3.

     6. adding elements to the end of a list using the append() method. 
             
             myList.append(10)    # adds the element 10 to the end of the list.

     7. Concatenation: Lists can be concatenated using the + operator. 
             
             new_list = my_list + [7, 8, 9] 

     8. Lists can be iterated using loops, such as for and while, to access each element in the list.
      
Common List Methods: Lists have various useful methods like 

              insert()
              remove()
              pop()
              sort(), 
              reverse(), 
              index(), 
              count(), .



## Challenge_12: Lists Operations

Rembering to use appropriate list methods and operations, write a Python program that performs the following operations on a list:

         1. Create an empty list called numbers.
         2. Prompt the user to enter five integers, one at a time. Add each entered integer to the
            numbers list.
         3. Print the list numbers in its original order.
         4. Sort the numbers list in ascending order.
         5. Print the sorted list.
         6. Find and print the maximum value and the minimum value from the numbers list.
         7. Calculate and print the sum of all the elements in the numbers list.
         8. Prompt the user to enter a number to search for in the numbers list. Check if the number
            is present in the list and print an appropriate message.
         9. Remove the first occurrence of the number entered in step 8 from the numbers list.
         10.Print the final contents of the numbers list.






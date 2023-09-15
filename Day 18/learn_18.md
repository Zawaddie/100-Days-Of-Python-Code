# On Day 18

# Data Structures: DICTIONARIES
Are unordered, mutable data structures that store key-value pairs.
They provide an efficient way to store and retrieve data by using keys to access corresponding values.

## characteristics of dictionaries:
### Key-Value Pairs: 
Consist of key-value pairs enclosed in curly braces { }.  
Each key is unique within the dictionary, and it is associated with a corresponding value.   
Keys can be of any hashable data type, such as strings, numbers, or tuples.

### Unordered: 
The order of elements is not preserved.   
The order of items may vary when iterating over a dictionary.  
In Python versions 3.7 and later, dictionaries maintain the insertion order.

### Mutable: 
You can add, update, or delete key-value pairs after the dictionary is created. 
You can modify the value associated with a specific key or add new key-value pairs to the dictionary.

### Dynamic Size: 
Can grow or shrink dynamically as you add or remove key-value pairs.  
They can store a variable number of items based on your needs.

### Fast Access: 
provide fast access to values by using keys. The retrieval of values is optimized using a hash function that maps keys to their corresponding locations in memory. This allows for efficient lookup of values even in large dictionaries.

### Iterability: 
You can iterate over dictionaries using loops to access each key-value pair.  
The for loop is commonly used for dictionary iteration.

### Key-Based Lookup: 
Allow you to access values by using keys. Given a key, you can retrieve the associated value from the dictionary. If a key is not present, it raises a KeyError unless you use the get() method, which returns a default value instead.

### No Duplicate Keys: 
Do not allow duplicate keys. If you try to assign a value to an existing key, it updates the value associated with that key instead of creating a new entry.

## Use cases:

        - Storing and retrieving data based on a key.
        - Implementing lookup tables or mappings.
        - Counting occurrences or frequencies of elements.
        - Configurations and settings storage.
        - Caching or memorization of expensive function calls.
        - Representing complex data structures or relationships.
        - By understanding dictionaries in Python, you can leverage their power to efficiently organize, access, and manipulate data using key-value pairs

## Challenge_18:  Phonebook

Write a Python program that allows the user to manage a phonebook. The program should provide the following functionality:

    1. Allow the user to add a new contact to the phonebook. Each contact should have a name and a corresponding phone number. The program should prevent duplicate entries.

    2. Allow the user to search for a contact by name and display their phone number if found. If the contact is not found, display a message indicating that the contact is not in the phonebook.

    3. Allow the user to remove a contact from the phonebook by providing the name of the contact. If the contact is not found, display a message indicating that the contact is not in the phonebook.

    4.Allow the user to view all contacts in the phonebook, displaying both the name and phone number for each contact.

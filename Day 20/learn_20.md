# On Day 20

# File Handling in Python:
considered the following under python file handling: 

    - Opening and closing files in Python
    - Reading and writing text files
    - Reading and writing binary files
    - Different modes for file handling (read mode, write mode, append mode, etc.)
    - File object methods for reading, writing, and manipulating files (e.g., read(), write(), seek 
      (), tell())
    - Handling file exceptions and errors
    - Working with file paths and directories
    - Context managers and the with statement for automatic file closing

## Opening files in Python:
To open a file, you use the in-built open() function, which takes two parameters: the FILE NAME (including the path if necessary) and the MODE in which you want to open the file.  

The mode specifies whether you want to read, write, or append to the file. 
The most common modes are:

      'r': Read mode (default). Opens the file for reading.

      'w': Write mode. Opens the file for writing. Creates a new file if it doesn't exist, or truncates the existing file.

      'a': Append mode. Opens the file for appending. Creates a new file if it doesn't exist.

      'x': Exclusive creation mode. Creates a new file, but raises an error if the file already exists.

To open a file in write mode:

      file = open('example.txt', 'w')

Here, we open the file named "example.txt" in write mode.  
If the file doesn't exist, it will be created.  
If it does exist, its contents will be truncated.

### Closing Files in python:
After you are done working with a file, you can close it using the close() method. 
Closing the file ensures that any buffered data is written to the file and releases system resources associated with the file.

To close a file:

    file.close()

Here, file is the file object that was opened previously using open().  
Calling close() on the file object closes the file.


## with Statement:
Python also provides a more convenient way for automatically closing files using the "with" statement.

The statement creates a temporary scope where the file is opened, and it automatically takes care of closing the file when the block is exited.

    with open('example.txt', 'w') as file:
        file.write('Hello, world!')    # Perform file operations

Here, the open() function is used within a 'with ;statement. The file is automatically closed when the block is exited, even if an exception occurs.

Using the with statement is generally a best practice for working with files in Python.

Always handle file exceptions appropriately and perform necessary error handling when working with files in your programs.

## Reading Text Files:
File object's methods used:

      read()
      readline()

The read() method reads the entire contents of the file as a single string.

The readline() method reads a single line from the file.

    with open('example.txt', 'r') as file:
        contents = file.read()
        print(contents)

Here, the with statement is used to open the file in read mode and create a file object.  
The read() method is then called on the file object to read the entire contents of the file into the contents variable. Finally, the contents are printed.

To read the file line by line, use the readline() method in a loop:

    with open('example.txt', 'r') as file:
        line = file.readline()
        while line:
            print(line)
            line = file.readline()

Here, the readline() method is called within a loop. The loop continues until there are no more lines to read from the file.

## Writing Text Files:
File object's methods used:

      write()
      writelines()

The write() method writes a string to the file.

The writelines() method writes a list of strings to the file.

    with open('example.txt', 'w') as file:
        file.write('Hello, world!')

Here, the with statement is used to open the file in write mode and create a file object.  
The write() method is then called on the file object to write the string 'Hello, world!' to the file.

To write multiple lines or a list of strings:

    lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']

    with open('example.txt', 'w') as file:
        file.writelines(lines)

Here, the writelines() method is called with a list of strings lines. Each string represents a line of text to be written to the file.

## Reading Binary Files:
Use the file object's read() method with the appropriate mode for binary file operations:

    with open('example.bin', 'rb') as file:
        data = file.read()
        print(data)

Here, the with statement is used to open the file in read mode with binary mode specified as 'rb'.  
The read() method is called on the file object to read the entire contents of the binary file into the data variable. Finally, the binary data is printed.

## Writing Binary Files:
Use the file object's write() method:

    with open('example.bin', 'wb') as file:
        data =b'\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21'
        file.write(data)
        
Here, the 'with' statement is used to open the file in write mode with binary mode specified as 'wb'.  
The write() method is then called on the file object to write binary data to the file. The binary data is represented as a bytes literal b'\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21'.

## Handling File Exceptions and Errors:
Handle potential exceptions and errors that may occur. 
Common file-related exceptions:  

    FileNotFoundError (when the file doesn't exist)
    PermissionError (when the file cannot be accessed due to permissions)
    IOError (for general I/O errors)

handle these exceptions using try-except blocks to gracefully handle errors and provide appropriate error messages to the user.

### Working with File Paths and Directories:
The 'os' module provides functions for working with file paths and directories in a platform-independent manner. 

Functions useful for manipulating file paths and checking the existence or properties of files and directories:

    os.path.join()
    os.path.exists()
    os.path.isdir()
    os.listdir()  


## Challenge_20: Word Counter
Write a Python program that reads a text file and counts the occurrence of each word in the file. The program should then display the words along with their corresponding counts in descending order of frequency.


    1. Ask the user to enter the path to the text file they want to analyze.
    2. Open the file in read mode and read its contents.
    3. Split the contents into individual words, removing any leading or trailing whitespace and punctuation marks.
    4. Create a dictionary to store the word counts.
    5.Iterate through each word and update its count in the dictionary.
    6. Sort the dictionary by value (count) in descending order.
    7. Display the words along with their counts.
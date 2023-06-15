## On Day 01
I prepared my python Development Environment and started out on the challenge with the basic python syntax and data types:

## Variables and their assignments
Variables temporarily store data in computer’s memory. Acts as an address pointing to specific stored data
syntax:     variable_name = value
     price = 10 
     rating = 4.9 
     course_name = ‘Python for Beginners’ 
     is_published = True

## Data Types
  • price is an integer (a whole number without a decimal point) 
  • rating is a float (a number with a decimal point) 
  • course_name is a string (a sequence of characters) 
  • is_published is a boolean. Boolean values can be True or False. 

## Comments 
used to add notes to code by explaining the hows and whys, not what the code does. That should be reflected in the code itself. 

## Strings 
single (‘ ‘) or double (“ “) quotes defines strings 
A multi-line string surrounded with tripe quotes (“””). 
We can get individual characters in a string using square brackets []. 
     course = ‘Python for Beginners’
     course[1] # returns the second character
     course[-1] # returns the first character from the end 
     course[-2] # returns the second character from the end
We can slice a string using a similar notation: 
    course[1:5] 
The above expression returns all the characters starting from the index position of 1 
to 5 (but excluding 5). The result will be ytho 
If we leave out the start index, 0 will be assumed. 
If we leave out the end index, the length of the string will be assumed. 

## Formatted strings
We can use formatted strings to dynamically insert values into our strings: 
     name = ‘Mosh’ 
     message = f’Hi, my name is {name}’
     message.upper() # to convert to uppercase
     message.lower() # to convert to lowercase
     message.title() # to capitalize the first letter of every word
     message.find(‘p’) # returns the index of the first occurrence of p (or -1 if not found) 
     message.replace(‘p’, ‘q’)
To check if a string contains a character (or a sequence of characters), we use the in 
operator: 
     contains = ‘Python’ in course

## Challenge_01
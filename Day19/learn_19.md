# On Day 19

# Regular expressions:
consider:

        - Understanding the syntax and pattern matching rules of regular expressions
        - Metacharacters and character classes in regular expressions
        - Quantifiers and repetition in regular expressions
        - Anchors and boundary matching
        - Grouping and capturing in regular expressions
        - Special sequences and escape characters in regular expressions
        - Regular expression functions and methods in Python 
          (e.g., re.search(), re.match(), re.findall())
        - Modifying and replacing strings using regular expressions

Regular expressions (regex,regexp) are powerful pattern-matching tools. They provide a concise and flexible way to search, match, and manipulate text based on specific patterns.

Are essentially sequences of characters that define a search pattern.  
They allow you to describe complex search patterns by using a combination of metacharacters, special sequences, and literal characters.

## Basic Syntax:

LITERAL CHARACTERS: Regular expressions can contain literal characters, which match themselves exactly.  
For example, the regex abc matches the string "abc" as is.

METACHARACTERS: Metacharacters have special meanings in regular expressions. Some commonly used metacharacters include:  
            a)  . (matches any character)  
            b)  * (matches zero or more occurrences)    
            c)  + (matches one or more occurrences)  
            d)  ? (matches zero or one occurrence)  
            e)  ^ (matches the start of a string)  
            f)  $  matches the end of a string

CHARACTER CLASSES: Character classes are enclosed in square brackets ([]) and allow you to define a set of characters to match. For example, [aeiou] matches any vowel.

QUANTIFIERS: Quantifiers specify the number of occurrences to match.   
For example, a{2,4} matches 2 to 4 occurrences of the letter 'a'.

## Functions and Methods in the re Module:
The Python re module provides functions and methods for working with regular expressions:

    re.search(pattern, string) 
Searches for the pattern anywhere in the string and returns a match object or None.

    re.match(pattern, string)
Matches the pattern at the beginning of the string and returns a match object or None.

    re.findall(pattern, string)
Returns all non-overlapping occurrences of the pattern in the string as a list of strings.

    re.finditer(pattern, string) 
Returns an iterator yielding match objects for all non-overlapping occurrences of the pattern.

    re.sub(pattern, repl, string) 
Replaces all occurrences of the pattern in the string with the replacement string.

    re.split(pattern, string) 
Splits the string by the occurrences of the pattern and returns a list of strings.


## use cases for regular expressions:
Pattern Matching: 

Are commonly used for pattern matching in strings. You can search for specific patterns or sequences of characters within a text.

Text Extraction: 

Enable you to extract specific parts of a text that match a given pattern.  
For example, you can extract email addresses, URLs, or phone numbers from a larger string.

Text Validation: 

Regular expressions are useful for validating whether a string matches a certain pattern or conforms to a specific format. For instance, you can validate email addresses, dates, or credit card numbers.

Text Replacement: 

Regular expressions allow you to perform find and replace operations in strings based on patterns. You can search for a specific pattern and replace it with another string or modify it in some way.

Data Parsing: 

Regular expressions are often used to parse structured or semi-structured data. For example, you can parse log files, CSV files, or HTML/XML documents by extracting relevant information based on specific patterns.

Data Cleaning: 

Regular expressions can be employed to clean up text data by removing unwanted characters, replacing multiple spaces with a single space, or removing HTML tags, among other things.

Text Manipulation: 

Regular expressions provide powerful string manipulation capabilities. You can split strings, join strings, or perform other operations based on pattern matches.

## Special Sequences:

Special sequences are predefined patterns that match common patterns. 

    \d matches any digit, 
    \w matches any alphanumeric character, 
    \s matches any whitespace character
    \b matches a word boundary.

## Challenge_19:

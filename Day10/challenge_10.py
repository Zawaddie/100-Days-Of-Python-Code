def is_palindrome(input_string):
    # Remove spaces and punctuation, and convert to lowercase
    input_string = ''.join(e for e in input_string if e.isalnum()).lower()
    # Check if the input string is equal to its reverse
    return input_string == input_string[::-1]

while True:
    try:
        word = input("Enter a word or phrase: ")
        
        if not word:  # If input is empty, skip processing and prompt again
            print("Input cannot be empty. Please try again.")
            continue

        if is_palindrome(word):
            print("The input is a palindrome.")
        else:
            print("The input is not a palindrome.")

        break  # Exit the loop after processing the input
        
    except Exception as e:
        print("An error occurred:", e)

import string

def count_words(filename):
    word_counts = {}

    # Open the file and read its contents
    with open(filename, 'r') as file:
        # Read the entire file as a string
        text = file.read()

        # Remove punctuation marks
        text = text.translate(str.maketrans('', '', string.punctuation))

        # Split the text into individual words
        words = text.split()

        # Count the occurrence of each word
        for word in words:
            word = word.lower()  # Convert the word to lowercase
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    # Sort the word counts in descending order
    sorted_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Display the word counts
    print("Word Counts:")
    print("-------------")
    for word, count in sorted_counts:
        print(f"{word}: {count}")

# Ask the user to enter the path to the text file
filename = input("Enter the path to the text file: ")

# Call the function to count the words
count_words(filename)

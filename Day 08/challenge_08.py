# WORD COUNTER


sentence = input("Enter a sentence: ")   # prompt the user to enter a sentense

sentence = sentence.strip()              # Remove leading and trailing spaces from the sentence

word_count = 0                           # Initialize a variable to keep track of the word count

for word in sentence.split():            # Use a for loop to iterate over each word in the sentence by splitting it based on spaces using the split() method
    word_count += 1

print("The sentence contains", word_count, "words.")  # Print the final word count

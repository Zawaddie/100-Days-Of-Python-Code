def word_frequency_counter(text):
    words = text.split()
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency


# Prompt the user to enter a text string
text = input("Enter a text string: ")

# Call the word_frequency_counter function
frequency_dict = word_frequency_counter(text)

# Print the word frequency dictionary
print("Word Frequency:")
print(frequency_dict)

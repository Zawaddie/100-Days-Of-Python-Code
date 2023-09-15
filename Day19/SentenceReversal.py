def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = [words[i] for i in range(len(words) - 1, -1, -1)]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Call the function to reverse the sentence
reversed_sentence = reverse_sentence(sentence)

# Display the reversed sentence
print("Reversed Sentence:", reversed_sentence)

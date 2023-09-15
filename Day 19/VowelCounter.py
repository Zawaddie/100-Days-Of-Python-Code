def vowel_counter(sentence):
    vowels = 'aeiou'
    counts = [(vowel, sentence.lower().count(vowel)) for vowel in vowels]
    sorted_counts = sorted(counts, key=lambda x: x[1], reverse=True)
    return sorted_counts

# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Call the function to count the vowel occurrences
vowel_counts = vowel_counter(sentence)

# Display the vowel counts
print("Vowel Counts:")
print("-------------")
for vowel, count in vowel_counts:
    print(f"{vowel}: {count}")

# Program to find the longest word in a sentence

sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Assume first word is longest
longest_word = words[0]

# Loop through words
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("The longest word is:", longest_word)
print("Length:", len(longest_word))
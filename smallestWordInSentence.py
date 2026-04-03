# Program to find the smallest word in a sentence

sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Assume first word is smallest
smallest_word = words[0]

# Loop through words
for word in words:
    if len(word) < len(smallest_word):
        smallest_word = word

print("The smallest word is:", smallest_word)
print("Length:", len(smallest_word))
# Program to count total number of words

sentence = input("Enter a sentence: ")

# Split sentence into words using space
words = sentence.split()

# Count the words
total_words = len(words)

print("Total number of words:", total_words)
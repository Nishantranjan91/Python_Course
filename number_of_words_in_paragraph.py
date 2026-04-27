import re

paragraph = input("Enter a paragraph: ")

# Find all words using regex
words = re.findall(r'\b\w+\b', paragraph)

print("Number of words:", len(words))
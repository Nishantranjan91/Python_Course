def is_meaningful(word):
    dictionary = {"hello", "world", "python", "india", "school", "computer"}

    if word.lower() in dictionary:
        return True
    return False

# Input
word = input("Enter a word: ")

if is_meaningful(word):
    print("✅ Meaningful word")
else:
    print("❌ Not meaningful")
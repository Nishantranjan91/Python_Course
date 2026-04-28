char = input("Enter a character: ")

if len(char) != 1:
    print("Please enter only one character.")
else:
    print("ASCII value is", ord(char))
# Program to count vowels in a line

line = input("Enter a line: ")

count = 0
vowels = "aeiouAEIOU"

for ch in line:
    if ch in vowels:
        count += 1

print("Total number of vowels:", count)
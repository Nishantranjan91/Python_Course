# Program to check divisibility by 9

num = input("Enter a number: ")

digit_sum = 0

for digit in num:
    digit_sum += int(digit)

if digit_sum % 9 == 0:
    print("The number is divisible by 9")
else:
    print("The number is NOT divisible by 9")
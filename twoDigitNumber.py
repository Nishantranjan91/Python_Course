# Program to check three-digit number

num = int(input("Enter a number: "))

# Check condition
if 100 <= abs(num) <= 999:
    print("It is a three-digit number")
else:
    print("It is NOT a three-digit number")
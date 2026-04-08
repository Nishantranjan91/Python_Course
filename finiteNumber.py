import math

# Input number
num = float(input("Enter a number: "))

# Check condition
if math.isfinite(num):
    print("The number is finite")
else:
    print("The number is infinite")
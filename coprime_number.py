# Python program to check co-prime numbers

import math

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd = math.gcd(num1, num2)

if gcd == 1:
    print(num1, "and", num2, "are Co-Prime numbers")
else:
    print(num1, "and", num2, "are not Co-Prime numbers")
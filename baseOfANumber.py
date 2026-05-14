# Python program to find the base number

power = int(input("Enter the power value: "))
exponent = int(input("Enter the exponent value: "))

base = power ** (1 / exponent)

print("Base =", base)
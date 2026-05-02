# Function to calculate geometric mean
import math

def geometric_mean(a, b):
    return math.sqrt(a * b)

# Taking input from user
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

# Calculating and printing result
gm = geometric_mean(x, y)
print("Geometric Mean =", gm)
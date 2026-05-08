import math

# Input sides
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))

# Calculate hypotenuse
c = math.sqrt(a**2 + b**2)

# Display result
print("Hypotenuse =", c)
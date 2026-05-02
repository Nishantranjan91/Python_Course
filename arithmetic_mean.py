# Function to calculate arithmetic mean
def arithmetic_mean(a, b):
    return (a + b) / 2

# Taking input from user
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

# Calculating and printing result
am = arithmetic_mean(x, y)
print("Arithmetic Mean =", am)
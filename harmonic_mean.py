# Function to calculate harmonic mean
def harmonic_mean(a, b):
    return (2 * a * b) / (a + b)

# Taking input from user
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

# Calculating and printing result
hm = harmonic_mean(x, y)
print("Harmonic Mean =", hm)
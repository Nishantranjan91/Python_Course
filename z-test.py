import math

# Input values
p0 = float(input("Enter population proportion (p0): "))
x = int(input("Enter number of success (x): "))
n = int(input("Enter sample size (n): "))

# Sample proportion
p_hat = x / n

# Z-test formula
z = (p_hat - p0) / math.sqrt((p0 * (1 - p0)) / n)

# Output
print("Sample proportion (p̂):", p_hat)
print("Z-value:", round(z, 4))
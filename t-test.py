import math

# Input values
sample_mean = float(input("Enter sample mean: "))
population_mean = float(input("Enter population mean: "))
sample_std = float(input("Enter sample standard deviation: "))
n = int(input("Enter sample size: "))

# T-test formula
t = (sample_mean - population_mean) / (sample_std / math.sqrt(n))

# Output
print("T-value:", round(t, 4))
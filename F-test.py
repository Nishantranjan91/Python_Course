import statistics

# Input sample data
sample1 = list(map(float, input("Enter values of sample 1 (space-separated): ").split()))
sample2 = list(map(float, input("Enter values of sample 2 (space-separated): ").split()))

# Calculate variances
var1 = statistics.variance(sample1)
var2 = statistics.variance(sample2)

# F-test statistic (larger variance / smaller variance)
if var1 > var2:
    F = var1 / var2
else:
    F = var2 / var1

# Output
print("Variance of sample 1:", round(var1, 4))
print("Variance of sample 2:", round(var2, 4))
print("F-value:", round(F, 4))
# Program to calculate variance

# Input data
data = list(map(float, input("Enter data values (space-separated): ").split()))

n = len(data)

# Calculate mean
mean = sum(data) / n

# Calculate variance
variance = sum((x - mean) ** 2 for x in data) / n

# Output
print("Mean:", round(mean, 4))
print("Variance:", round(variance, 4))
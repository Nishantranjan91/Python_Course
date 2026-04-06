# Program to calculate mean

# Input data
data = list(map(float, input("Enter numbers (space-separated): ").split()))

# Calculate mean
mean = sum(data) / len(data)

# Output
print("Mean:", round(mean, 4))
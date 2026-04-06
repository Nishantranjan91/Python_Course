# Program to calculate median

# Input data
data = list(map(float, input("Enter numbers (space-separated): ").split()))

# Sort the data
data.sort()
n = len(data)

# Find median
if n % 2 == 1:
    median = data[n // 2]
else:
    median = (data[n // 2 - 1] + data[n // 2]) / 2

# Output
print("Sorted data:", data)
print("Median:", median)
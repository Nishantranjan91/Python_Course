# Program to calculate average

# Input numbers
numbers = list(map(float, input("Enter numbers (space-separated): ").split()))

# Calculate average
average = sum(numbers) / len(numbers)

# Output
print("Average:", round(average, 4))
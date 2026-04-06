# Program to calculate mode

# Input data
data = list(map(int, input("Enter numbers (space-separated): ").split()))

# Count frequency
freq = {}

for num in data:
    freq[num] = freq.get(num, 0) + 1

# Find maximum frequency
max_freq = max(freq.values())

# Find all modes
modes = [key for key, value in freq.items() if value == max_freq]

# Output
print("Mode(s):", modes)
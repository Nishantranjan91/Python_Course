# Input speeds
speeds = list(map(float, input("Enter speeds separated by space: ").split()))

# Calculate average speed
average_speed = sum(speeds) / len(speeds)

# Output result
print("Average Speed =", average_speed)
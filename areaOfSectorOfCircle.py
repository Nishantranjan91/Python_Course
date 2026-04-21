import math

# Input from user
radius = float(input("Enter the radius of the circle: "))
angle = float(input("Enter the angle of the sector (in degrees): "))

# Calculate area
area = (angle / 360) * math.pi * (radius ** 2)

# Display result
print("The area of the sector is:", area)
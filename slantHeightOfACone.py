import math

# Input from user
radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))

# Calculate slant height
slant_height = math.sqrt(radius**2 + height**2)

# Display result
print("The slant height of the cone is:", slant_height)
def find_hcf(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return abs(a * b) // find_hcf(a, b)

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("LCM of", num1, "and", num2, "is:", find_lcm(num1, num2))
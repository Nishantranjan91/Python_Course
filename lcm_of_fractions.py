import math

def lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

# Input fractions
num1 = int(input("Enter numerator of first fraction: "))
den1 = int(input("Enter denominator of first fraction: "))

num2 = int(input("Enter numerator of second fraction: "))
den2 = int(input("Enter denominator of second fraction: "))

# LCM of fractions
lcm_num = lcm(num1, num2)
hcf_den = math.gcd(den1, den2)

result_num = lcm_num
result_den = hcf_den

print("LCM of fractions is:", result_num, "/", result_den)
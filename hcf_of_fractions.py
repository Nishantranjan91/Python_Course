import math

def hcf_fractions(n1, d1, n2, d2):
    # HCF of numerators
    hcf_num = math.gcd(n1, n2)
    
    # LCM of denominators
    lcm_den = abs(d1 * d2) // math.gcd(d1, d2)
    
    return hcf_num, lcm_den

# Input fractions
num1 = int(input("Enter numerator of first fraction: "))
den1 = int(input("Enter denominator of first fraction: "))

num2 = int(input("Enter numerator of second fraction: "))
den2 = int(input("Enter denominator of second fraction: "))

hcf_num, hcf_den = hcf_fractions(num1, den1, num2, den2)

print("HCF of fractions is:", hcf_num, "/", hcf_den)
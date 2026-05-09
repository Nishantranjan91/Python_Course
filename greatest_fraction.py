# Program to find the greatest fraction

from fractions import Fraction

n = int(input("Enter number of fractions: "))

fractions_list = []

for i in range(n):
    frac = input(f"Enter fraction {i+1} (example 3/4): ")
    fractions_list.append(Fraction(frac))

greatest = max(fractions_list)

print("Greatest fraction is:", greatest)
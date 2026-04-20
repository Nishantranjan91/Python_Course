# Input values
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (in years): "))

# Calculate compound amount
amount = principal * (1 + rate / 100) ** time

# Calculate compound interest
compound_interest = amount - principal

# Output result
print("Compound Interest =", compound_interest)
print("Total Amount =", amount)
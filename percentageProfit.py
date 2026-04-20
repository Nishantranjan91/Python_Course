# Input cost price and selling price
cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

# Calculate profit
profit = selling_price - cost_price

# Calculate percentage profit
if cost_price != 0:
    profit_percent = (profit / cost_price) * 100
    print("Profit Percentage =", profit_percent, "%")
else:
    print("Cost price cannot be zero")
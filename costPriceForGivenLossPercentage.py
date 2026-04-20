# Input selling price and loss percentage
selling_price = float(input("Enter Selling Price: "))
loss_percent = float(input("Enter Loss Percentage: "))

# Calculate cost price
if loss_percent < 100:
    cost_price = (selling_price * 100) / (100 - loss_percent)
    print("Cost Price =", cost_price)
else:
    print("Loss percentage should be less than 100")
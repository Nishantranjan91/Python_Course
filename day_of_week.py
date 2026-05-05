import datetime

# Input date (year, month, day)
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

date = datetime.date(year, month, day)

# Get day name
print("Day of the week is:", date.strftime("%A"))
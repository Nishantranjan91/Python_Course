import datetime

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

date = datetime.date(year, month, day)

# Week of month calculation
first_day = date.replace(day=1)
week_number = ((date.day + first_day.weekday()) // 7) + 1

print("Week of the month is:", week_number)
# Program to check divisibility by 11

num = input("Enter a number: ")

odd_sum = 0
even_sum = 0

for i in range(len(num)):
    if i % 2 == 0:
        odd_sum += int(num[i])
    else:
        even_sum += int(num[i])

difference = abs(odd_sum - even_sum)

if difference % 11 == 0:
    print("The number is divisible by 11")
else:
    print("The number is NOT divisible by 11")
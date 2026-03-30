n = int(input())

num = abs(n)   # handle negative numbers

sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

# check Harshad condition
if sum_digits != 0 and n % sum_digits == 0:
    print("Harshad Number")
else:
    print("Not Harshad Number")
a = int(input("please tell your number"))
copy = a
rev = 0
while a>0:
    rev = rev * 10 + a % 10
    a = a // 10
if rev == copy:
        print("yes your number is pallindrome")
else:
        print("sorry your number is not pallindrome")    
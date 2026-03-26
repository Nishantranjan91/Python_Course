a = int(input("please tell your number:"))
s = 0
while a>0:
    s = s + a % 10
    a = a // 10
print(f"your digits sum is {s}")
    #sum  of digits of a number 
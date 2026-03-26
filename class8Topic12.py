a =15
dup = a
square = a**2
count = 0
while a > 0:
    count = count+1
    a = a // 10
    extract = square % (10**count)
    if extract == dup:
         print("your number is automorphic")
    else:
         print("sorry the number is not automorphic")      
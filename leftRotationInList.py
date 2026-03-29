a = [10,20,30,40,50]
for i in range(len(a)-1):
    a[i],a[i+1] = a[i+1],a[i]
print(a)
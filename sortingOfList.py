a = [12,13,14,15,16,17,23,24,25,36,78,90]
for i in range(len(a)-1):
    if a[i] < a[i+1]:
        continue
    else:
        print("your list is not sorted")
        break
else:
    print("your list is sorted")

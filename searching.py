a = [23,67,123,1,54,7,98,45,23,13,6,68]
search = 6
for i in range(len(a)):
    if a[i] == search:
        print(f"element found at index {i}")
        break
else:
    print("sorry no such element are exist")   
a = [1,45,23,89,45,90,12,36,82]
max = a[0]
index = 0

for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        index = i
print(f"your maximum element is {max} at index {index}")        
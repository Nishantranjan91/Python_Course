# a = [1,45,23,89,45,90,12,36,82]
# max = a[0]
# index = 0

# for i in range(len(a)):
#     if a[i] > max:
#         max = a[i]
#         index = i
# print(f"your maximum element is {max} at index {index}")      
  





a = [1,45,23,89,45,90,12,36,82]
max = a[0]
max2 = a[0]
index = 0
index2 = 0
for i in range(len(a)):
    if a[i] > max:
        max2 = max
        index2 = index
        index = i
    elif a[i] > max2:
        max2 = a[i]
        index2 = i    
print(f"max {max}at {index} and max2 is {max2} at {index2}")        
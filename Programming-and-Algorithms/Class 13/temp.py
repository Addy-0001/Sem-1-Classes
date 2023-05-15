list1 = [1, 2, 3, 4, 5]
list2 = []
i = len(list1) - 1
while i >= 0:
    list2.append(list1[i])
    i -= 1
print(list2)
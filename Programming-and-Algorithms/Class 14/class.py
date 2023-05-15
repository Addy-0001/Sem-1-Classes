a = [1, 2, 3, 4, 5]
print(a)
a.append(6)
print(a)
a.insert(0, "object")
print(a)
a.extend({7, 8, 9})
print(a)

a.remove(1)
print(a)

a.pop(2)
print(a)

a = [1, 2, 3, 4, 1, 1]
b = []
count = 0

data = ["sunil", "roshan", 29]
print(data)
del data[0]
print(data)
data.clear()
print(data)

data = (1, 2, 3, 4)
# Add 5 to the tuple
list_data = list(data)
list_data.append(5)
data = tuple(list_data)
print(data)

a = {"name": "Adamya",
     "age": 20,
     "name": "School"
     }
print(a)

# make a dictionary with all possible ways
a = dict(name="Adamya", age=20)
print(a)

a = dict([("name", "Adamya"), ("age", 20)])
print(a)

a = dict({"name": "Adamya", "age": 20})
print(a)

a = {"name": "Adamya", 1: [1, 2, 3]}
print(a)

a = dict([("name", "Adamya"), ("age", 20)])
print(a)

data = {"name": "Adamya", "age": 20}
data1 = dict(Name="Adamya", age=20)
print(data.items())
print(data.keys())
print(data.values())

print(data1)

data["Hari"] = '20'

print(data)

print(data.get("name"))

print(data.pop("name"))

print(data.popitem())

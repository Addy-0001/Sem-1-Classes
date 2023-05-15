# 1. What will be the output of the following program?
#  Program
l = [10, 20, 30, 40, 50]
t = ('Sundeep', 25, 79.58)
s = 'set theory'
s1 = set(l)
s2 = set(t)
s3 = set(s)
print(s1)
print(s2)
print(s3)

# 2.  Given a list
#  How will you check whether 30 is present in the list or not?

lst = [10, 25, 4, 12, 3, 8]
for i in lst:
    if i == 30:
        print("30 is present in the list")
    else:
        print("30 is not present in the list")


# 3. Write a Python program to unpack a tuple into several variables.
tup1 = (1, 2, 3, 4, 5, 6)
lst = list(tup1)
for item in lst:
    print(item)

# 4.  Write a Python program to copy a list.
list1 = [1, 2, 3, 4, 5, 6]
list2 = list1.copy()
print(list2)

# 5.  Given a string
#  s = 'Hello'
#  How will you obtain a list['H', 'e', 'l', 'l', 'o'] from it?
s = "Hello"
lst = list(s)
print(lst)

# 6.  Suppose a list has 20 numbers. Write a program that removes all
#  duplicates from this list.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 6, 7, 9, 10, 11, 12]
lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)


# 7. Write a Python program to count the number of even and odd numbers from a series of numbers.
series = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count_even = 0
count_odd = 0
for i in series:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
print("Number of even numbers :", count_even)
print("Number of odd numbers :", count_odd)

# 8. Write a Python program to add an item in a tuple.
tup1 = (1, 2, 3, 4, 5, 6)
print(tup1)
lst = list(tup1)
lst.append(7)
tup2 = tuple(lst)
print(tup2)

# 9. Which of the following is the correct way to create an empty set?
#  s1 = set( )
#  s2 = { }
#  What are the types of s1 and s2? How will you confirm the type?
s1 = set()
s2 = {}
print(type(s1))
print(type(s2))
# Therefore, s1 is a set and s2 is a dictionary.

# 10.  Write a Python program to convert a tuple to a string.
tup1 = ('S', 'u', 'n', 'd', 'e', 'e', 'p')
str1 = ''.join(tup1)
print(str1)

# 11.  Suppose a list contains positive and negative numbers. Write a
#  program to create two lists—one containing positive numbers and
#  another containing negative numbers.

lst = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
lst1 = []
lst2 = []
for i in lst:
    if i > 0:
        lst1.append(i)
    else:
        lst2.append(i)
print(lst1)
print(lst2)


# 12.  Write a Python program to find the length of a tuple.
tup1 = (1, 2, 3, 4, 5, 6)
print(len(tup1))

# 13.  Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
dict1 = {0: 10, 1: 20}
dict1[2] = 30
print(dict1)

# 14. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
dict4 = {}
for d in (dict1, dict2, dict3):
    dict4.update(d)
print(dict4)

# 15.  Write a Python script to check if a given key already exists in a dictionary.
dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
key = int(input("Enter the key to be checked : "))
if key in dic1.keys():
    print("Key is present in the dictionary")
else:
    print("Key is not present in the dictionary")

# 16.  Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
dict1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64,
         9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
for i in dict1:
    print(i, ":", dict1[i])

# 17. How will you create a list, tuple, set and dictionary, each containing
#  one element?
lst = [1]
tup = (1,)
s = {1}
d = {1: 1}
print(lst)
print(tup)
print(s)
print(d)

# 18. Write a Python program to rename a key in dictionary.
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print(dict1)
key = int(input("Enter the key to be renamed : "))
new_key = int(input("Enter the new key : "))
dict1[new_key] = dict1.pop(key)
print(dict1)

# 19. Write a Python program to create a set.
s = set()
print(s)

# 20. Write a Python program to iterate over sets.
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
for i in s:
    print(i)

# 21. Write a Python program to add member(s) in a set.
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s.add(11)
print(s)

# 22. Write a Python program to remove item(s) from set
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(s1)
s1.remove(10)
print(s1)

# 23. Write a Python program to remove an item from a set if it is present in the set.
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(s1)
s1.discard(10)
print(s1)

# 24. Write a Python program to create an intersection of sets.
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {1, 2, 3, 4, 5, 11, 12, 13, 14, 15}
print(s1.intersection(s2))

# 25. Write a Python program to update value in dictionary.
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print(dict1)
key = int(input("Enter the key to be updated : "))
new_value = int(input("Enter the new value : "))
dict1[key] = new_value
print(dict1)

# 26. Write a Python script to check if a given values exists in a dictionary.
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
value = int(input("Enter the value to be checked : "))
if value in dict1.values():
    print("Value is present in the dictionary")
else:
    print("Value is not present in the dictionary")

# 27. Given the following dictionary:
#  d = { 'd1': {'Fruitname' : 'Mango', 'Season' : 'Summer'},
#  'd2': {'Fruitname' : 'Orange', 'Season' : 'Winter'}}
#  How will you access and print Mango and Winter?
d = {'d1': {'Fruitname': 'Mango', 'Season': 'Summer'}, }
print(d['d1']['Fruitname'])
print(d['d1']['Season'])

# 28. Given the following dictionary
#  marks = {
#  'Subu' : {'Maths' : 88, 'Eng' : 60, 'SSt' : 95},
#  'Amol' : {'Maths' : 78, 'Eng' : 68, 'SSt' : 89},
#  'Raka' : {'Maths' : 56, 'Eng' : 66, 'SSt' : 77}
#  }
#  Write a program to perform the following operations:
#  - Print marks obtained by Amol in English.
#  - Set marks obtained by Raka in Maths to 77.
marks = {
    "Subu": {"Maths": 88, "Eng": 60, "SSt": 95},
    "Amol": {"Maths": 78, "Eng": 68, "SSt": 89},
    "Raka": {"Maths": 56, "Eng": 66, "SSt": 77}
}
print(marks["Amol"]["Eng"])
marks["Raka"]["Maths"] = 77
print(marks["Raka"]["Maths"])

# 29. How will you create an empty list, empty tuple, empty set and
#  empty dictionary?

lst = []
tup = ()
s = set()
d = {}
print(lst)
print(tup)
print(s)
print(d)
# 30. Given dictionary
# a={"salary":20, "age":90}
# Write a program to perform the following operations:
# -sort the given dictionary by key in ascending order
# -sort the given dictionary by value in descending order
a = {"salary": 20, "age": 90}
print(sorted(a.items()))
print(sorted(a.items(), reverse=True))


# 31. Write a program that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
# If it is divisible by 5, it should return “Buzz”.
# If it is divisible by both 3 and 5, it should return “FizzBuzz”.
# Otherwise, it should return the same number.

number = int(input("Enter the number : "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

# 32. Given input
# a=[1,2,3,4]
# expected output: ["ram",1,2,"hari",4]
a = [1, 2, 3, 4]
a[0] = "ram"
a[2] = "hari"
print(a)

# 33. Given input
# a=[1,2,3,4]
# expected output: [1,2,3,4,[8,9]]
a = [1, 2, 3, 4]
a.append([8, 9])
print(a)

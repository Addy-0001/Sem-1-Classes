# 1. print "softwarica" 10 times using while loop
i = 0
while i < 11:
    print("softwarica")
    i += 1

# 2. Sum of a list using while loop
list1 = [1, 2, 3, 4, 5]
sum = 0
i = 0
while i < len(list1):
    sum += list1[i]
    i += 1
print(sum)


# 3. print each character using indexing using while loop
name = "softwarica"
i = 0
while i < len(name):
    print(name[i])
    i += 1

# 4. write a program to display integer from of a list. given list=[1,"a","c",2,3,4] using while loop
list1 = [1, "a", "c", 2, 3, 4]
i = 0
while i < len(list1):
    if type(list1[i]) == int:
        print(list1[i])
    i += 1

# 5. multiplication of a each element. given list=[4,5,3,2] using while loop
list1 = [4, 5, 3, 2]
i = 0
while i < len(list1):
    print(list1[i] * 2)
    i += 1

# 6. multiplication table of a given number using while loop
num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{num} * {i} = {num * i}")
    i += 1


# 7. reverse a list using while loop
list1 = [1, 2, 3, 4, 5]
list2 = []
i = len(list1) - 1
while i >= 0:
    list2.append(list1[i])
    i -= 1
print(list2)


# 8.  given list is [1,2,3,4] but expected output in new list [2,3,4,5] using while loop
list1 = [1, 2, 3, 4]
list2 = []
i = 0
while i < len(list1):
    list2.append(list1[i] + 1)
    i += 1
print(list2)


# 9. given number is prime or not using while loop
num = int(input("Enter a number: "))
i = 2
while i < num:
    if num % i == 0:
        print("Not Prime")
        break
    i += 1
else:
    print("Prime")


# 10. Write a python program to display all the prime numbers within a given range using while loop
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
while lower <= upper:
    i = 2
    while i < lower:
        if lower % i == 0:
            break
        i += 1
    else:
        print(lower)
    lower += 1


# 11. Python program that accepts a string and calculate the number of digits and letters and space using while loop
string = input("Enter a string: ")
i = 0
digit = 0
letter = 0
space = 0
while i < len(string):
    if string[i].isdigit():
        digit += 1
    elif string[i].isspace():
        space += 1
    else:
        letter += 1
    i += 1
print(f"Digit: {digit}")
print(f"Letter: {letter}")
print(f"Space: {space}")

# 12. Python program to check the validity of username and password input by users using while loop
username = input("Enter username: ")
password = input("Enter password: ")
while True:
    if len(username) < 10:
        print("Username must be 10 characters long")
        break
    elif len(password) < 10:
        print("Password must be 10 characters long")
        break
    elif username == password:
        print("Username and password must be different")
        break
    else:
        print("Valid")
        break

# 13. program to print the given number is odd or even using while loop
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 14. factorial of a given number
num = int(input("Enter a number: "))
i = 1
fact = 1
while i <= num:
    fact *= i
    i += 1
print(fact)

# 15. program to check given number is palindrome or not
num = int(input("Enter a number: "))
temp = num
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# 16. program to check given number is armstrong or not using while loop
num = int(input("Enter a number: "))
temp = num
sum = 0
while num > 0:
    rem = num % 10
    sum += rem ** 3
    num = num // 10
if temp == sum:
    print("Armstrong")
else:
    print("Not Armstrong")


# 17. Python program to check a number is perfect square using while loop
num = int(input("Enter a number: "))
i = 1
while i <= num:
    if i * i == num:
        print("Perfect Square")
        break
    i += 1
else:
    print("Not Perfect Square")


# 18. python program to check a number is perfect number using while loop
num = int(input("Enter a number: "))
i = 1
sum = 0
while i < num:
    if num % i == 0:
        sum += i
    i += 1
if sum == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")


# 19. Print multiplication table of  1,2,3,4,5,6,7,8 using while loop
list = [1, 2, 3, 4, 5, 6, 7, 8]
i = 1
while i <= 10:
    for j in list:
        print(f"{j} * {i} = {j * i}")
    i += 1


# 20. Given list is lst=[1,2,3,4] but print 1 and 2 only using while loop
lst = [1, 2, 3, 4]
i = 0
while i < len(lst):
    if lst[i] == 3 or lst[i] == 4:
        break
    print(lst[i])
    i += 1

# 21. Python program to calculate the sum of all the odd numbers within the given range using while loop
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
sum = 0
while lower <= upper:
    if lower % 2 != 0:
        sum += lower
    lower += 1
print(sum)


# 22. Python program to calculate the sum of all the even numbers within the given range using while loop
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
sum = 0
while lower <= upper:
    if lower % 2 == 0:
        sum += lower
    lower += 1
print(sum)


# 23. Python program to count the space of a given string using while loop
string = input("Enter a string: ")
i = 0
space = 0
while i < len(string):
    if string[i].isspace():
        space += 1
    i += 1
print(space)


# 24. given list is [1,2,3,4] but expected output is [1,8,27,64] using while loop
lst = [1, 2, 3, 4]
i = 0
while i < len(lst):
    lst[i] = lst[i] ** 3
    i += 1
print(lst)


# 25. Multiplication of a list using while loop
lst = [1, 2, 3, 4]
i = 0
mul = 1
while i < len(lst):
    mul *= lst[i]
    i += 1
print(mul)


# 26. Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50) using while loop
i = 0
while i < 50:
    if i == 8:
        break
    print(i)
    i += 1

# 27. Write a for loop that iterates through a string and prints every letter using while loop
string = input("Enter a string: ")
i = 0
while i < len(string):
    print(string[i])
    i += 1


# 28. Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam using while loop
a = ["ram", "shyam", 1, 2]
i = 0
while i < len(a):
    print(f"Hello! {a[i]}")
    i += 1

# 29. Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2'] using while loop
a = ["ram", "shyam", 1, 2]
i = 0
while i < len(a):
    a[i] = "Dr." + str(a[i])
    i += 1
print(a)


# 30. Write a for loop which appends the square of each number to the new list using while loop
lst1 = [1, 2, 3, 4]
lst2 = []
i = 0
while i < len(lst1):
    lst2.append(lst1[i] ** 2)
    i += 1
print(lst2)


# 31. Write a for loop using an if statement, that appends each number to the new list if it's positive. given lst1=[111, 32, -9, -45, -17, 9, 85, -10] using while loop
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
lst2 = []
i = 0
while i < len(lst1):
    if lst1[i] > 0:
        lst2.append(lst1[i])
    i += 1
print(lst2)


# 32. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. given list=[0,1,2,3,4,5,6] using while loop
lst = [0, 1, 2, 3, 4, 5, 6]
i = 0
while i < len(lst):
    if lst[i] == 3 or lst[i] == 6:
        i += 1
        continue
    print(lst[i])
    i += 1

# 33. Write a program which appends the type of each element in the first list to the second list using while loop
list1 = [1, "a", 2, "b", 3, "c"]
list2 = []
i = 0
while i < len(list1):
    list2.append(type(list1[i]))
    i += 1
print(list2)


# 34. Use else block to display a message “Done” after successful execution of while loop
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Done")


# 35. Write a while loop statement to print the following series:
# 105 98 -------7
i = 105
while i >= 7:
    print(i)
    i -= 7

# 36. removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython
bad_chars = [';', ':', '!', "*", " "]
string = "py;th* o:n ! ;py * t*h:o !n"
i = 0
while i < len(string):
    string = string.replace(bad_chars[i], "")
    i += 1
print(string)

# 37. Python program to count the number of even and odd numbers from a series of numbers using while loop
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
even = 0
odd = 0
while i < len(lst):
    if lst[i] % 2 == 0:
        even += 1
    else:
        odd += 1
    i += 1
print(f"Even: {even} and Odd: {odd}")


# 38. Given list is lst=[1,2,3,4] but print 1 2 and 4 only using while loop
lst = [1, 2, 3, 4]
i = 0
while i < len(lst):
    if lst[i] == 3:
        i += 1
        continue
    print(lst[i])
    i += 1


# 39. Given list is lst=[1,2,3,4] but print 1 and 4 only
lst = [1, 2, 3, 4]
i = 0
while i < len(lst):
    if lst[i] == 2 or lst[i] == 3:
        i += 1
        continue
    print(lst[i])
    i += 1

# 40. Given list is [1,2,3,4] but expected output is [1,"a",2,4]
lst = [1, 2, 3, 4]
i = 0
while i < len(lst):
    if lst[i] == 3:
        lst[i] = "a"
    i += 1
print(lst)

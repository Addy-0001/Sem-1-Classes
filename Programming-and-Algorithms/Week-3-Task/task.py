# 1. print "softwarica" 10 times
for i in range(10):
    print("softwarica")
# 2. Sum of a list
lst = [1, 2, 3, 4, 5]
sum = 0
for i in lst:
    sum = sum + i
print(sum)
# 3. print each character using indexing
str = "softwarica"
for i in range(len(str)):
    print(str[i])
# 4. write a program to display integer from of a list. given list=[1,"a","c",2,3,4]\lst = [1,"a","c",2,3,4]
for i in lst:
    if type(i) == int:
        print(i)
# 5. multiplication of a each element. given list=[4,5,3,2]
lst = [4, 5, 3, 2]
mul = 1
for i in lst:
    mul = mul * i
    print(mul)
# 6. multiplication table of a given number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "*", i, "=", num*i)

# 7. reverse a list
lst = [1, 2, 3, 4, 5]
list_rev = []
for i in range(len(lst)-1, -1, -1):
    list_rev.append(lst[i])
print(list_rev)

# 8.  given list is [1,2,3,4] but expected output in new list [2,3,4,5]
lst = [1, 2, 3, 4]
lst_new = []
for i in lst:
    lst_new.append(i+1)
print(lst_new)


# 9. given number is prime or not
num = int(input("Enter a number: "))
for i in range(2, num):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime")

# 10. Write a python program to display all the prime numbers within a given range.
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

# 11. Python program that accepts a string and calculate the number of digits and letters and space
str = input("Enter a string: ")
digit = 0
letter = 0
space = 0
for i in str:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        letter += 1
    elif i.isspace():
        space += 1
print("Digit: ", digit)
print("Letter: ", letter)
print("Space: ", space)

# 12. Python program to check the validity of username and password input by users
username = input("Enter username: ")
password = input("Enter password: ")
if username == "softwarica" and password == "softwarica":
    print("Login successful")
else:
    print("Login failed")

# 13. program to print the given number is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 14. factorial of a given number
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

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
    print("Not palindrome")

# 16. program to check given number is armstrong or not
num = int(input("Enter a number: "))
temp = num
sum = 0
while num > 0:
    rem = num % 10
    sum = sum + rem ** 3
    num = num // 10
if temp == sum:
    print("Armstrong")
else:
    print("Not armstrong")

# 17. Python program to check a number is perfect square
num = int(input("Enter a number: "))
for i in range(1, num):
    if i * i == num:
        print("Perfect square")
        break
else:
    print("Not perfect square")

# 18. python program to check a number is perfect number
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print("Perfect number")
else:
    print("Not perfect number")

# 19. Print multiplication table of  1,2,3,4,5,6,7,8
for i in range(1, 9):
    for j in range(1, 11):
        print(i, "*", j, "=", i*j)
    print("")

# 20. Given list is lst=[1,2,3,4] but print 1 and 2 only
lst = [1, 2, 3, 4]
for i in lst:
    if i == 3:
        break
    print(i)

# 21. Python program to calculate the sum of all the odd numbers within the given range.
range_no = int(input("Enter a range: "))
sum = 0
for i in range(1, range_no+1):
    if i % 2 != 0:
        sum = sum + i
print(sum)

# 22. Python program to calculate the sum of all the even numbers within the given range.
range_no = int(input("Enter a range: "))
sum = 0
for i in range(1, range_no+1):
    if i % 2 == 0:
        sum = sum + i
print(sum)

# 23. Python program to count the space of a given string
str = input("Enter a string: ")
count = 0
for i in str:
    if i.isspace():
        count += 1
print(count)

# 24. given list is [1,2,3,4] but expected output is [1,8,27,64]
lst = [1, 2, 3, 4]
lst_new = []
for i in lst:
    lst_new.append(i**3)
print(lst_new)

# 25. Multiplication of a list
lst = [1, 2, 3, 4]
mul = 1
for i in lst:
    mul = mul * i
print(mul)

# 26. Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50)
for i in range(50):
    if i == 8:
        break
    print(i)

# 27. Write a for loop that iterates through a string and prints every letter.
str = input("Enter a string: ")
for i in str:
    print(i)

# 28. Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam
a = ["ram", "shyam", 1, 2]
list_new = []
for i in a:
    if type(i) == str:
        list_new.append(i)
for i in list_new:
    print("Hello!", i)


# 29. Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:
# ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
a = ["ram", "shyam", 1, 2]
lst = []
for lst_item in a:
    i_string = "Dr. " + lst_item
    lst.append(i_string)
print(lst)

# 30. Write a for loop which appends the square of each number to the new list.
a = [1, 2, 3, 4]
lst = []
for i in a:
    lst.append(i**2)
print(lst)

# 31. Write a for loop using an if statement, that appends each number to the new list if it's positive. given lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
lst2 = []
for i in lst1:
    if i > 0:
        lst2.append(i)
print(lst2)

# 32. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. given list=[0,1,2,3,4,5,6]
lst = [0, 1, 2, 3, 4, 5, 6]
for i in lst:
    if i == 3 or i == 6:
        continue
    print(i)

# 33. Write a for loop which appends the type of each element in the first list to the second list.
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = []
for i in lst1:
    lst2.append(type(i))
print(lst1)
print(lst2)

# 34. Use else block to display a message “Done” after successful execution of for loop.
for i in range(5):
    print(i)
else:
    print("Done")

# 35. Write a while loop statement to print the following series:
# 105 98 -------7

i = 105
while i >= 7:
    print(i)
    i = i - 7

# 36. removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython
bad_chars = [';', ':', '!', "*", " "]
string = "py;th* o:n ! ;py * t*h:o !n"
for i in bad_chars:
    string = string.replace(i, "")
print(string)

# 37. Python program to count the number of even and odd numbers from a series of numbers.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count = 0
odd_count = 0
for i in lst:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even count: ", even_count)
print("Odd count: ", odd_count)

# 38. Given list is lst=[1,2,3,4] but print 1 2 and 4 only
lst = [1, 2, 3, 4]
for i in lst:
    if i == 3:
        continue
    print(i)

# 39. Given list is lst=[1,2,3,4] but print 1 and 4 only
lst = [1, 2, 3, 4]
for i in lst:
    if i == 2 or i == 3:
        continue
    print(i)

# 40. Given list is [1,2,3,4] but expected output is [1,"a",2,4]
lst = [1, 2, 3, 4]
lst_new = []
for i in lst:
    if i == 3:
        lst_new.append("a")
        continue
    lst_new.append(i)
print(lst_new)

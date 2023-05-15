from math import * 
# 1. Write a program to accept two integers and check whether they are equal or not.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")


# 2. Write a program to check whether a given number is even or odd.
a = int(input("Enter a number: "))
b = a % 2
if b == 0:
    print("The number is even")
else:
    print("The number is odd")

# 3. Write a program to accept a number and check whether it is positive or negative.
a = int(input("Enter a number: "))
if a > 0:
    print("The number is positive")
elif a < 0:
    print("The number is negative")
else:
    print("The number is zero")

# 4. Write a program to check whether an alphabet is a vowel or a consonant.
a = input("Enter an alphabet: ")
if a == "a" or a == "e" or a == "i" or a == "o" or a == "u" or a == "A" or a == "E" or a == "I" or a == "O" or a == "U":
    print("The alphabet is a vowel")
else:
    print("The alphabet is a consonant")

# 5. Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print(1)
elif a > b:
    print(2)
else:
    print(3)

# 6. Print "Hello" if a is equal to b, and c is equal to d.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a == b and c == d:
    print("Hello")

# 7. Print "Hello" if a is equal to b, or if c is equal to d.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a == b or c == d:
    print("Hello")

# 8.  Accept input from user if given number is a multiple of both 3 and 5 prints "FizzBuzz" instead of number
#     if given number is a multiple of 3 but not 5 prints "Fizz" instead of number
#     if given number is a multiple of 5 but not 3 prints "Buzz" instead of number
#     if given number is not multiple of 3 or 5 prints value as usual.

a = int(input("Enter a number: "))
b = a % 3
c = a % 5

if b == 0 and c == 0:
    print("FizzBuzz")
elif b == 0:
    print("Fizz")
elif c == 0:
    print("Buzz")
else:
    print(a)

# 9. Check whether the user input number is even or odd and display it to user.
a = int(input("Enter a number: "))
b = a % 2

if b == 0:
    print("The number is even")
else:
    print("The number is odd")

# 10. WAP which accepts marks of four subjects and display total marks, percentage and grade.
#     (Hint: more than 70 –> distinction, more than 60–> first, more than 40 –> pass, less than 40 –> fail)

a = int(input("Enter marks of first subject: "))
b = int(input("Enter marks of second subject: "))
c = int(input("Enter marks of third subject: "))
d = int(input("Enter marks of fourth subject: "))

total = a + b + c + d
percentage = total / 4

if percentage >= 70:
    print("Distinction")
elif percentage >= 60 and percentage < 70:
    print("First")
elif percentage >= 40 and percentage < 60:
    print("Pass")
else:
    print("Fail")

# 11. What is the output of APPLE > apple?
print("APPLE" > "apple")

# 12. Write a Python program to display your details like name, age, address in three different lines.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")
print(f"Name: {name}, \n Age: {age}, \n Address: {address}")

# 13. Write a python program which accepts the radius of circle from user and compute the area.
radius = int(input("Enter the radius of circle: "))
area = pi * (radius ** 2)
print(f"The area of circle is {area}")

# 14. Given three integers, print the smallest one. (Three integers should be user input)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a != b and a != c and b != c:
    if a < b and a < c:
        print(a, "is smallest")
    elif b < a and b < c:
        print(b, "is smallest")
    else:
        print(c, "is smallest")
else:
    print("All numbers are equal")

# 15. Given three integers, print the largest one. (Three integers should be user input)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a != b and a != c and b != c:
    if a > b and a > c:
        print(a, "is largest")
    elif b > a and b > c:
        print(b, "is largest")
    else:
        print(c, "is largest")
else:
    print("All numbers are equal")

# 16. Write a program that takes three numbers and prints their sum. Every number is given on a separate line.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(a + b + c)

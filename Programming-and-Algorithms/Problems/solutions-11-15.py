# 11. What is the output of APPLE > apple?
print("APPLE" > "apple")

# 12. Write a Python program to display your details like name, age, address in three different lines.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")
print(f"Name: {name}, \n Age: {age}, \n Address: {address}")

# 13. Write a python program which accepts the radius of circle from user and compute the area.
radius = int(input("Enter the radius of circle: "))
area = 3.14 ** radius
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

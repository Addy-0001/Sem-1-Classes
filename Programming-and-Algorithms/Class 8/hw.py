#Write a program that takes 3 inputs from a user and prints which is the largest input

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a == b and a == c:
    print("All numbers are equal")
else:
    if a > b and a > c:
        print(f"{a} is the largest number")
    elif b > a and b > c:
        print(f"{b} is the largest number")
    else:
        print(f"{c} is the largest number")

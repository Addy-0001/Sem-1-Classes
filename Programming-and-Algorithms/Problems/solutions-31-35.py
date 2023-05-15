# 31. Accept three numbers from the user and display the second largest number.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a != b and a != c and b != c:
    if a > b and a > c:
        if b > c:
            print(f"{b} is second largest")
        else:
            print(f"{c} is second largest")
    elif b > a and b > c:
        if a > c:
            print(f"{a} is second largest")
        else:
            print(f"{c} is second largest")
    else:
        if a > b:
            print(f"{a} is second largest")
        else:
            print(f"{b} is second largest")
else:
    print("All numbers are equal")

# 32. Accept the number of days from the user and calculate the charge for library according to following:
#     Till five days: Rs 2/day
#     Six to ten days: Rs 3/day
#     11 to 15 days: Rs 4/day
#     After 15 days: Rs 5/day

days = int(input("Enter number of days: "))
if days <= 5:
    print(f"Charge for library: {days * 2}")
elif days > 5 and days <= 10:
    print(f"Charge for library: {days * 3}")
elif days > 10 and days <= 15:
    print(f"Charge for library: {days * 4}")
else:
    print(f"Charge for library: {days * 5}")

# 33. A company decided to give bonus of 5 % to employee if his/her year of service is more than 5years. 
# Ask user for their salary and year of service and print the net bonus amount.

salary = int(input("Enter salary: "))
year_of_service = int(input("Enter year of service: "))
if year_of_service > 5:
    print(f"Net bonus amount: {salary * 0.05}")
else:
    print("No bonus")

# 34. Write a program to check two strings are anagram or not .
a = input("Enter first string: ")
b = input("Enter second string: ")

if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not anagram")

# 35. A school has following rules for grading system:
#     Below 25 - F
#     25 to 45 - E
#     45 to 50 - D
#     50 to 60 - C
#     60 to 80 - B
#     Above 80 - A
#     Ask user to enter marks and print the corresponding grade.
marks = int(input("Enter marks: "))
if marks < 25:
    print("F")
elif marks >= 25 and marks < 45:
    print("E")
elif marks >= 45 and marks < 50:
    print("D")
elif marks >= 50 and marks < 60:
    print("C")
elif marks >= 60 and marks < 80:
    print("B")
else:
    print("A")


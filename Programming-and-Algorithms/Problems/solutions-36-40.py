# 36. Write a program to display last digit of a number
a = int(input("Enter a number: "))
print(f"Last digit of {a} is {a % 10}")

# 37. Write a program to display middle digit or second last digit number
#  Repeat...............................................................

# 38. A school decided to replace the desks in three classrooms. 
# Each desk sits two students. 
# Given the number of students in each class, print the smallest possible number of desks that can be 
# purchased. 
# The program should read three integers: the number of students in each of the three
# classes, a, b and c respectively.
# Hint. In the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.
a = int(input("Enter number of students in first class: "))
b = int(input("Enter number of students in second class: "))
c = int("Enter number of students in third class: ")
print(f"Total number of desks: {a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2}")

# 39. Write a python program which calculates tax of an employee with given condition:
#     Salary            	       Tax Rate
#     Below 20000                  15%
#     20000 to 50000               25%
#     50000 to 100000              30%
#     Above 100000                 35%
salary = int(input("Enter salary: "))
if salary < 20000:
    print(f"Tax: {salary * 0.15}")
elif salary >= 20000 and salary < 50000:
    print(f"Tax: {salary * 0.25}")
elif salary >= 50000 and salary < 100000:
    print(f"Tax: {salary * 0.30}")
else:
    print(f"Tax: {salary * 0.35}")

# 40. For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0.
x = int(input("Enter a number: "))
if x > 0:
    print("True")
elif x < 0:
    print("False")
else:
    print("Zero")

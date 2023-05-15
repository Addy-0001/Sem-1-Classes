# 26. Write a program to accept the cost price of a bike qnd display the road tax to be paid according to the following criteria:
#     Cost price(in Rs)                         Tax
#     >100000		                              15%
#     >50000 and <=100000                       10%
#     <=50000                                   5%

cost = int(input("Enter cost price of bike: "))
if cost > 100000:
    print(f"Road tax to be paid: {cost * 0.15}")
elif cost > 50000 and cost <= 100000:
    print(f"Road tax to be paid: {cost * 0.1}")
else:
    print(f"Road tax to be paid: {cost * 0.05}")

# 27. Accept 3 number and display the smallest number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a != b and a != c and b != c:
    if a < b and a < c:
        print(f"{a} is smallest")
    elif b < a and b < c:
        print(f"{b} is smallest")
    else:
        print(f"{c} is smallest")
else:
    print("All numbers are equal")

# 28. Accept 3 number and display the largest number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a != b and a != c and b != c:
    if a > b and a > c:
        print(f"{a} is smallest")
    elif b > a and b >  c:
        print(f"{b} is smallest")
    else:
        print(f"{c} is smallest")
else:
    print("All numbers are equal")

# 29. Accept 3 number and display the second largest number
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

# 30. A company decided to give bonus to employee according to following criteria:
#     Time period of service              Bonus
#     More than 10 years	                10%
#     >=6 and <=10                        8%
#     Less than 6 years                   5%

time = int(input("Enter time period of service: "))
if time > 10:
    print(f"Bonus: {time * 0.1}")
elif time >= 6 and time <= 10:
    print(f"Bonus: {time * 0.08}")
else:
    print(f"Bonus: {time * 0.05}")


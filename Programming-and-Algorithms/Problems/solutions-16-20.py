# 16. Write a program that takes three numbers and prints their sum. Every number is given on a separate line.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(a + b + c)

# 17. N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket.
#     How many apples will each single student get? How many apples will remain in the basket? The program reads the numbers N and K. 
#     It should print the two answers for the questions above.
n = int(input("Enter number of students: "))
k = int(input("Enter number of apples: "))

print(f"Each student will get {k // n} apples")
print(f"Remaining apples in basket: {k % n}")

# 18. Check whether 5 is in list of first 5 natural numbers or not . Hint: List = > [1, 2, 3, 4, 5]
list = [1, 2, 3, 4, 5]
if 5 in list:
    print("5 is in list")
else:
    print("5 is not in list")

# 19. Write a program to check whether a number entered is three-digit number or not .
number = int(input("Enter a number: "))

if number >= 100 and number <= 999:
    print("Number is three-digit number")
else:
    print("Number is not three-digit number")

# 20. Write a program to display middle digit or second last digit number
a = int(input("Enter a three digit number: "))
digit_last = a % 10
digit_middle = (a // 10) % 100

print(f"Middle digit: {digit_middle}")
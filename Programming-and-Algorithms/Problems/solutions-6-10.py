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
# 21. A school has following rules for grading system:
#     a. Below 25 - F
#     b. 25 to 45 - E
#     c. 45 to 50 - D
#     d. 50 to 60 - C
#     e. 60 to 80 - B
#     f. Above 80 - A
#     Ask user to enter marks and print the corresponding grade.

a = int(input("Enter marks: "))
if a < 25:
    print("F")
elif a >= 25 and a < 45:
    print("E")
elif a >= 45 and a < 50:
    print("D")
elif a >= 50 and a < 60:
    print("C")
elif a >= 60 and a < 80:
    print("B")
else:
    print("A")

# 22. Accept any city from the user and display monument of that city.
# City                                 Monument
# Delhi                               Red Fort
# Agra                                Taj Mahal
# Jaipur                              Jal Mahal

city = input("Enter city: ")
if city.capitalize() == "Delhi":
    print("Red Fort")
elif city.capitalize() == "Agra" :
    print("Taj Mahal")
elif city.capitalize() == "Jaipur":
    print("Jal Mahal")

# 23.  Write a program to whether a number(accepted from user) is divisible by 2 and 3 both.
a = int(input("Enter a number: "))
if a % 2 == 0 and a % 3 == 0:
    print("Number is divisible by 2 and 3 both")
else:
    print("Number is not divisible by 2 and 3 both")

# 24. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
#     Like:
#     Enter First Number: 7
#     Enter Second Number: 9
#     Enter operator: +
#     Your Answer is: 16

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator: [choose from : +, -, *, /, %]")

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
elif operator == "%":
    print(a % b)
else:
    print("Invalid operator choose from +, -, *, /, %")

# 25. Write a program to accept marks from the user and display the grade according to the following criteria:
#     Marks                                    Grade
#     > 90                                        A
#     > 80 and <= 90                              B
#     >= 60 and <= 80                             C
#     below 60                                    D

marks = int(input("Enter marks: "))
if marks > 90:
    print("A")
elif marks > 80 and marks <= 90:
    print("B")
elif marks >= 60 and marks <= 80:
    print("C")
else:
    print("D")

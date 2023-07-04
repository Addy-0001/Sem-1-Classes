# Program to display integer from the list given. List = [1, 'a', 'b', 2, 3, 4]
def display():
    list = [1, 'a', 'b', 2, 3, 4]
    for i in list:
        if type(i) == int:
            print(i)

# Check if the given number is prime or not


def prime():
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


# Python program that accepts a string and calculate the number of digits and letters
def count():
    string = input("Enter a string: ")
    digit = 0
    letter = 0
    for i in string:
        if i.isdigit():
            digit += 1
        elif i.isalpha():
            letter += 1
    print("Letters: ", letter)
    print("Digits: ", digit)

# Program to find the factorial of a number


def factorial():
    num = int(input("Enter a number: "))
    factorial = 1
    if num < 0:
        print("Factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)


# Program to check if the given number is armstrong or not
def armstrong():
    num = int(input("Enter a number: "))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")

# Program to check if a number is a perfect number


def perfect():
    num = int(input("Enter a number: "))
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        print(num, "is a Perfect number")
    else:
        print(num, "is not a Perfect number")

# Program to count the space of a given string


def space():
    string = input("Enter a string: ")
    count = 0
    for i in string:
        if i == " ":
            count += 1
    print("Number of spaces in the string: ", count)

# Write a for loop using an if statement that appends each number to the new list if it is positive. Given list List = [111, 32, -9, -45, -17, 9, 85, -10]


def positive():
    list = [111, 32, -9, -45, -17, 9, 85, -10]
    new_list = []
    for i in list:
        if i > 0:
            new_list.append(i)
    print(new_list)

# Reverse a string using while loop


def reverse():
    string = input("Enter a string: ")
    reverse = ""
    i = len(string) - 1
    while i >= 0:
        reverse += string[i]
        i -= 1
    print(reverse)

# Reverse a string using for loop


def reverse_for():
    string = input("Enter a string: ")
    reverse = ""
    for i in string:
        reverse = i + reverse
    print(reverse)

# Program to find the sum of all digits of a number


def sum():
    num = int(input("Enter a number: "))
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num //= 10
    print("Sum of the digits of the number: ", sum)

# Write an example of break and continue keyword using both for loop and while loop


def break_continue():
    # break
    for i in range(1, 11):
        if i == 5:
            break
        print(i)
    # continue
    for i in range(1, 11):
        if i == 5:
            continue
        print(i)
    # break
    i = 1
    while i < 11:
        if i == 5:
            break
        print(i)
        i += 1
    # continue
    i = 1
    while i < 11:
        if i == 5:
            i += 1
            continue
        print(i)
        i += 1

# Python program to find the factorial of a given number using recursion


def factorial_recursion(num):
    if num == 1:
        return num
    else:
        return num * factorial_recursion(num - 1)


# Using a for loop and appemd each time with a dr. prefix to the list, a = ["Ram", "Shyam"] then the output should be ["Dr. Ram", "Dr. Shyam"]
def prefix():
    a = ["Ram", "Shyam"]
    new_list = []
    for i in a:
        new_list.append("Dr. " + i)
    print(new_list)

# Fiven list is [1, 2, 3, 4] but the expected output is [1, a, 2, 4]


def replace():
    list = [1, 2, 3, 4]
    list[2] = "a"
    list[3] = 4
    print(list)


def main():
    print(
        "Input 1 for Program to display integer from the list given. List = [1, 'a', 'b', 2, 3, 4]")
    print("Input 2 for Check if the given number is prime or not")
    print("Input 3 for Python program that accepts a string and calculate the number of digits and letters")
    print("Input 4 for Program to find the factorial of a number")
    print("Input 5 for Program to check if the given number is armstrong or not")
    print("Input 6 for Program to check if a number is a perfect number")
    print("Input 7 for Program to count the space of a given string")
    print(
        "Input 8 for Write a for loop using an if statement that appends each number to the new list if it is positive. Given list List = [111, 32, -9, -45, -17, 9, 85, -10]")
    print("Input 9 for Reverse a string using while loop")
    print("Input 10 for Reverse a string using for loop")
    print("Input 11 for Program to find the sum of all digits of a number")
    print("Input 12 for Write an example of break and continue keyword using both for loop and while loop")
    print("Input 13 for Python program to find the factorial of a given number using recursion")
    print(
        "Input 14 for Using a for loop and appemd each time with a dr. prefix to the list, a = ['Ram', 'Shyam'] then the output should be ['Dr. Ram', 'Dr. Shyam']")
    print(
        "Input 15 for Fiven list is [1, 2, 3, 4] but the expected output is [1, a, 2, 4]")
    print("Input 0 to exit")

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            display()
        elif choice == 2:
            prime()
        elif choice == 3:
            count()
        elif choice == 4:
            factorial()
        elif choice == 5:
            armstrong()
        elif choice == 6:
            perfect()
        elif choice == 7:
            space()
        elif choice == 8:
            positive()
        elif choice == 9:
            reverse()
        elif choice == 10:
            reverse_for()
        elif choice == 11:
            sum()
        elif choice == 12:
            break_continue()
        elif choice == 13:
            num = int(input("Enter a number: "))
            print("Factorial of", num, "is", factorial_recursion(num))
        elif choice == 14:
            prefix()
        elif choice == 15:
            replace()
        elif choice == 0:
            break
        else:
            print("Invalid choice")

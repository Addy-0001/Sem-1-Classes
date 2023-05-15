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

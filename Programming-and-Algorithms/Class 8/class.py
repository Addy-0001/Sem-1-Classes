# from pdb import *

# # Type Checking -
# # Python is a dynamically typed language.
# # Implicit type conversion occurs.

# a = "Python"
# print(a[:])
# print(a[-len(a)])

# # Compile Time Error
# #       - Syntax errors
# # Error Handling
# #       - Try and Except
# print(a[5])

# The bike Problem
bike1 = "Yamaha"
bike1_price = 25000

bike2 = "Honda"
bike2_price = 50000

name = input("Enter your name: ")
choose = int(input("Enter your choice - 1 for Yamaha and 2 for Honda"))
print("Hello", name)
set_trace()
if choose == 1:
    print(f"{bike1} will cost you {bike1_price}")
elif choose == 2:
    print(f"{bike2 + 2000} will cost you {bike2_price}") #Error will be detected here
else:
    print("Invalid choice")

#Ram's girlfriend Dilemma
pocket_money = int(input("Enter your pocket money"))

if pocket_money > 5000:
    print("Ram goes on a date with Rita")
elif pocket_money > 200:
    print("Ram goes on a date with Sita")
else:
    print("Ram goes with friends")

# Take user input called pocket money, if > 400, mutton momo, else if 400 to 200, chicken momo, else ver momo
pocket_money = int(input("Enter your pocket money: "))
if pocket_money > 400:
    print("Mutton Momo")
elif pocket_money > 200 and pocket_money <= 400:
    print("Chicken Momo")
else:
    print("Veg Momo")

# take specific char from user. Check if vowel
# if vowel, print "Vowel"
# else print "Consonant"
# if input is not a char, print "Invalid Input"
character_ip = input("Enter a character: ")

if character_ip.isalpha() == False or len(character_ip) < 1 or len(character_ip) > 1:
    print("Invalid Input")
else:
    if character_ip == "a" or character_ip == "e" or character_ip == "i" or character_ip == "o" or character_ip == "u" or character_ip == "A" or character_ip == "E" or character_ip == "I" or character_ip == "O" or character_ip == "U":
        print("Vowel")
    else:
        print("Consonant")

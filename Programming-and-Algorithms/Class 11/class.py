# 1. Print the first 10 natural numbers using for loop
for i in range(1, 11):
    print(i)

# 2. Python program to print all the even numbers within the fiven range
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    if i % 2 == 0:
        print(i)

# 3. python program to calculate the sum of all numbers from 1 to a given number
number = int(input("Enter a number: "))
sum = 0
for i in range(1, number + 1):
    sum += i
print(sum)

# 4. Python program to calculate the sum of all odd numbers from all odd numbers within a given range
number1 = int(input("Enter the lower range value: "))
number2 = int(input("Enter the upper range value: "))
sum = 0

for i in range(number1, number2 + 1):
    if i % 2 != 0:
        sum += i
print(sum)

# 5. Python program to print multiplication table of a given number
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")

# 6. Ptrhon program to display numbers from a list using for loop
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)

# 7. Python program to count the total number of digits in a number
number = int(input("Enter a number: "))
str_number = str(number)
length = len(str_number)

sum = 0
for i in range(0, length):
    sum += int(str_number[i])
print(sum)

# 8. Python program to check if a string is palindrome or not
word = input("Enter a word: ")
length = len(word)
rev_word = ""
for i in range(length, 0, -1):
    rev_word += word[i-1]
if word == rev_word:
    print("Palindrome")
else:
    print("Not palindrome")

# 9. Python program to accept a word from the user and reverse it
word = input("Enter a word: ")
length = len(word)
rev_word = ""
for i in range(length, 0, -1):
    rev_word += word[i-1]
print(rev_word)

# 10. Python program to count the number of even and odd numbers from a series of numbers
number = int(input("Enter a number: "))
even = 0
odd = 0
for i in range(1, number + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Even: {even} Odd: {odd}")

# 11. Python program to find the factorial of a number
number = int(input("Enter a number: "))
sum = 1
for i in range(1, number + 1):
    sum *= i
print(sum)

# 12. Python program to accept a string and calculate the number of digits and letters
word = input("Enter a word: ")
length = len(word)
digit = 0
letter = 0
for i in range(0, length):
    if word[i].isdigit():
        digit += 1
    else:
        letter += 1
print(f"Digit: {digit} Letter: {letter}")

# 13. Python program to iterate the integers from 1 to 25
for i in range(1, 26):
    print(i)

# 14. Python program to check the validity of username and password input by users
username = "admin"
password = "admin123"

for i in range(3):
    user = input("Enter username: ")
    passw = input("Enter password: ")
    if user == username and passw == password:
        print("Login successful")
        break
    else:
        print("Wrong username or password")
        print(f"{2-i} attempts left")
else:
    print("Account blocked")
print("End of Program")

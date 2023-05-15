for i in range(10):
    print(f"{i}   Python")

for i in range(10):
    print(f"{i} = Python")


a = "Python"
b = 0
for char in a:
    print(f"{b} = {char}")
    b += 1

a = "Python"
for i in range(len(a)):
    print(f"{i} = {a[i]}")

a = [1, 2, 3, 4, 5]
for data in a:
    print(10+data, data)

a = 2
for i in range(1, 11):
    print(f"{a} * {i} = {a*i}")

a = 2
for i in range(10, 0, -1):
    print(f"{a} * {i} = {a*i}")

a = [1, 2, 3, 4]
sum = 0
for item in a:
    sum += item
print(sum)

a = [1, 2, 3, 4]
sum = 1
for item in a:
    sum *= item
print(sum)

user = int(input("Enter a number: "))
for i in range(1, user + 1):
    if i % 2 != 0:
        print(f"{i} - odd")
    else:
        print(f"{i} - even")

word = input("Enter a word: ")
length = len(word)
rev_word = ""
for i in range(length, 0, -1):
    rev_word += word[i-1]
print(rev_word)


a = int(input("Enter a number: "))
sum = 1
for item in range(1, a+1):
    sum *= item
print(sum)

# HW - define username and password. Take input from user and check if password is correct or not. if more than 3 times wrong password, print "Account blocked"
#     print how many attempts are left.
#     if 3 attempts end, print "Account blocked"
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


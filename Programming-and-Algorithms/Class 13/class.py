i = 0
name = "John"
while i in range(len(name)):
    print(f"{i} = {name[i]}")
    i += 1

# Multiplication table using while loop
i = 1
while i <= 10:
    print(f"2 * {i} = {2*i}")
    i += 1

a = [1, 2, 3, 4, 5]
sum = 0
i = 0
while i < len(a):
    sum += a[i]
    i += 1
print(sum)

a = "Python"
i = len(a) - 1
while i >= 0:
    print(a[i], end="")
    i -= 1
print()

#checking if input number is palindrome using while loop
num = int(input("Enter a number: "))
temp = num
rev = 0
while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#check if the above number is prime or nor 
num = int(input("Enter a number: "))
i = 2
while i < num:
    if num % i == 0:
        print("Not Prime")
        break
    i += 1
else:
    print("Prime")

#print the factorial of a number 
num = 5
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print(fact)

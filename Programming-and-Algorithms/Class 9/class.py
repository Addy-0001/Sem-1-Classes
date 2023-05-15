# 1. What is the output of ‘banana’ > ‘BANANA’?

# 1. Write a program to check whether a person is eligible for voting or not . (accept age from user)

# 2. Write a program to check whether a number is divisible by 7 or not .

# 3. Write a program to display "python" if a number entered by user is a multiple of five, otherwise print "sorry".

# 4. Write a program to check whether the last digit of a number(entered by user) is divisible by 3 or not .

# 5. Write a program to find the lowest number out of two numbers expected from user.

# # 6. Consider the following code:
    # if i < j: 
    #     if j < k: 
    #         i = j
    #     else:
    #         j = k
    # else:
    #     if j >  k:
    #        j = i
    #     else:
    #         i = k
    # print(i, j, k)
    # What will be the above code print if the variables i,j and k have the following values?

    # a. i=3, j=5, k=7

    # b. i=-2, j=-5, k=9

    # c. i=8, j=15, k=12

    # d. 13, j=15, k=13

    # e. i=3, j=5, k=17

    # f. i=25, j=15, k=17

# 1. What is the output of ‘banana’ > ‘BANANA’?
print('banana' > 'BANANA')

# 2. Write a program to check whether a person is eligible for voting or not . (accept age from user)
age = int(input('Enter your age: '))
if age >= 18:
    print('You are eligible for voting.')
else:
    print('You are not eligible for voting.')

# 3. Write a program to check whether a number is divisible by 7 or not .
num = int(input('Enter a number: '))
if num != 0:
    if num % 7 == 0:
        print('The number is divisible by 7.')
    else:
        print('The number is not divisible by 7.')
else:
    print('The number is zero.')

# 4. Write a program to check whether the last digit of a number(entered by user) is divisible by 3 or not .
num = int(input('Enter a number: '))
b = str(num)
last_digit = b[-1]
print('The last digit of the number is', last_digit)
num = int(last_digit)
if num != 0:
    if num % 3 == 0:
        print('The last digit of the number is divisible by 3.')
    else:
        print('The last digit of the number is not divisible by 3.')
else:
    print('The number is zero.')

# 5. Write a program to find the lowest number out of two numbers expected from user.
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
if num1 == num2:
    print('Both numbers are equal.')
else:
    if num1 < num2:
        print('The lowest number is', num1)
    else:
        print('The lowest number is', num2)

# 6. Consider the following code:
def comparision(i, j, k):
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j >  k:
           j = i
        else:
            i = k
    print(i, j, k)
    # a. i=3, j=5, k=7

    # b. i=-2, j=-5, k=9

    # c. i=8, j=15, k=12

    # d. 13, j=15, k=13

    # e. i=3, j=5, k=17

    # f. i=25, j=15, k=17

comparision(3, 5, 7) # 5, 5, 7
comparision(-2, -5, 9) # 9, -5, 9
comparision(8, 15, 12) # 8, 12, 12
comparision(13, 15, 13) # 13, 13, 13
comparision(3, 5, 17) # 5, 5, 17
comparision(25, 15, 17) # 17, 15, 17

# Middle Digit
a = int(input("Enter a Number: "))
b = str(a)
c = len(b)//2 
if len(b)%2==0:
    length = b[c-1:c+1]
else:
    length = b[c]
print(length) 

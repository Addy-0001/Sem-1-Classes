def softwarica():
    for i in range(10):
        print("softwarica")


def listSum():
    lst = [1, 2, 3, 4, 5]
    sum = 0
    for i in lst:
        sum = sum + i
    print(sum)


def printChar():
    str = "softwarica"
    for i in range(len(str)):
        print(str[i])


def intDisplay():
    lst = [1, "a", "c", 2, 3, 4]
    for i in lst:
        if type(i) == int:
            print(i)


def mul():
    lst = [4, 5, 3, 2]
    mul = 1
    for i in lst:
        mul = mul * i
        print(mul)


def mulTable():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(num, "*", i, "=", num*i)


def listRev():
    lst = [1, 2, 3, 4, 5]
    list_rev = []
    for i in range(len(lst)-1, -1, -1):
        list_rev.append(lst[i])
    print(list_rev)


def listNew():
    lst = [1, 2, 3, 4]
    lst_new = []
    for i in lst:
        lst_new.append(i+1)
    print(lst_new)


def prime():
    num = int(input("Enter a number: "))
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")


def primeRange():
    lower = int(input("Enter lower range: "))
    upper = int(input("Enter upper range: "))
    for num in range(lower, upper+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)


def stringcalc():
    '''prints the number of digits, characters and 
    spaces in the input string'''
    string = input("Enter a string: ")
    digit = 0
    char = 0
    space = 0
    for i in string:
        if i.isdigit():
            digit = digit + 1
        elif i.isalpha():
            char = char + 1
        elif i.isspace():
            space = space + 1
    print("Digits: ", digit)
    print("Characters: ", char)
    print("Spaces: ", space)


def validitycheck():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "softwarica" and password == "softwarica":
        print("Login successful")
    else:
        print("Login failed")


def oddevencheck():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


def factorialfinder():
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    print("Factorial: ", fact)


def palindromecheck():
    string = input("Enter a string: ")
    if string == string[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")


def armstrongcheck():
    num = int(input("Enter a number: "))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3
        temp = temp // 10
    if num == sum:
        print("Armstrong number")
    else:
        print("Not armstrong number")


def perfectSquareCheck():
    num = int(input("Enter a number: "))
    for i in range(1, num+1):
        if i * i == num:
            print("Perfect square")
            break
    else:
        print("Not perfect square")


def perfectNumberCheck():
    num = int(input("Enter a number: "))
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    if num == sum:
        print("Perfect number")
    else:
        print("Not perfect number")


def multiplicationTablerange():
    for i in range(1, 9):
        for j in range(1, 11):
            print(i, "*", j, "=", i*j)
    print("")


def printSpecific():
    lst = [1, 2, 3, 4]
    for i in lst:
        if i == 3:
            break
        print(i)


def sumodd():
    range_no = int(input("Enter a range: "))
    sum = 0
    for i in range(1, range_no+1):
        if i % 2 != 0:
            sum = sum + i
    print(sum)


def sumeven():
    range_no = int(input("Enter a range: "))
    sum = 0
    for i in range(1, range_no+1):
        if i % 2 == 0:
            sum = sum + i
    print(sum)


def countspace():
    string = input("Enter a string: ")
    count = 0
    for i in string:
        if i.isspace():
            count = count + 1
    print("Space: ", count)


def changelist():
    lst = [1, 2, 3, 4]
    lst_new = []
    for i in lst:
        lst_new.append(i**3)
    print(lst_new)


def listmul():
    lst = [1, 2, 3, 4]
    mul = 1
    for i in lst:
        mul = mul * i
    print(mul)


def breakloop():
    for i in range(50):
        if i == 8:
            break
        print(i)


def stringiteration():
    str = input("Enter a string: ")
    for i in str:
        print(i)


def listiteration():
    a = ["ram", "shyam", 1, 2]
    list_new = []
    for i in a:
        if type(i) == str:
            list_new.append(i)
    for i in list_new:
        print("Hello!", i)


def listiteration2():
    a = ["ram", "shyam", 1, 2]
    lst = []
    for lst_item in a:
        i_string = "Dr. " + lst_item
        lst.append(i_string)
    print(lst)


def listappend():
    a = [1, 2, 3, 4]
    lst = []
    for i in a:
        lst.append(i**2)
    print(lst)


def listappend2():
    lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
    lst2 = []
    for i in lst1:
        if i > 0:
            lst2.append(i)
    print(lst2)


def loopContinue():
    lst = [0, 1, 2, 3, 4, 5, 6]
    for i in lst:
        if i == 3 or i == 6:
            continue
        print(i)


def appendType():
    lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lst2 = []
    for i in lst1:
        lst2.append(type(i))
    print(lst1)
    print(lst2)


def loopElse():
    for i in range(5):
        print(i)
    else:
        print("Done")


def printSeries():
    i = 105
    while i >= 7:
        print(i)
        i = i - 7

def badcharremove():
    bad_chars = [';', ':', '!', "*", " "]
    string = "py;th* o:n ! ;py * t*h:o !n"
    for i in bad_chars:
        string = string.replace(i, "")
    print(string)

def countevenodd(): 
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_count = 0
    odd_count = 0
    for i in lst:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("Even count: ", even_count)
    print("Odd count: ", odd_count)

def printListData(): 
    lst = [1, 2, 3, 4]
    for i in lst:
        if i == 3:
            continue
        print(i)

def printListData2():
    lst = [1, 2, 3, 4]
    for i in lst:
        if i == 3 or i == 2:
            continue
        print(i)

def printListData3():
    lst = [1, 2, 3, 4]
    lst_new = []
    for i in lst:
        if i == 3:
            lst_new.append("a")
            continue
        lst_new.append(i)
    print(lst_new)

softwarica()
listSum()
printChar()
intDisplay()
mul()
mulTable()
listRev()
listNew()
prime()
primeRange()
stringcalc()
validitycheck()
oddevencheck()
factorialfinder()
palindromecheck()
armstrongcheck()
perfectSquareCheck()
perfectNumberCheck()
multiplicationTablerange()
printSpecific()
sumodd()
sumeven()
countspace()
changelist()
listmul()
breakloop()
stringiteration()
listiteration()
listiteration2()
listappend()
listappend2()
loopContinue()
appendType()
loopElse()
printSeries()
badcharremove()
countevenodd()
printListData()
printListData2()
printListData3()
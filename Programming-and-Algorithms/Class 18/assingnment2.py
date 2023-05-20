# Write the same code but use while loop instead of for loop

def softwarica():
    i = 0
    while i < 10:
        print("softwarica")
        i += 1


def listSum():
    lst = [1, 2, 3, 4, 5]
    sum = 0
    i = 0
    while i < len(lst):
        sum = sum + lst[i]
        i += 1
    print(sum)


def printChar():
    str = "softwarica"
    i = 0
    while i < len(str):
        print(str[i])
        i += 1


def intDisplay():
    lst = [1, "a", "c", 2, 3, 4]
    i = 0
    while i < len(lst):
        if type(lst[i]) == int:
            print(lst[i])
        i += 1


def mul():
    lst = [4, 5, 3, 2]
    mul = 1
    i = 0
    while i < len(lst):
        mul = mul * lst[i]
        print(mul)
        i += 1


def mulTable():
    num = int(input("Enter a number: "))
    i = 1
    while i <= 10:
        print(num, "x", i, "=", num * i)
        i += 1


def listRev():
    lst = [1, 2, 3, 4, 5]
    list_rev = []
    i = len(lst) - 1
    while i >= 0:
        list_rev.append(lst[i])
        i -= 1
    print(list_rev)


def listNew():
    lst = [1, 2, 3, 4]
    lst_new = []
    i = 0
    while i < len(lst):
        lst_new.append(lst[i]+1)
        i += 1
    print(lst_new)


def prime():
    num = int(input("Enter a number: "))
    i = 2
    while i < num:
        if num % i == 0:
            print("Not prime")
            break
        i += 1
    else:
        print("Prime")


def primeRange():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    i = num1
    while i <= num2:
        j = 2
        while j < i:
            if i % j == 0:
                print("Not prime")
                break
            j += 1
        else:
            print("Prime")
        i += 1


def stringcalc():
    str = input("Enter a string: ")
    i = 0
    sum = 0
    while i < len(str):
        if str[i].isdigit():
            sum = sum + int(str[i])
        i += 1
    print(sum)


def validitycheck():
    str = input("Enter a string: ")
    i = 0
    while i < len(str):
        if str[i] == "@":
            print("Valid")
            break
        i += 1
    else:
        print("Invalid")


def oddevencheck():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


def factorialfinder():
    num = int(input("Enter a number: "))
    i = 1
    factorial = 1
    while i <= num:
        factorial = factorial * i
        i += 1
    print(factorial)


def palindromecheck():
    str = input("Enter a string: ")
    i = 0
    j = len(str) - 1
    while i < len(str):
        if str[i] != str[j]:
            print("Not palindrome")
            break
        i += 1
        j -= 1
    else:
        print("Palindrome")


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
    i = 1
    while i <= num:
        if i * i == num:
            print("Perfect square")
            break
        i += 1
    else:
        print("Not perfect square")


def perfectNumberCheck():
    num = int(input("Enter a number: "))
    sum = 0
    i = 1
    while i < num:
        if num % i == 0:
            sum = sum + i
        i += 1
    if num == sum:
        print("Perfect number")
    else:
        print("Not perfect number")


def multiplicationTablerange():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    i = num1
    while i <= num2:
        j = 1
        while j <= 10:
            print(i, "x", j, "=", i * j)
            j += 1
        i += 1


def printSpecific():
    lst = [1, 2, 3, 4, 5]
    i = 0
    while i < len(lst):
        if lst[i] == 3:
            print(lst[i])
            break
        i += 1


def sumodd():
    lst = [1, 2, 3, 4, 5]
    sum = 0
    i = 0
    while i < len(lst):
        if lst[i] % 2 != 0:
            sum = sum + lst[i]
        i += 1
    print(sum)


def sumeven():
    lst = [1, 2, 3, 4, 5]
    sum = 0
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            sum = sum + lst[i]
        i += 1
    print(sum)


def countspace():
    str = input("Enter a string: ")
    i = 0
    count = 0
    while i < len(str):
        if str[i] == " ":
            count += 1
        i += 1
    print(count)


def changelist():
    lst = [1, 2, 3, 4, 5]
    i = 0
    while i < len(lst):
        if lst[i] == 3:
            lst[i] = 6
        i += 1
    print(lst)


def listmul():
    lst = [1, 2, 3, 4, 5]
    mul = 1
    i = 0
    while i < len(lst):
        mul = mul * lst[i]
        i += 1
    print(mul)


def breakloop():
    lst = [1, 2, 3, 4, 5]
    i = 0
    while i < len(lst):
        if lst[i] == 3:
            break
        print(lst[i])
        i += 1


def stringiteration():
    str = input("Enter a string: ")
    i = 0
    while i < len(str):
        print(str[i])
        i += 1


def listiteration():
    lst = [1, 2, 3, 4, 5]
    i = 0
    while i < len(lst):
        print(lst[i])
        i += 1


def listiteration2():
    lst = [1, 2, 3, 4, 5]
    i = len(lst) - 1
    while i >= 0:
        print(lst[i])
        i -= 1


def listappend():
    lst = [1, 2, 3, 4, 5]
    lst_new = []
    i = 0
    while i < len(lst):
        lst_new.append(lst[i])
        i += 1
    print(lst_new)


def listappend2():
    lst = [1, 2, 3, 4, 5]
    lst_new = []
    i = len(lst) - 1
    while i >= 0:
        lst_new.append(lst[i])
        i -= 1
    print(lst_new)


def loopContinue():
    lst = [1, 2, 3, 4, 5]
    i = 0
    while i < len(lst):
        if lst[i] == 3:
            i += 1
            continue
        print(lst[i])
        i += 1


def appendType():
    lst = [1, 2, 3, 4, 5]
    lst_new = []
    i = 0
    while i < len(lst):
        if type(lst[i]) == int:
            lst_new.append(lst[i])
        i += 1
    print(lst_new)


def loopElse():
    lst = [1, 2, 3, 4, 5]
    i = 0
    while i < len(lst):
        if lst[i] == 3:
            print("Found")
            break
        i += 1
    else:
        print("Not found")


def printSeries():
    lst = [1, 2, 3, 4, 5]
    i = 0
    while i < len(lst):
        if lst[i] == 3:
            print("Found")
            break
        i += 1
    else:
        print("Not found")


def badcharremove():
    str = input("Enter a string: ")
    i = 0
    while i < len(str):
        if str[i] == "@":
            i += 1
            continue
        print(str[i])
        i += 1


def countevenodd():
    lst = [1, 2, 3, 4, 5]
    even_count = 0
    odd_count = 0
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        i += 1
    print("Even count: ", even_count)
    print("Odd count: ", odd_count)


def printListData():
    lst = [1, 2, 3, 4, 5]
    i = 0
    while i < len(lst):
        print(lst[i])
        i += 1


def printListData2():
    lst = [1, 2, 3, 4, 5]
    i = 0
    while i < len(lst):
        print(lst[i])
        i += 1


def printListData3():
    lst = [1, 2, 3, 4, 5]
    i = 0
    while i < len(lst):
        print(lst[i])
        i += 1


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

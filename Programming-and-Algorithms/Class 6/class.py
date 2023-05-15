def add(num1, num2):
    """This adds the numbers sent in the argument and returns the sum"""
    return num1 + num2

print(add(3, 5))
print(add.__doc__) #This is why docstrings are executable and allocate memory


#logical operators
#and, or, not

a = 10
b = 20 
c = a + b
#and statements
print(a < b and c)
print(a > b and c)
#or statements
print(a < b or c)
print(a > b or c)
#not statements
print(not(a < b))
print(not(a > b))


for i in range(10):
    print(i, end=(" "))
    if i == 5:
        for j in range(3, 5):
            print(j, end=(" "))
print("\n")


a = 60
b = 13
c = 0 

c = a & b
print("Value of c is ", c)

c = a | b
print("Value of c is ", c)

c = a ^ b
print("Value of c is ", c)

c = ~a
print("Value of c is ", c)

c = a << 2
print("Value of c is ", c)

c = a >> 2
print("Value of c is ", c)

c = ~a 
c = ~c
print("Value of c is ", c)

a = 5
a = ~ a 
print(a)

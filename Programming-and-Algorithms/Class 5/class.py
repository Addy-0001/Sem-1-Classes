# print(10, 20, 30, sep = '/')
# print("Hi", end = " ")
# print("Hello")
# print(10, sep = "-")
# print("""hello""")
# a = eval(input())
# print(type(a))

# a = 15 # This is int, by definition
# b = input() # this is string because python accepts ONLY STRINGS WITH THE input() function. 

# num1 = int(input("Enter first number "))
# num2 = int(input("Enter second number "))
# num3 = int(input("Enter third number "))
# num4 = int(input("Enter fourth number "))
# num5 = int(input("Enter last number "))

# print("The sum is: ", num1 + num2 + num3 + num4 + num5)
# print("The product is: ", num1 * num2 * num3 * num4 * num5)
# print("The division is: ", num1 / num2 / num3 / num4 / num5)
# print("The division is: ", num1 - num2 - num3 - num4 - num5)

a = 20 + 3j 
print(type(a))

b = a.imag
print(b)
# print(a.real())

def function1():
    """
        This is docstring. this is not printed. It is not a comment either. 
        Docstrings are written when functions are defined. They are used to explain what the function does. 
    """
    print("This is function 1")


function1()

# sum = a + b
# print(sum)
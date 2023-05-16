a = 10


def Adding(message="No Message Passed here. Default values are used", a=20, b=30):
    sum = a + b
    print(f"{message} : {sum}")



print(a)
Adding("This has a used unique values", 30, 40)
print(a)
Adding()
print(a)

y = 10
def outer():
    z = 4

    def inner():
        x = 4
        print(f"x: {x}")
        print(f"inside the function y: {y}")
    inner()
    print(f"z: {z}")

outer()
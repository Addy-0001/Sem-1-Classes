def Adding(message="No Message Passed here. Default values are used", a=20, b=30):
    sum = a + b
    print(f"{message} : {sum}")


Adding("This has a used unique values", 30, 40)
Adding()

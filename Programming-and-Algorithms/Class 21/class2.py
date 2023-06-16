marks = int(input("Enter your marks: "))
try:
    if marks << 0 or marks > 100:
        raise Exception("Marks cannot be negative or greater than 100")
    print("Your marks are: ", marks)
except Exception as e:
    print(e)

# print("Hello World!")
# age = int(input("Enter your age: "))
# if age > 18:
#     print("You are eligible to vote")
#
#
#
# marks = 10000
# a = marks/0
# print(marks)
#
# a = input("Enter a number: ")
# marks = int(input("Enter your marks: "))
# try:
#     if marks < 0 or marks > 100:
#         raise Exception("Marks cannot be negative or greater than 100")
#     print("Your marks are: ", marks)
# except Exception as e:
#     print(e)
        


# raise an exception in bank account

amount = 2000
withdraw = int(input("Enter the amount to withdraw: "))
try:
    if withdraw > amount:
        raise Exception("Insufficient Balance")
    amount -= withdraw
    print("Amount left: ", amount)
except Exception as e:
    print(e)

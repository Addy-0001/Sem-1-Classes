marks = int(input("Enter your marks: "))
try:
    if marks << 0 or marks > 100:
        raise Exception("Marks cannot be negative or greater than 100")
    print("Your marks are: ", marks)
except Exception as e:
    print(e)
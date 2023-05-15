userName = input("Enter name: ")
balance = 985655544
print("Hello {name}, welcome to the app.".format(name = userName.title()))
# You can use positional argument before keyword argument but you can't do the other way around. 

#mixed arguments
print("Hello {0}, your balance is {blc}.".format("adam", blc = 3455))

print("hello {0}, your balance is {1}.".format("Adam", 12345)) # positional argument

print(f"Hi, {userName} welcome to the program. Your balance is {balance}") #The fprint function

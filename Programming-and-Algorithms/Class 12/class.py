# Printing A using Pattern
for row in range(6):
    for column in range(5):
        if ((row == 1 or row == 2 or row == 4 or row == 5) and (column == 0 or column == 4)):
            print("*", end=" ")
        elif (row == 3):
            print("*", end=" ")
        elif (row == 0 and (column == 1 or column == 2 or column == 3)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")
print("\n")

# Printing B using Pattern
for row in range(7):
    for column in range(4):
        if ((row == 0 or row == 3 or row == 6) and column != 3):
            print("*", end=" ")
        elif ((row == 1 or row == 2 or row == 4 or row == 5) and (column == 0 or column == 3)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")
print("\n")

# Printing C using Pattern
for row in range(7):
    for column in range(4):
        if ((row == 0 or row == 6) and column != 0):
            print("*", end=" ")
        elif ((row == 1 or row == 2 or row == 3 or row == 4 or row == 5) and column == 0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")
print("\n")

# Printing D using Pattern
for row in range(7):
    for column in range(4):
        if ((row == 0 or row == 6) and column != 3):
            print("*", end=" ")
        elif ((row == 1 or row == 2 or row == 3 or row == 4 or row == 5) and (column == 0 or column == 3)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")
print("\n")


# Printing E using Pattern
for row in range(7):
    for column in range(4):
        if ((row == 0 or row == 3 or row == 6) and column != 3):
            print("*", end=" ")
        elif ((row == 1 or row == 2 or row == 4 or row == 5) and column == 0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")
print("\n")

# Printing F using Pattern
for row in range(7):
    for column in range(4):
        if ((row == 0 or row == 3) and column != 3):
            print("*", end=" ")
        elif ((row == 1 or row == 2 or row == 4 or row == 5 or row == 6) and column == 0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")
print("\n")

# Printing G using Pattern
for row in range(7):
    for column in range(4):
        if (row == 0 and column != 0):
            print("*", end=" ")
        elif ((row == 1 or row == 2 or row == 3) and column == 0):
            print("*", end=" ")
        elif (row == 4 and column != 1):
            print("*", end=" ")
        elif (row == 5 and (column == 0 or column == 3)):
            print("*", end=" ")
        elif (row == 6 and column != 0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")
print("\n")

# Printing M using Pattern 
for row in range(6):
    for column in range(5):
        if(column == 0 or column == 4):
            print("*", end = " ")
        elif(row == 1 and (column == 1 or column == 3)):
            print("*", end=" ")
        elif(row == 2 and column == 2):
            print("*", end=" ")
        else: 
            print(" ", end=" ")
    print("")
            
# Print "Adamya" using pattern

for row in range(6):
    for column in range(25):
        if ((column == 1 or column == 4 or column == 9 or column == 12 or column == 16 or column == 18 or column == 20 or column == 23) and row == 0):
            print('#', end=' ')
        elif ((row == 1 or row == 2 or row == 3 or row == 4 or row == 5) and (column == 0 or column == 2 or column == 4 or column == 10 or column == 8 or column == 12 or column == 16 or column == 19 or column == 22 or column == 24)):
            print('#', end=' ')
        elif ((row == 1 or row == 2 or row == 3 or row == 4) and column == 6):
            print('#', end=' ')
        elif ((row == 5 or row == 0) and column == 5):
            print('#', end=' ')
        elif ((row == 3) and (column == 1 or column == 9 or column == 23)):
            print('#', end=' ')
        elif ((row == 1) and (column == 13 or column == 15) or ((row == 2) and (column == 14))):
            print('#', end=' ')
        else:
            print(" ", end=" ")
    print("")
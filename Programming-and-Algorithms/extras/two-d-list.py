# Make a matrix and replace the rows with column and column with rows

# Making the matrix
row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
matrix = []
mat_row = []
data = 0

for i in range(row):
    for j in range(column):
        data = int(input(f"Enter element {i+1}x{j+1}: "))
        mat_row.append(data)
    matrix.append(mat_row)
    mat_row = []

# Printing the matrix as is
for matrix_column in matrix:
    for matrix_row in matrix_column:
        print(matrix_row, end=" ")
    print("")

# replacing the rows with columns and columns with rows
temp = row
row = column
column = temp

# Printing the replaced rows and columns
for i in range(row):
    for j in range(column):
        print(matrix[j][i], end=" ")
    print("")

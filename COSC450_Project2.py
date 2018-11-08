# Steven Hogenson
# COSC450 Project 2
# 12/7/2018
#
# This program will read in integers from a text file and sort the integers into two
# matrices. These matrices are then multiplied together. The original matrices and the product are written to an output
# text file. The product matrix gets sorted and this sorted matrix is written to the output file also.


# gets integers from the text file
inputFile = open("COSC450_P2_Data.txt", "r")
intStorage = []  # array where the integers will be stored

for val in inputFile.read().split():
    intStorage.append(int(val))  # append the integers from the file to array intStorage
inputFile.close()

m1Cols_m2Rows = int(intStorage.__len__() / 5)

# make Matrix 1
rows = 5
cols = m1Cols_m2Rows
A = [[0] * cols for _ in range(rows)]  # makes a 5*X matrix filled with 0s
count = 0
for i in range(5):
    for j in range(m1Cols_m2Rows):
        A[i][j] = intStorage[count]  # fills 5*X matrix with the integers from intStorage
        count = count + 1

# make Matrix 2
rows = m1Cols_m2Rows
cols = 5
B = [[0] * cols for _ in range(rows)]  # makes a X*5 matrix filled with 0s
count = 0
for i in range(m1Cols_m2Rows):
    for j in range(5):
        B[i][j] = intStorage[count]  # fills X*5 matrix with the integers from intStorage
        count = count + 1

def matrixmult(A, B):
    C = [[0 for _ in range(5)] for _ in range(5)]  # makes a 5*5 matrix filled with 0s
    for i in range(5):
        for j in range(5):
            for k in range(m1Cols_m2Rows):
                C[i][j] += A[i][k] * B[k][j]  # fills C with the product of Matrix 1 and Matrix 2
    return C

def writeFile(write_orAppend, rows, columns, matrix, matrixName):
    with open("COSC450_P2_Output.txt", write_orAppend) as text_file:
        text_file.write(matrixName)
        for i in range(rows):
            for j in range(columns):
                text_file.write(str(matrix[i][j]) + " ")
            text_file.write("\n")

def sortMatrix(matrix):
    for i in range(25):
        for j in range(24):
            currentRow = int(j / 5)
            currentColumn = j % 5
            currentRow_orNextRow = int((j + 1) / 5)
            nextColumn = (j + 1) % 5

            # simple swap algorithm
            if matrix[currentRow][currentColumn] > matrix[currentRow_orNextRow][nextColumn]:
                temp = matrix[currentRow][currentColumn]
                matrix[currentRow][currentColumn] = matrix[currentRow_orNextRow][nextColumn]
                matrix[currentRow_orNextRow][nextColumn] = temp

    return matrix

C = matrixmult(A, B)
writeFile("w", 5, m1Cols_m2Rows, A, "Matrix 1: \n")
writeFile("a", m1Cols_m2Rows, 5, B, "\nMatrix 2: \n")
writeFile("a", 5, 5, C, "\nMatrix Product: \n")
writeFile("a", 5, 5, sortMatrix(C), "\nMatrix Product Sorted: \n")

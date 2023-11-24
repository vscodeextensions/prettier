import numpy as np

def add_matrix(A, B):
    total = []
    for i in range(len(A)):
        rows = []
        for j in range(len(B)):
            rows.append(A[i][j] + B[i][j])
        total.append(rows)
    return total

def subtract_matrix(A, B):
    total = []
    for i in range(len(A)):
        rows = []
        for j in range(len(B)):
            rows.append(A[i][j] - B[i][j])
        total.append(rows)
    return total

def multiply_matrix(A, B):
    if len(A[0]) != len(B):
        print("The number of columns in matrix A must be equal to the number of rows in matrix B.")
        return
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            row.append(0)
        result.append(row)
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def divide_matrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Both matrices must have the same dimensions for division.")
        return
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            if B[i][j] != 0:
                row.append(A[i][j] / B[i][j])
            else:
                print("Division by zero is not allowed.")
        result.append(row)
    return result

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j], end=' ')
        print("\n")

def create_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(int(input(f"Enter element at row {i+1} and column {j+1}: ")))
        matrix.append(row)
    return matrix

# Main program loop
while True:
    print("Matrix Operations Menu:")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Divide Matrices")
    print("5. Quit")
    
    choice = input("Enter your choice : ")
    
    if choice == '1':
        A = create_matrix(int(input("Enter the number of rows for Matrix A: ")), int(input("Enter the number of columns for Matrix A: ")))
        B = create_matrix(int(input("Enter the number of rows for Matrix B: ")), int(input("Enter the number of columns for Matrix B: ")))
        print("Matrix A : \n")
        print_matrix(A)
        print("Matrix B : \n")
        print_matrix(B)
        result = add_matrix(A, B)
        print("Result of Matrix Addition:")
        print_matrix(result)
    elif choice == '2':
        A = create_matrix(int(input("Enter the number of rows for Matrix A: ")), int(input("Enter the number of columns for Matrix A: ")))
        B = create_matrix(int(input("Enter the number of rows for Matrix B: ")), int(input("Enter the number of columns for Matrix B: ")))
        print("Matrix A : \n")
        print_matrix(A)
        print("Matrix B : \n")
        print_matrix(B)
        result = subtract_matrix(A, B)
        print("Result of Matrix Subtraction:")
        print_matrix(result)
    elif choice == '3':
        A = create_matrix(int(input("Enter the number of rows for Matrix A: ")), int(input("Enter the number of columns for Matrix A: ")))
        B = create_matrix(int(input("Enter the number of rows for Matrix B: ")), int(input("Enter the number of columns for Matrix B: ")))
        print("Matrix A : \n")
        print_matrix(A)
        print("Matrix B : \n")
        print_matrix(B)
        result = multiply_matrix(A, B)
        if result:
            print("Result of Matrix Multiplication:")
            print_matrix(result)
    elif choice == '4':
        A = create_matrix(int(input("Enter the number of rows for Matrix A: ")), int(input("Enter the number of columns for Matrix A: ")))
        B = create_matrix(int(input("Enter the number of rows for Matrix B: ")), int(input("Enter the number of columns for Matrix B: ")))
        print("Matrix A : \n")
        print_matrix(A)
        print("Matrix B : \n")
        print_matrix(B)
        result = divide_matrix(A, B)
        if result:
            print("Result of Matrix Division:")
            print_matrix(result)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option !!")
"""
OUTPUT :
Matrix Operations Menu:
1. Add Matrices
2. Subtract Matrices
3. Multiply Matrices
4. Divide Matrices
5. Quit
Enter your choice : 1
Enter the number of rows for Matrix A: 2
Enter the number of columns for Matrix A: 2
Enter element at row 1 and column 1: 2
Enter element at row 1 and column 2: 3
Enter element at row 2 and column 1: 4
Enter element at row 2 and column 2: 5
Enter the number of rows for Matrix B: 2
Enter the number of columns for Matrix B: 2
Enter element at row 1 and column 1: 2
Enter element at row 1 and column 2: 3
Enter element at row 2 and column 1: 4
Enter element at row 2 and column 2: 5
Matrix A : 
2 3 
4 5 
Matrix B : 
2 3 
4 5 
Result of Matrix Addition:
4 6 
8 10 
Enter your choice : 2
Enter the number of rows for Matrix A: 2
Enter the number of columns for Matrix A: 2
Enter element at row 1 and column 1: 2
Enter element at row 1 and column 2: 3
Enter element at row 2 and column 1: 4
Enter element at row 2 and column 2: 5
Enter the number of rows for Matrix B: 2
Enter the number of columns for Matrix B: 2
Enter element at row 1 and column 1: 2
Enter element at row 1 and column 2: 3
Enter element at row 2 and column 1: 4
Enter element at row 2 and column 2: 5
Matrix A : 
2 3 
4 5 
Matrix B : 
2 3 
4 5 
Result of Matrix Subtraction:
0 0 
0 0 
Enter your choice : 3

"""




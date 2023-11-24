import numpy as np

def find_transpose():
    rows = int(input("Enter the number of rows for the matrix: "))
    columns = int(input("Enter the number of columns for the matrix: "))
    
    matrix = np.empty((rows, columns))
    
    print("Enter elements for the matrix:")
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = float(input(f"Enter element at row {i+1} and column {j+1}: "))
    
    transpose_matrix = np.transpose(matrix)
    
    print("\nOriginal Matrix:")
    print(matrix)
    
    print("\nTranspose of the Matrix:")
    print(transpose_matrix)

def solve_linear_system():
    num_variables = int(input("Enter the number of variables in the system: "))
    
    A = np.empty((num_variables, num_variables))
    B = np.empty(num_variables)
    
    print("Enter the coefficients of the linear system (matrix A):")
    for i in range(num_variables):
        for j in range(num_variables):
            A[i][j] = float(input(f"Enter coefficient A[{i+1}][{j+1}]: "))
    
    print("\nEnter the constants (vector B):")
    for i in range(num_variables):
        B[i] = float(input(f"Enter constant B[{i+1}]: "))
    
    solution = np.linalg.solve(A, B)
    
    print("\nSolution of the Linear System:")
    for i in range(num_variables):
        print(f"x{i+1} =", solution[i])

# Main program loop
while True:
    print("\nMenu:")
    print("1. Find Transpose of a Matrix")
    print("2. Solve a Linear System of Equations")
    print("3. Quit")
    
    choice = input("Enter your choice : ")
    
    if choice == '1':
        find_transpose()
    elif choice == '2':
        solve_linear_system()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")

        
"""
Menu:
1. Find Transpose of a Matrix
2. Solve a Linear System of Equations
3. Quit
Enter your choice : 1
Enter the number of rows for the matrix: 2
Enter the number of columns for the matrix: 2
Enter elements for the matrix:
Enter element at row 1 and column 1: 1
Enter element at row 1 and column 2: 2
Enter element at row 2 and column 1: 3
Enter element at row 2 and column 2: 4

Original Matrix:
[[1. 2.]
 [3. 4.]]

Transpose of the Matrix:
[[1. 3.]
 [2. 4.]]

Enter your choice : 2
Enter the number of variables in the system: 2
Enter the coefficients of the linear system (matrix A):
Enter coefficient A[1][1]: 3
Enter coefficient A[1][2]: 4
Enter coefficient A[2][1]: 1
Enter coefficient A[2][2]: -1

Enter the constants (vector B):
Enter constant B[1]: 5
Enter constant B[2]: 0

Solution of the Linear System:
x1 = 0.7142857142857143
x2 = 0.7142857142857143
"""



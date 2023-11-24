import numpy as np
import pandas as pd

def check_prime(x):
    if x < 2:
        return False
    if x==2:
        return True
    for i in range(2, int(x ** 0.5) + 2):
        if x % i == 0:
            return False
    return True

choice = 0
while choice != 4:
    print("1. Generate random numbers and print the frequency of numbers")
    print("2. Even and Odd numbers from between a range of your choice")
    print("3. Read CSV file")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        num_dict = {}
        num_count = int(input('Enter the number of random numbers you want to generate: '))
        a = np.random.normal(0, 1, num_count)
        new_a = np.round(a * 100)
        for num in new_a:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
        print("\nInteger\tFrequency")
        for key, value in num_dict.items():
            print(f'{int(key)}\t{value}')

    elif choice == 2:
        m = int(input("Enter the start: "))
        n = int(input("Enter the end: "))
        even = [i for i in range(m, n + 1) if i % 2 == 0]
        odd = [i for i in range(m, n + 1) if i % 2 != 0]
        prime = [i for i in range(m, n + 1) if check_prime(i)]
        print("Even numbers:", even)
        print("Odd numbers:", odd)
        print("Prime numbers:", prime)

    elif choice == 3:
        csv_addr = "https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/organizations/organizations-100.csv"
        custom_addr = input("Enter the address of the CSV file (press Enter for the default CSV): ").strip()
        if custom_addr:
            csv_addr = custom_addr
        try:
            csv_file = pd.read_csv(csv_addr)
            print("Columns in your CSV file are:\n")
            for col in csv_file.columns:
                print(col)
            req_col = input("Enter the column name you want: ")
            if req_col in csv_file.columns:
                print("The required column is:\n")
                print(csv_file[req_col])
            else:
                print("Column not present in dataset (Might be a spelling error)")
        except pd.errors.EmptyDataError:
            print("The CSV file is empty.")
        except pd.errors.ParserError:
            print("Error parsing CSV file. Please check the file format.")
            
    elif choice == 4:
        print("Exiting the program.")
        
    else:
        print("Invalid choice. Please enter a valid option.")

        
"""
OUTPUT:
1. Generate random numbers and print the frequency of numbers
2. Even and Odd numbers from between a range of your choice
3. Read CSV file
4. Exit
Enter your choice: 1
Enter no. of random numbers you want to generate: 10
Integer Frequency
-81 1
-32 1
152 1
122 1
40 1
82 1
120 1
86 1
65 1
-1 1
Enter your choice: 2
Enter the start: 44 
Enter the end: 88
Even numbers: [44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88]
Odd numbers: [45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87]
Prime numbers: [47, 53, 59, 61, 67, 71, 73, 79, 83]
Enter your choice: 3
Enter 1 if you want to enter the address of the CSV file
For the default CSV file, press any integer: 2
Columns in your CSV file are:
Index
Organization Id
Name
Website
Country
Description
Founded
Industry
Number of employees
Enter the column name you want: Name
The required column is:
0 Ferrell LLC
1 Mckinney, Riley and Day
2 Hester Ltd
3 Holder-Sellers
4 Mayer Group
 ... 
95 Holmes Group
96 Good Ltd
97 Clements-Espinoza
98 Mendez Inc
99 Watkins-Kaiser
Name: Name, Length: 100, dtype: object
Enter the data index you want to select: 98
The element selected from the CSV file is Mendez Inc
"""


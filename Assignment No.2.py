import numpy as np
import pandas as pd

# Initialize choice variable
choice = 0

# Loop until the user chooses to exit
while choice != 3:
    print("1. Unpack Tuple\n")
    print("2. Merge dict\n")
    print("3. Exit\n")
    
    # Get user choice
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        # Unpack a tuple and print its values
        packed_tuple = (1, 3, 4)
        rank1, rank2, rank3 = packed_tuple
        print(f'Variable:\nrank1 has value {rank1}\nrank2 has value {rank2}\nrank3 has value {rank3}\n')

    elif choice == 2:
        # Merge two dictionaries
        print("Enter first dict of fruits:\n")
        dict_1 = {}
        for i in range(int(input('Number of fruits you want to enter in dict_1: '))):
            dict_1[str(input('Enter fruit name: '))] = int(input("Enter no. of fruits you have: "))
        
        print("Enter second dict of fruits:\n")
        dict_2 = {}
        for i in range(int(input('Number of fruits you want to enter in dict_2: '))):
            dict_2[str(input('Enter fruit name: '))] = int(input("Enter no. of fruits you have: "))
        
        dict_2.update(dict_1)
        print(f'Your merged list of fruits is: {dict_2}')

    elif choice == 3:
        # Exit the program
        print("Exiting Program !!")

    else:
        # Invalid choice
        print("Enter a valid choice !!")
"""
OUTPUT :
1. Unpack Tuple
2. Merge dict
3. Exit
Enter your choice: 1
Variable:
rank1 has value 1
rank2 has value 3
rank3 has value 4
1. Unpack Tuple
2. Merge dict
3. Exit
Enter your choice: 2
Enter first dict of fruits:
Number of fruits you want to enter in dict_1: 1
Enter no. of fruits you have: 4
Enter fruit name: Apple
Enter second dict of fruits:
Number of fruits you want to enter in dict_2: 2
Enter no. of fruits you have: 3
Enter fruit name: Orange
Enter no. of fruits you have: 5
Enter fruit name: Pineapple
Your merged list of fruits is: {'Orange': 3, 'Pineapple': 5, 'Apple': 4}
 
"""


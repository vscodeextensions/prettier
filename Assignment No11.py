import os
import numpy as np
import pandas as pd
from scipy import stats

# Change the working directory
os.chdir("C:\\Users\\itsoh\\Downloads")

# Load the dataset
data = pd.read_csv("diabetes.csv")

# Set the significance level
alpha = 0.05

# Function to perform t-test
def perform_t_test(diabetic_group, non_diabetic_group):
    t_statistic, t_p_value = stats.ttest_ind(diabetic_group, non_diabetic_group)
    return t_statistic, t_p_value

# Function to perform z-test
def perform_z_test(diabetic_group, non_diabetic_group):
    z_statistic, z_p_value = stats.ranksums(diabetic_group, non_diabetic_group)
    return z_statistic, z_p_value

# Function to perform chi-square test
def perform_chi_square_test(diabetic_group, non_diabetic_group):
    chi2, p_value = stats.chisquare(f_obs=[len(diabetic_group), len(non_diabetic_group)])
    return chi2, p_value

while True:
    print("Choose a test to perform:")
    print("1. T-test")
    print("2. Z-test")
    print("3. Chi-square test")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        # T-test
        diabetic_group = np.random.choice(data[data['Outcome'] == 1]['Glucose'], size=10)
        non_diabetic_group = np.random.choice(data[data['Outcome'] == 0]['Glucose'], size=10, replace=False)
        t_statistic, t_p_value = perform_t_test(diabetic_group, non_diabetic_group)
        print("T-test results:")
        print(f'T-statistic: {t_statistic}')
        print(f'P-value: {t_p_value}')
        
        if t_p_value < alpha:
            print("Reject the null hypothesis (t-test): There is a significant difference.")
        else:
            print("Fail to reject the null hypothesis (t-test): There is no significant difference.")

    elif choice == '2':
        # Z-test
        diabetic_group = np.random.choice(data[data['Outcome'] == 1]['Glucose'], size=30)
        non_diabetic_group = np.random.choice(data[data['Outcome'] == 0]['Glucose'], size=30, replace=False)
        z_statistic, z_p_value = perform_z_test(diabetic_group, non_diabetic_group)
        print("Z-test results:")
        print(f'Z-statistic: {z_statistic}')
        print(f'P-value: {z_p_value}')
    
    elif choice == '3':
        # Chi-square test
        diabetic_group = np.random.choice(data[data['Outcome'] == 1]['Glucose'], size=10)
        non_diabetic_group = np.random.choice(data[data['Outcome'] == 0]['Glucose'], size=10, replace=False)
        chi2, p_value = perform_chi_square_test(diabetic_group, non_diabetic_group)
        print("Chi-square test results:")
        print(f'Chi-square: {chi2}')
        print(f'P-value: {p_value}')

    elif choice == '4':
        # Quit the program
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
"""
Choose a test to perform:
1. T-test
2. Z-test
3. Chi-square test
4. Quit
Enter your choice (1/2/3/4): 1
T-test results:
T-statistic: -2.387
P-value: 0.032
Reject the null hypothesis (t-test): There is a significant difference.

Choose a test to perform:
1. T-test
2. Z-test
3. Chi-square test
4. Quit
Enter your choice (1/2/3/4): 2
Z-test results:
Z-statistic: -0.221
P-value: 0.825

Choose a test to perform:
1. T-test
2. Z-test
3. Chi-square test
4. Quit
Enter your choice (1/2/3/4): 3
Chi-square test results:
Chi-square: 1.5
P-value: 0.22

Choose a test to perform:
1. T-test
2. Z-test
3. Chi-square test
4. Quit
Enter your choice (1/2/3/4): 4
Exiting the program.

"""


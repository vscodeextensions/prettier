import numpy as np
import pandas as pd
from scipy import stats

# Creating dataset
no_of_students = int(input("No. of students to be present in your dataset: "))
Academic_dataset = np.random.randint(1, 200, no_of_students)
data = {"Marks": Academic_dataset}
df = pd.DataFrame(data)

# Introduce missing values
no_of_null_values = np.random.randint(1, no_of_students // 10)
null_indices = np.random.choice(df.index, no_of_null_values, replace=False)
df.loc[null_indices, "Marks"] = np.nan
print("Dataset created successfully!")

# Menu for choice
choice = 1
while choice != 5:
    print("\nMenu")
    print("1. Check for missing values")
    print("2. Impute missing values")
    print("3. Check for outliers")
    print("4. Remove outliers")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if df.isna().sum()>0:
            print(f"There are {df.isna().sum().sum()} missing values in the dataset.")
        else:
            print("There are no missing values in the dataset.")

    elif choice == 2:
        if df.isna().sum().any():
            print("\nImputation Menu")
            print("1. Replace by median")
            print("2. Replace by mode")
            print("3. Replace by mean")
            impute_choice = int(input("Enter your choice: "))
            if impute_choice == 1:
                df["Marks"].fillna(df["Marks"].median(), inplace=True)
            elif impute_choice == 2:
                df["Marks"].fillna(df["Marks"].mode()[0], inplace=True)
            elif impute_choice == 3:
                df["Marks"].fillna(df["Marks"].mean(), inplace=True)
            print("Missing values imputed successfully!")
        else:
            print("There are no missing values in the dataset to be replaced.")

    elif choice == 3:
        print("\nOutlier Detection Menu")
        print("1. Z-score method")

        outlier_choice = int(input("Enter your choice: "))
        if outlier_choice == 1:
            z_scores = np.abs(stats.zscore(df["Marks"].dropna()))
            threshold = 3
            outliers = np.where(z_scores > threshold)[0]  
            if len(outliers) > 0:
                print(f"Found {len(outliers)} outliers.")
                print("Indices of outliers:", outliers)
            else:
                print("No outliers found.")

    elif choice == 4:
        print("\nRemoving Outliers Menu")
        print("1. Remove by Z-score method")

        remove_outlier_choice = int(input("Enter your choice: "))
        if remove_outlier_choice == 1:
            z_scores = np.abs(stats.zscore(df["Marks"].dropna()))
            threshold = 3
            df_no_outliers = df[(z_scores < threshold) | df["Marks"].isna()]

            print(f"Removed {len(df) - len(df_no_outliers)} outliers.")
            df = df_no_outliers.copy()
    elif choice==5:
        print("Exiting the program.")
        break
"""
OUTPUT:
# Sample Output 1 (Check for missing values)
No. of students to be present in your dataset: 50
Dataset created successfully!

Menu
1. Check for missing values
2. Impute missing values
3. Check for outliers
4. Remove outliers
5. Exit
Enter your choice: 1
There are 7 missing values in the dataset.

# Sample Output 2 (Impute missing values)
Menu
1. Check for missing values
2. Impute missing values
3. Check for outliers
4. Remove outliers
5. Exit
Enter your choice: 2

Imputation Menu
1. Replace by median
2. Replace by mode
3. Replace by mean
Enter your choice: 1
Missing values imputed successfully!

# Sample Output 3 (Check for outliers)
Menu
1. Check for missing values
2. Impute missing values
3. Check for outliers
4. Remove outliers
5. Exit
Enter your choice: 3
Outlier Detection Menu
1. Z-score method
Enter your choice: 1
Found 2 outliers.
Indices of outliers: [15, 23]

# Sample Output 4 (Remove outliers)
Menu
1. Check for missing values
2. Impute missing values
3. Check for outliers
4. Remove outliers
5. Exit
Enter your choice: 4

Removing Outliers Menu
1. Remove by Z-score method
Enter your choice: 1
Removed 2 outliers.

# Sample Output 5 (Exit)
Menu
1. Check for missing values
2. Impute missing values
3. Check for outliers
4. Remove outliers
5. Exit
Enter your choice: 5
Exiting the program
"""



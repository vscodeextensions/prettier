import pandas as pd
import os

# Change the working directory
os.chdir("C:\\Users\\itsoh\\Downloads\\")

# Read the Iris dataset
df = pd.read_csv("iris.csv")

while True:
    print("Menu:")
    print("1. Calculate Mean, Median, Mode, and Standard Deviation for a specific column")
    print("2. Calculate Correlation between features")
    print("3. Calculate Covariance between features")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        column_name = input("Enter the column name you want to analyze: ")

        if column_name in df.columns and pd.api.types.is_numeric_dtype(df[column_name]):
            print(f"For column {column_name}:")
            print(f"\tMean: {df[column_name].mean():.2f}")
            
            if len(df[column_name].mode()) == 1:
                print(f"\tMode: {df[column_name].mode().iloc[0]}")
            else:
                count = 1
                for i in df[column_name].mode():
                    print(f"\t{count} Mode: {i}")
                    count += 1

            print(f"\tMedian: {df[column_name].median():.2f}")
            print(f"\tStandard Deviation: {df[column_name].std():.2f}")
        else:
            print("Invalid column name or non-numeric column.")

    elif choice == "2":
        updated_df1 = df[df.columns[:-1]]  # Removing the last string type column
        correlation_matrix = updated_df1.corr()

        print("Correlation Matrix:")
        print("Positive Correlations: (Directly Proportional)")
        for i, col1 in enumerate(correlation_matrix.columns):
            for j, col2 in enumerate(correlation_matrix.columns):
                if i >= j:
                    continue
                if correlation_matrix.iloc[i, j] > 0:
                    print(f"{col1} and {col2}: {correlation_matrix.iloc[i, j]:.2f}")

        print("Negative Correlations: (Inversely Proportional)")
        for i, col1 in enumerate(correlation_matrix.columns):
            for j, col2 in enumerate(correlation_matrix.columns):
                if i >= j:
                    continue
                if correlation_matrix.iloc[i, j] < 0:
                    print(f"{col1} and {col2}: {correlation_matrix.iloc[i, j]:.2f}")

        print()

    elif choice == "3":
        updated_df2 = df[df.columns[:-1]]  # Removing the last string type column
        covariance_matrix = updated_df2.cov()

        print("Covariance Matrix:")
        print("Positive Covariances: (Directly Proportional)")
        for i, col1 in enumerate(covariance_matrix.columns):
            for j, col2 in enumerate(covariance_matrix.columns):
                if i >= j:
                    continue
                if covariance_matrix.iloc[i, j] > 0:
                    print(f"{col1} and {col2}: {covariance_matrix.iloc[i, j]:.2f}")

        print()

    elif choice == "4":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
"""
OUTPUT : 
Menu:
1. Calculate Mean, Median, Mode, and Standard Deviation for a specific column
2. Calculate Correlation between features
3. Calculate Covariance between features
4. Exit
Enter your choice: 1
Enter the column name you want to analyze: SepalLengthCm
For column SepalLengthCm:
        Mean: 5.84
        Mode: 5.0
        Median: 5.8
        Standard Deviation: 0.83

Menu:
1. Calculate Mean, Median, Mode, and Standard Deviation for a specific column
2. Calculate Correlation between features
3. Calculate Covariance between features
4. Exit
Enter your choice: 2
Correlation Matrix:
Positive Correlations: (Directly Proportional)
SepalLengthCm and SepalWidthCm: -0.37
SepalLengthCm and PetalLengthCm: 0.87
SepalLengthCm and PetalWidthCm: 0.82
SepalWidthCm and PetalLengthCm: -0.37
SepalWidthCm and PetalWidthCm: -0.37
PetalLengthCm and PetalWidthCm: 0.96

Negative Correlations: (Inversely Proportional)

Menu:
1. Calculate Mean, Median, Mode, and Standard Deviation for a specific column
2. Calculate Correlation between features
3. Calculate Covariance between features
4. Exit
Enter your choice: 3
Covariance Matrix:
Positive Covariances: (Directly Proportional)
SepalLengthCm and SepalWidthCm: -0.04
SepalLengthCm and PetalLengthCm: 1.27
SepalLengthCm and PetalWidthCm: 0.52
SepalWidthCm and PetalLengthCm: -0.36
SepalWidthCm and PetalWidthCm: -0.15
PetalLengthCm and PetalWidthCm: 0.53

Menu:
1. Calculate Mean, Median, Mode, and Standard Deviation for a specific column
2. Calculate Correlation between features
3. Calculate Covariance between features
4. Exit
Enter your choice: 4
Exiting the program.

"""



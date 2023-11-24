import pandas as pd
import matplotlib.pyplot as plt
import os
# Change the working directory
os.chdir("C:\\Users\\itsoh\\Downloads\\")

# Load the dataset
df = pd.read_csv("iris.csv")

def create_histograms():
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    axs = axs.ravel()
    for i, column in enumerate(df.columns[:-1]):
        axs[i].hist(df[column], bins=10, edgecolor='black')
        axs[i].set_xlabel(column)
        axs[i].set_ylabel('Frequency')
        axs[i].set_title(f'Histogram for {column}')
    
    plt.tight_layout()
    plt.show()

def create_boxplot():
    plt.boxplot(df.iloc[:, :-1].values, labels=df.columns[:-1])
    plt.xlabel('Features')
    plt.ylabel('Values')
    plt.title('Box Plot for Features')
    plt.show()

while True:
    print("Menu:")
    print("1. Create Histograms")
    print("2. Create Box Plot")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        create_histograms()
    elif choice == "2":
        create_boxplot()
        print("In the boxplot, the two ends of the box represent +-1.5 IQR range.")
        print("In the feature 'Sepal width', the circles outside the range represent outliers.")
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")


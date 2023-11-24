import squarify
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import Normalizer
from scipy.cluster.hierarchy import dendrogram, linkage

os.chdir("C:\\Users\\itsoh\\Downloads\\")
df = pd.read_csv("diabetes.csv")
df.columns = df.columns.str.lower()


def get_column_name():
    column_name = input("Enter the column name: ")
    return column_name.lower()


def create_tree_map(series, title):
    squarify.plot(series)
    plt.title(title)
    plt.show()


def create_line_plot(x_data, y_data, title, x_label, y_label):
    plt.figure()
    plt.plot(x_data, y_data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def create_scatter_plot(x_data, y_data, title, x_label, y_label):
    plt.figure()
    plt.scatter(x_data, y_data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def create_bar_plot(x_data, y_data, title, x_label, y_label):
    plt.figure()
    plt.bar(x_data, y_data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def create_density_plot(x_data, title, x_label):
    plt.figure()
    plt.hist(x_data, density=True)
    plt.title(title)
    plt.xlabel(x_label)
    plt.show()


def create_pie_chart(x_data, y_data, title):
    plt.figure()
    plt.pie(y_data, labels=x_data, autopct="%1.1f%%")
    plt.title(title)
    plt.show()


def create_bubble_plot(x_data, y_data, size_data, title, x_label, y_label):
    plt.figure()
    plt.scatter(x_data, y_data, s=size_data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def create_heatmap(matrix, title, x_label, y_label):
    plt.figure()
    plt.imshow(matrix, cmap='hot')
    plt.title(title)
    plt.xlabel(', '.join(x_label.tolist()))
    plt.ylabel(', '.join(y_label.tolist()))
    plt.colorbar()
    plt.show()


def create_dendrogram(df, title):
    print("Creating Dendrogram")
    print("Dendrogram for the above dataset is:")
    Z = linkage(df, method='ward')
    labels = df.columns[1:]
    plt.figure(figsize=(12, 8))
    dendrogram(Z)
    plt.xlabel('Features')
    plt.ylabel('Distance')
    plt.xticks(rotation=90)
    plt.show()


def create_correlation_matrix(df, title):
    corr_matrix = df.corr()
    print("Correlation Matrix (as Table):")
    print(corr_matrix)
    print("\nCorrelation Matrix (DataFrame Format):")
    print(corr_matrix.to_string())
    plt.figure()
    plt.matshow(corr_matrix, cmap='hot')
    plt.title(title)
    plt.xlabel('Features')
    plt.ylabel('Features')
    plt.colorbar()
    plt.show()


while True:
    print("Menu:")
    print("1. Line plot")
    print("2. Scatter plot")
    print("3. Bar plot")
    print("4. Density plot")
    print("5. Pie chart")
    print("6. Bubble plot")
    print("7. Heatmaps")
    print("8. Treemap")
    print("9. Correlation matrices")
    print("10. Dendrograms")
    print("11. Exit")
    print('Columns names (for options): pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age, outcome')

    choice = input("Enter your choice: ")

    if choice == "1":
        temp = 0
        while temp != 5:
            print("\nPlotting Line Plot\n")
            print("1. SkinThickness Vs BMI\n2. Age Vs Insulin\n3. BloodPressure Vs Age")
            print("Custom feature names")
            print("5. Exit to main menu")
            print("Enter your Choice : ")
            temp = int(input())

            if temp == 1 or temp == 2 or temp == 3 or temp == 4 or temp == 5:
                if temp == 1:
                    x_column = "skinthickness"
                    y_column = "bmi"
                elif temp == 2:
                    x_column = "age"
                    y_column = "insulin"
                elif temp == 3:
                    x_column = "bloodpressure"
                    y_column = "age"
                elif temp == 4:
                    x_column = get_column_name()
                    y_column = get_column_name()
                elif temp == 5:
                    break

                create_line_plot(df[x_column], df[y_column], "Line Plot", x_column, y_column)

            else:
                print("Enter a valid input!")

        print("Interpretation from line plot:\nFor this dataset, all line plots are irregular and cannot form any unique pattern or curve. More like scatterplot results are obtained.")

    elif choice == "2":
        while True:
            print("Scatter Plot Menu:")
            print("1. Blood Pressure vs. Age")
            print("2. BMI vs. Glucose Levels")
            print("3. Insulin Levels vs. Age")
            print("4. Skin Thickness vs. BMI")
            print("5. Exit to main menu")
            print("Enter your choice: ")
            temp = input()

            if temp == "1" or temp == "2" or temp == "3" or temp == "4" or temp == "5":
                if temp == "1":
                    x_column = "bloodpressure"
                    y_column = "age"
                    title = 'Blood Pressure vs. Age'
                    print("Interpretation:")
                    print("- There are outliers as some entries of blood pressures.")
                    print("- Majority of blood pressure lies between 60 and 90.")
                elif temp == "2":
                    x_column = "bmi"
                    y_column = "glucose"
                    title = 'BMI vs. Glucose Levels'
                    print("Interpretation:")
                    print("- There are outliers as some entries of BMI.")
                    print("- Major BMI range is 25 to 40, and glucose range is 75 to 150.")
                elif temp == "3":
                    x_column = "insulin"
                    y_column = "age"
                    title = 'Insulin Levels vs. Age'
                    print("Interpretation:")
                    print("- There are entries from age 20 to 80 having insulin levels greater than 0.")
                elif temp == "4":
                    x_column = "skinthickness"
                    y_column = "bmi"
                    title = 'Skin Thickness vs. BMI'
                    print("Interpretation:")
                    print("- Skin thickness is in the range of 10 to 50.")
                    print("- BMI in the range from 15 to 45 with some outliers with nearly zero values.")
                elif temp == "5":
                    break

                create_scatter_plot(df[x_column], df[y_column], f'Scatter Plot: {title}', x_column, y_column)

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    elif choice == "3":
        print("Creating Bar plot...")
        feature = get_column_name()

        if feature in df.columns:
            x_data = df[feature]
            y_data = x_data.value_counts().values
            x_labels = x_data.value_counts().index
            create_bar_plot(x_labels, y_data, f'Bar Plot for {feature.capitalize()}', feature)
            
            if feature == 'age':
                print("Interpretation:")
                print("- Most of the dataset entries lie between the age of 20 to 40.")
            elif feature == 'bmi':
                print("Interpretation:")
                print("- BMI mode is between 35-40, and BMI is in the range of 10 to 67.")
            elif feature == 'bloodpressure':
                print("Interpretation:")
                print("- Blood pressure is in the range of 30 to 110.")
        else:
            print("Invalid feature name. Please enter a valid column name.")

    elif choice == "4":
        print("Creating Density plot...")
        feature = get_column_name()

        if feature in df.columns:
            create_density_plot(df[feature], f'Density Plot for {feature.capitalize()}', feature)
            
            if feature == 'age':
                print("Interpretation:")
                print("- The majority of the dataset entries are between the age of 20 to 40.")
            elif feature == 'bmi':
                print("Interpretation:")
                print("- The BMI distribution is right-skewed, with a mode around 30-35.")
            elif feature == 'bloodpressure':
                print("Interpretation:")
                print("- Blood pressure distribution is fairly uniform, with a peak around 70-80.")
        else:
            print("Invalid feature name. Please enter a valid column name.")

    elif choice == "5":
        print("Creating Pie chart...")
        feature = get_column_name()

        if feature in df.columns:
            create_pie_chart(df[feature], f'Pie Chart for {feature.capitalize()}')
        else:
            print("Invalid feature name. Please enter a valid column name.")

    elif choice == "6":
        print("Creating Bubble plot...")
        x_feature = get_column_name()
        y_feature = get_column_name()
        size_feature = get_column_name()

        if x_feature in df.columns and y_feature in df.columns and size_feature in df.columns:
            create_bubble_plot(df[x_feature], df[y_feature], df[size_feature], f'Bubble Plot: {x_feature} vs {y_feature} (Size: {size_feature})', x_feature, y_feature, size_feature)
        else:
            print("Invalid feature name. Please enter valid column names.")

    elif choice == "7":
        print("Creating Heatmap...")
        print("Select heatmap type:")
        print("1. Correlation Heatmap")
        print("2. Custom Heatmap")
        heatmap_choice = input("Enter your choice: ")

        if heatmap_choice == "1":
            create_heatmap(df.corr(), "Correlation Heatmap")
            print("Interpretation:")
            print("- A positive correlation is seen between age and pregnancies.")
            print("- A positive correlation is observed between age and diabetes pedigree function.")
            print("- Other correlations are not strongly apparent.")
        elif heatmap_choice == "2":
            print("Custom Heatmap")
            feature1 = get_column_name()
            feature2 = get_column_name()
            if feature1 in df.columns and feature2 in df.columns:
                create_heatmap(pd.crosstab(df[feature1], df[feature2]), f'Heatmap: {feature1} vs {feature2}')
            else:
                print("Invalid feature names. Please enter valid column names.")

    elif choice == "8":
        print("Creating Treemap...")
        feature = get_column_name()

        if feature in df.columns:
            create_treemap(df[feature], f'Treemap for {feature.capitalize()}')
        else:
            print("Invalid feature name. Please enter a valid column name.")

    elif choice == "9":
        print("Creating Correlation Matrices...")
        create_correlation_matrices(df)
        print("Interpretation:")
        print("- The correlation matrix provides insights into the relationships between different features.")
        print("- A strong positive correlation is observed between age and pregnancies.")
        print("- A positive correlation is observed between age and diabetes pedigree function.")
        print("- Other correlations are not strongly apparent.")

    elif choice == "10":
        print("Creating Dendrogram...")
        create_dendrogram(df)
        print("Interpretation:")
        print("- The dendrogram provides a hierarchical clustering of the dataset.")
        print("- Similar entries are grouped together based on their similarity.")
        print("- In this dendrogram, entries with similar features are clustered together.")

    elif choice == "11":
        print("Exiting the program")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 11")



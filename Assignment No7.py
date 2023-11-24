import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import skew
import seaborn as sns
from warnings import filterwarnings

filterwarnings('ignore')

# Function to create a dataset
def create_dataset():
    Student_Id = np.arange(1, 101, 1)
    Marks = np.random.randint(1, 200, 100)
    df = pd.DataFrame({"StudentId": Student_Id, "Marks": Marks})
    return df

# Function to calculate skewness
def calculate_skewness(array):
    return (3 * (array.mean() - array.median()) / array.std())

# Function to plot statistics
def plot_statistics(data, ax, title):
    data_series = pd.Series(data)  # Convert NumPy array to pandas Series
    mean_value = data_series.mean()
    median_value = data_series.median()
    mode_values = data_series.mode().values
    skewness_value = calculate_skewness(data_series)

    ax.axvline(mean_value, color='green', linestyle='dashed', linewidth=1, label=f'Mean: {mean_value:.2f}')
    ax.axvline(median_value, color='red', linestyle='dashed', linewidth=1, label=f'Median: {median_value:.2f}')
    for mode in mode_values:
        ax.axvline(mode, color='orange', linestyle='dashed', linewidth=1, label=f'Mode: {mode:.2f}')

    skewness_label = "Positive (Right-skewed)" if skewness_value > 0 else "Negative (Left-skewed)"
    ax.set_xlabel(f'Skewness: {skewness_value:.2f} - {skewness_label}')
    ax.set_title(title)
    ax.legend()

# Main program loop
while True:
    print("\nMenu:")
    print("1. Create Dataset")
    print("2. Display Original and Transformed Distributions (Subplots)")
    print("3. Display Original Distribution (Single Plot)")
    print("4. Change Scale for Better Understanding")
    print("5. Convert Non-linear Relation to Linear")
    print("6. Decrease Skewness")
    print("7. Convert Distribution into Normal")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        df = create_dataset()
        print(df.head())
        print("Dataset created successfully.")

    elif choice == 2:
        if 'df' not in locals():
            print("Please create a dataset first (Option 1).")
        else:
            plt.figure(figsize=(12, 5))

            # Original Data (Left Subplot)
            plt.subplot(1, 2, 1)
            sns.distplot(df['Marks'], bins=25, hist=True, kde=True, color='green')
            plt.title('Original Marks Distribution')
            plt.xlabel('Marks')
            plt.ylabel('Density')
            plot_statistics(df['Marks'], plt.gca(), 'Original Marks Distribution')

            # Transformed Data (Right Subplot)
            df_transformed = np.sqrt(df['Marks'])  # Apply Square Root Transformation
            plt.subplot(1, 2, 2)
            sns.distplot(df_transformed, bins=25, hist=True, kde=True, color='skyblue')
            plt.title('Square Root Transformed Marks Distribution')
            plt.xlabel('Transformed Marks')
            plt.ylabel('Density')
            plt.tight_layout()
            plt.show()

    elif choice == 3:
        if 'df' not in locals():
            print("Please create a dataset first (Option 1).")
        else:
            plt.figure(figsize=(8, 6))
            # Original Data
            sns.distplot(df['Marks'], bins=25, hist=True, kde=True, color='green')
            plot_statistics(df['Marks'], plt.gca(), 'Original Marks Distribution')
            plt.tight_layout()
            plt.show()

    elif choice == 4:
        if 'df' not in locals():
            print("Please create a dataset first (Option 1).")
        else:
            plt.figure(figsize=(12, 5))

            # Original Data (Left Subplot)
            plt.subplot(1, 2, 1)
            sns.distplot(df['Marks'], bins=25, hist=True, kde=True, color='green')
            plot_statistics(df['Marks'], plt.gca(), 'Original Marks Distribution')

            # Scaled Data (Right Subplot)
            scale_factor = float(input("Enter the scale factor: "))
            df_scaled = df['Marks'] * scale_factor
            plt.subplot(1, 2, 2)
            sns.distplot(df_scaled, bins=25, hist=True, kde=True, color='purple')
            plot_statistics(df_scaled, plt.gca(), 'Scaled Marks Distribution')
            plt.tight_layout()
            plt.show()

    elif choice == 5:
        if 'df' not in locals():
            print("Please create a dataset first (Option 1).")
        else:
            plt.figure(figsize=(12, 5))

            # Original Data (Left Subplot)
            plt.subplot(1, 2, 1)
            sns.distplot(df['Marks'], bins=25, hist=True, kde=True, color='green')
            plot_statistics(df['Marks'], plt.gca(), 'Original Marks Distribution')

            # Log-Transformed Data (Right Subplot)
            df_log = np.log(df['Marks'])
            plt.subplot(1, 2, 2)
            sns.distplot(df_log, bins=25, hist=True, kde=True, color='orange')
            plot_statistics(df_log, plt.gca(), 'Log-Transformed Marks Distribution')
            plt.tight_layout()
            plt.show()

    elif choice == 6:
        if 'df' not in locals():
            print("Please create a dataset first (Option 1).")
        else:
            plt.figure(figsize=(12, 5))

            # Original Data (Left Subplot)
            plt.subplot(1, 2, 1)
            sns.distplot(df['Marks'], bins=25, hist=True, kde=True, color='green')
            plot_statistics(df['Marks'], plt.gca(), 'Original Marks Distribution')

            # Square Root Transformed Data (Right Subplot)
            df_sqrt = np.sqrt(df['Marks'])
            plt.subplot(1, 2, 2)
            sns.distplot(df_sqrt, bins=25, hist=True, kde=True, color='skyblue')
            plot_statistics(df_sqrt, plt.gca(), 'Square Root Transformed Marks Distribution')
            plt.tight_layout()
            plt.show()

    elif choice == 7:
        if 'df' not in locals():
            print("Please create a dataset first (Option 1).")
        else:
            plt.figure(figsize=(12, 5))

            # Original Data (Left Subplot)
            plt.subplot(1, 2, 1)
            sns.distplot(df['Marks'], bins=25, hist=True, kde=True, color='green')
            plot_statistics(df['Marks'], plt.gca(), 'Original Marks Distribution')

            # Normal Distribution (Right Subplot)
            original_mean = df['Marks'].mean()
            original_std = df['Marks'].std()
            normal_data = np.random.normal(original_mean, original_std, 100)
            plt.subplot(1, 2, 2)
            sns.distplot(normal_data, bins=25, hist=True, kde=True, color='purple')
            plt.tight_layout()
            plt.show()

    elif choice == 8:
        print("Exiting the program!")
        break

    else:
        print("Invalid choice. Please try again.")







import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, MaxAbsScaler

# Changing path
os.chdir("C:\\Users\\itsoh\\Downloads\\")

# Reading the CSV file
df = pd.read_csv('diabetes_unclean.csv')

while True:
    print("1. Search Duplicate Records")
    print("2. To drop all Null values in the original dataframe")
    print("3. Fill NULL values with a user-given value")
    print("4. Apply MinMax Transformation")
    print("5. Apply Standardization of given data")
    print("6. Apply Maximum Absolute Scaling")
    print("7. Exit")
    
    choice = int(input("Enter the choice number: "))

    if choice == 1:
        if df.duplicated().sum() == 0:
            print("No duplicate values!")
        else:
            print(df[df.duplicated()])

    elif choice == 2:
        df.dropna(inplace=True)
        print(df)

    elif choice == 3:
        fill_value = float(input("Enter the value to fill NULL values with: "))
        df.fillna(fill_value, inplace=True)
        for i in df.columns:
            if df[i].is_na()==True:
                df[i].fillna(df[i])         
        print(df)

    elif choice == 4:
        scaler = MinMaxScaler()
        columns_to_scale = ['AGE', 'Urea', 'Cr', 'HbA1c', 'Chol', 'TG', 'HDL', 'LDL', 'VLDL', 'BMI']
        df1 = df[columns_to_scale]
        req_col = []
        for i in df.columns:
            if df[i].dtype!='O':
                req_col.append(i)
        req_col
        scaled_df = pd.DataFrame(scaler.fit_transform(df1), columns=columns_to_scale)
        print(scaled_df)

    elif choice == 5:
        scaler = StandardScaler()
        columns_to_scale = ['AGE', 'Urea', 'Cr', 'HbA1c', 'Chol', 'TG', 'HDL', 'LDL', 'VLDL', 'BMI']
        df1 = df[columns_to_scale]
        scaled_df = pd.DataFrame(scaler.fit_transform(df1), columns=columns_to_scale)
        print(scaled_df)

    elif choice == 6:
        scaler = MaxAbsScaler()
        columns_to_scale = ['AGE', 'Urea', 'Cr', 'HbA1c', 'Chol', 'TG', 'HDL', 'LDL', 'VLDL', 'BMI']
        df1 = df[columns_to_scale]
        scaled_df = pd.DataFrame(scaler.fit_transform(df1), columns=columns_to_scale)
        print(scaled_df)

    elif choice == 7:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option!")

"""
OUTPUT :
1. Search Duplicate Records
2. To drop all Null values in the original dataframe
3. Fill NULL values with a user-given value
4. Apply MinMax Transformation
5. Apply Standardization of given data
6. Apply Maximum Absolute Scaling
7. Exit
Enter the choice number: 1
No duplicate values!
1. Search Duplicate Records
2. To drop all Null values in the original dataframe
3. Fill NULL values with a user-given value
4. Apply MinMax Transformation
5. Apply Standardization of given data
6. Apply Maximum Absolute Scaling
7. Exit
Enter the choice number: 2
       ID  No_Pation Gender   AGE  Urea     Cr  HbA1c  Chol   TG  HDL  LDL  \
0     502      17975      F  50.0   4.7   46.0    4.9   4.2  0.9  2.4  1.4   
1     735      34221      M  26.0   4.5   62.0    4.9   3.7  1.4  1.1  2.1   
2     420      47975      F  50.0   4.7   46.0    4.9   4.2  0.9  2.4  1.4   
3     680      87656      F  50.0   4.7   46.0    4.9   4.2  0.9  2.4  1.4   
4     504      34223      M  33.0   7.1   46.0    4.9   4.9  1.0  0.8  2.0   
...   ...        ...    ...   ...   ...    ...    ...   ...  ...  ...  ...   
1000  185     454316      M  64.0   8.8  106.0    8.5   5.9  2.1  1.2  4.0   
1002  188     454316      F  75.0  10.3  113.0    8.6   4.2  1.6  0.9  2.6   
1003  189     454316      M  58.0   4.0   55.0    7.9   4.9  2.0  1.2  1.4   
1007  194     454316      F  57.0   4.1   70.0    9.3   5.3  3.3  1.0  1.4   
1008  195       4543      f  55.0   4.1   34.0   13.9   5.4  1.6  1.6  3.1   

      VLDL   BMI CLASS  
0      0.5  24.0     N  
1      0.6  23.0     N  
2      0.5  24.0     N  
3      0.5  24.0     N  
4      0.4  21.0     N  
...    ...   ...   ...  
1000   1.2  32.0    Y   
1002   0.7  32.0    Y   
1003   1.1  35.0    Y   
1007   1.3  29.0    Y   
1008   0.7  33.0    Y   

[994 rows x 14 columns]
1. Search Duplicate Records
2. To drop all Null values in the original dataframe
3. Fill NULL values with a user-given value
4. Apply MinMax Transformation
5. Apply Standardization of given data
6. Apply Maximum Absolute Scaling
7. Exit
Enter the choice number: 3
Enter the value to fill NULL values with: 4
       ID  No_Pation Gender   AGE  Urea     Cr  HbA1c  Chol   TG  HDL  LDL  \
0     502      17975      F  50.0   4.7   46.0    4.9   4.2  0.9  2.4  1.4   
1     735      34221      M  26.0   4.5   62.0    4.9   3.7  1.4  1.1  2.1   
2     420      47975      F  50.0   4.7   46.0    4.9   4.2  0.9  2.4  1.4   
3     680      87656      F  50.0   4.7   46.0    4.9   4.2  0.9  2.4  1.4   
4     504      34223      M  33.0   7.1   46.0    4.9   4.9  1.0  0.8  2.0   
...   ...        ...    ...   ...   ...    ...    ...   ...  ...  ...  ...   
1000  185     454316      M  64.0   8.8  106.0    8.5   5.9  2.1  1.2  4.0   
1002  188     454316      F  75.0  10.3  113.0    8.6   4.2  1.6  0.9  2.6   
1003  189     454316      M  58.0   4.0   55.0    7.9   4.9  2.0  1.2  1.4   
1007  194     454316      F  57.0   4.1   70.0    9.3   5.3  3.3  1.0  1.4   
1008  195       4543      f  55.0   4.1   34.0   13.9   5.4  1.6  1.6  3.1   

      VLDL   BMI CLASS  
0      0.5  24.0     N  
1      0.6  23.0     N  
2      0.5  24.0     N  
3      0.5  24.0     N  
4      0.4  21.0     N  
...    ...   ...   ...  
1000   1.2  32.0    Y   
1002   0.7  32.0    Y   
1003   1.1  35.0    Y   
1007   1.3  29.0    Y   
1008   0.7  33.0    Y   

[994 rows x 14 columns]
1. Search Duplicate Records
2. To drop all Null values in the original dataframe
3. Fill NULL values with a user-given value
4. Apply MinMax Transformation
5. Apply Standardization of given data
6. Apply Maximum Absolute Scaling
7. Exit
Enter the choice number: 5
          AGE      Urea        Cr     HbA1c      Chol        TG       HDL  \
0   -0.411899 -0.145760 -0.378677 -1.332538 -0.507847 -1.032054  1.803674   
1   -3.153598 -0.213631 -0.112266 -1.332538 -0.892767 -0.674564 -0.160433   
2   -0.411899 -0.145760 -0.378677 -1.332538 -0.507847 -1.032054  1.803674   
3   -0.411899 -0.145760 -0.378677 -1.332538 -0.507847 -1.032054  1.803674   
4   -2.353936  0.668693 -0.378677 -1.332538  0.031041 -0.960556 -0.613688   
..        ...       ...       ...       ...       ...       ...       ...   
989  1.187426  1.245598  0.620363  0.084060  0.800881 -0.174077 -0.009348   
990  2.444038  1.754631  0.736917  0.123410 -0.507847 -0.531567 -0.462603   
991  0.502001 -0.383309 -0.228821 -0.152040  0.031041 -0.245575 -0.009348   
992  0.387764 -0.349373  0.020939  0.398860  0.338977  0.683900 -0.311518   
993  0.159289 -0.349373 -0.578485  2.208958  0.415961 -0.531567  0.594993   

          LDL      VLDL       BMI  
0   -1.084782 -0.370087 -1.128439  
1   -0.457300 -0.342856 -1.329995  
2   -1.084782 -0.370087 -1.128439  
3   -1.084782 -0.370087 -1.128439  
4   -0.546940 -0.397318 -1.733109  
..        ...       ...       ...  
989  1.245863 -0.179468  0.484016  
990 -0.009099 -0.315624  0.484016  
991 -1.084782 -0.206700  1.088687  
992 -1.084782 -0.152237 -0.120654  
993  0.439102 -0.315624  0.685573  

[994 rows x 10 columns]
1. Search Duplicate Records
2. To drop all Null values in the original dataframe
3. Fill NULL values with a user-given value
4. Apply MinMax Transformation
5. Apply Standardization of given data
6. Apply Maximum Absolute Scaling
7. Exit
Enter the choice number: 6
          AGE      Urea       Cr    HbA1c      Chol        TG       HDL  \
0    0.632911  0.120823  0.05750  0.30625  0.407767  0.065217  0.242424   
1    0.329114  0.115681  0.07750  0.30625  0.359223  0.101449  0.111111   
2    0.632911  0.120823  0.05750  0.30625  0.407767  0.065217  0.242424   
3    0.632911  0.120823  0.05750  0.30625  0.407767  0.065217  0.242424   
4    0.417722  0.182519  0.05750  0.30625  0.475728  0.072464  0.080808   
..        ...       ...      ...      ...       ...       ...       ...   
989  0.810127  0.226221  0.13250  0.53125  0.572816  0.152174  0.121212   
990  0.949367  0.264781  0.14125  0.53750  0.407767  0.115942  0.090909   
991  0.734177  0.102828  0.06875  0.49375  0.475728  0.144928  0.121212   
992  0.721519  0.105398  0.08750  0.58125  0.514563  0.239130  0.101010   
993  0.696203  0.105398  0.04250  0.86875  0.524272  0.115942  0.161616   

          LDL      VLDL       BMI  
0    0.141414  0.014286  0.502618  
1    0.212121  0.017143  0.481675  
2    0.141414  0.014286  0.502618  
3    0.141414  0.014286  0.502618  
4    0.202020  0.011429  0.439791  
..        ...       ...       ...  
989  0.404040  0.034286  0.670157  
990  0.262626  0.020000  0.670157  
991  0.141414  0.031429  0.732984  
992  0.141414  0.037143  0.607330  
993  0.313131  0.020000  0.691099  

[994 rows x 10 columns]
1. Search Duplicate Records
2. To drop all Null values in the original dataframe
3. Fill NULL values with a user-given value
4. Apply MinMax Transformation
5. Apply Standardization of given data
6. Apply Maximum Absolute Scaling
7. Exit
Enter the choice number: 7
Exiting the program.

"""



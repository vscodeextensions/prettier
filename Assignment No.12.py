import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Change the working directory
os.chdir("C:")

# Load the dataset
train_df = pd.read_csv("Train.csv")

# Define features and target variable
features = ['Item_Weight', 'Item_Visibility', 'Item_MRP', 'Outlet_Establishment_Year']
target = 'Item_Outlet_Sales'

# Drop rows with missing values in selected features
train_df.dropna(subset=features, inplace=True)

# Apply label encoding for categorical columns
label_encoders = {}
for col in train_df.columns:
    if train_df[col].dtype == 'object':
        label_encoders[col] = LabelEncoder()
        train_df[col] = label_encoders[col].fit_transform(train_df[col].astype(str))

# Linear Regression
X_train, X_test, y_train, y_test = train_test_split(train_df[features], train_df[target], test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error (Linear Regression):", mse)

# Calculate R-squared
r_squared = r2_score(y_test, predictions)
print("R-squared (Linear Regression):", r_squared)

# Print coefficients with up to 3 decimals
coefficients = model.coef_
coefficients_rounded = [round(coef, 3) for coef in coefficients]
print("Coefficients (up to 3 decimals):", coefficients_rounded)
"""
 OUTPUT : 
 Mean Squared Error (Linear Regression): 1436636.7252664343
R-squared (Linear Regression): 0.40903465340493195
Coefficients (up to 3 decimals): [-2.835, -2526.669, 15.107, 3.687]

"""


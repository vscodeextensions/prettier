import os
os.chdir("C:")

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# Load the Pima Indians Diabetes dataset
df = pd.read_csv('diabetes.csv')

# Split the dataset into training and test data
X_train, X_test, y_train, y_test = train_test_split(df.drop(['Outcome', 'BloodPressure'], axis=1), df['Outcome'], test_size=0.25, random_state=42)

# Train the Naive Bayes classifier on the training data
clf = GaussianNB()
clf.fit(X_train, y_train)

# Make predictions on the test data using the trained classifier
y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = np.mean(y_pred == y_test)

# Calculate true positives, false positives, true negatives, and false negatives
true_positives = np.sum((y_pred == 1) & (y_test == 1))
false_positives = np.sum((y_pred == 1) & (y_test == 0))
true_negatives = np.sum((y_pred == 0) & (y_test == 0))
false_negatives = np.sum((y_pred == 0) & (y_test == 1))

# Calculate precision, recall, and F1 score
precision = true_positives / (true_positives + false_positives)
recall = true_positives / (true_positives + false_negatives)
fl_score = 2 * (precision * recall) / (precision + recall)

# Print metrics
print('Accuracy: {:.2f}'.format(accuracy))
print('Precision: {:.2f}'.format(precision))
print('Recall: {:.2f}'.format(recall))
print('F1 Score: {:.2f}'.format(fl_score))

# Output the correlation matrix
corr_matrix = df.corr()
print("Correlation Matrix:")
print(corr_matrix)

"""
OUTPUT :
Accuracy: 0.75
Precision: 0.66
Recall: 0.62
F1 Score: 0.64
Correlation Matrix:
This matrix shows the correlation between different features in the dataset.
Each cell in the matrix represents the correlation coefficient between two features.
The values range from -1 to 1, where 1 indicates a strong positive correlation, -1 indicates a strong negative correlation, and 0 indicates no correlation.

The interpretation of the correlation matrix is specific to the dataset and the context of the features.
 
"""


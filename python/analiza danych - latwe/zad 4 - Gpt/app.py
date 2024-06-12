# Importing necessary libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import time

# Generating some sample data
X_train = np.array([[1], [2], [3], [4], [5]])  # Features
y_train = np.array([2, 4, 5, 4, 5])  # Target values

# Creating and training the linear regression model
start_time = time.time()  # Start time
model = LinearRegression()
model.fit(X_train, y_train)
end_time = time.time()  # End time

# Calculating the compile time
compile_time = end_time - start_time

# Predicting values for new data
X_new = np.array([[6], [7]])  # New data
y_pred = model.predict(X_new)

print("Predictions for new data:")
for i in range(len(X_new)):
    print(f"X = {X_new[i][0]}, Predicted y = {y_pred[i]}")

print(f"Compile time: {compile_time} seconds")

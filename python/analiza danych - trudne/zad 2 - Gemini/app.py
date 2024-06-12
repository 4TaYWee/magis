import numpy as np
from tensorflow import keras
from tensorflow.keras.layers import LSTM, Dense


def create_dataset(data, look_back=1):
  """
  Creates a dataset for LSTM training.

  Args:
      data: A numpy array of time series data.
      look_back: The number of previous time steps to consider as input.

  Returns:
      A tuple of (X_train, y_train), where X_train is a 3D array of training
      samples and y_train is a 2D array of target values.
  """
  X, y = [], []
  for i in range(look_back, len(data)):
    X.append(data[i-look_back:i])
    y.append(data[i])
  return np.array(X), np.array(y)


# Sample time series data
data = np.random.rand(100)

# Split data into train and test sets
train_size = int(len(data) * 0.8)
train, test = data[:train_size], data[train_size:]

# Define look_back (number of previous steps to consider)
look_back = 1

# Prepare training and testing data
X_train, y_train = create_dataset(train, look_back)
X_test, y_test = create_dataset(test, look_back)

# Reshape input data for LSTM
X_train = np.expand_dims(X_train, axis=0)
X_test = np.expand_dims(X_test, axis=0)

# Build the LSTM model
model = keras.Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(look_back, 1)))  # 50 units in LSTM layer
model.add(LSTM(50))
model.add(Dense(1))  # Output layer with 1 unit for single value prediction

model.compile(loss="mse", optimizer="adam")  # Mean squared error loss and Adam optimizer

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

# Make predictions on test data
predictions = model.predict(X_test)

# Evaluate model performance (optional)
# ...

# Print first few predictions
print(predictions[:5])

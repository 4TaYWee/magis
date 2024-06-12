import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
import time

# Generate some sample data (time series)
def generate_data(n_samples, time_steps):
    X = np.arange(n_samples)
    y = np.sin(X)
    X = X.reshape((n_samples, time_steps, 1))
    return X, y

# Define LSTM model
def create_lstm_model(time_steps):
    model = Sequential()
    model.add(LSTM(units=50, input_shape=(time_steps, 1)))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Generate sample data
n_samples = 1000
time_steps = 10
X, y = generate_data(n_samples, time_steps)

# Timing compilation
start_compilation = time.time()

# Create and compile LSTM model
model = create_lstm_model(time_steps)

end_compilation = time.time()

# Timing training
start_training = time.time()

# Train LSTM model
model.fit(X, y, epochs=10, batch_size=32)

end_training = time.time()

# Make predictions
test_input = np.array([[i+j for j in range(time_steps)] for i in range(n_samples)])
test_input = np.reshape(test_input, (n_samples, time_steps, 1))

# Timing prediction
start_prediction = time.time()

predictions = model.predict(test_input)

end_prediction = time.time()

# Print sample predictions
print("First 10 predictions:")
print(predictions[:10])

# Print times
print("Compilation time: {:.2f} seconds".format(end_compilation - start_compilation))
print("Training time: {:.2f} seconds".format(end_training - start_training))
print("Prediction time: {:.2f} seconds".format(end_prediction - start_prediction))

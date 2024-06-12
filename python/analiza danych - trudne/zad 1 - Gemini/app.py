import time
from tensorflow import keras

# Define the model
model = keras.Sequential([
  keras.layers.Flatten(input_shape=(28, 28)),  # Flatten 28x28 images
  keras.layers.Dense(128, activation="relu"),  # Dense layer with 128 neurons and ReLU activation
  keras.layers.Dense(10, activation="softmax")  # Output layer with 10 neurons (for 10 digits) and softmax activation
])

# Compile the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Load the MNIST dataset (modify for your dataset)
(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()

# Preprocess the data (normalize pixel values)
train_images = train_images.reshape(-1, 28, 28, 1)  # Reshape for convolutional layers (if applicable)
train_images = train_images.astype("float32") / 255.0
test_images = test_images.reshape(-1, 28, 28, 1)
test_images = test_images.astype("float32") / 255.0

# Start time before training
start_time = time.perf_counter()

# Train the model
model.fit(train_images, train_labels, epochs=5)

# End time after training
end_time = time.perf_counter()

# Calculate total training time
total_time = end_time - start_time
print(f"Training time: {total_time:.2f} seconds")

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Test accuracy:", test_acc)

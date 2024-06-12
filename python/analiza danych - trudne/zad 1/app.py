import time
import tensorflow as tf
from tensorflow.keras import layers, models

start_compilation_time = time.time()

# Load the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build the neural network model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Flatten the input image
    layers.Dense(128, activation='relu'),  # Hidden layer with 128 neurons
    layers.Dropout(0.2),                    # Dropout layer to prevent overfitting
    layers.Dense(10, activation='softmax')  # Output layer with 10 neurons for 10 classes
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

end_compilation_time = time.time()

# Train the model
start_execution_time = time.time()
model.fit(x_train, y_train, epochs=5)
end_execution_time = time.time()

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)

print("Compilation Time:", end_compilation_time - start_compilation_time, "seconds")
print("Execution Time:", end_execution_time - start_execution_time, "seconds")
print("Test accuracy:", test_acc)

import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

# Pobierz dane CIFAR-10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Skalowanie danych
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Konwersja etykiet na format wejściowy dla sieci neuronowej
y_train = tf.keras.utils.to_categorical(y_train)
y_test = tf.keras.utils.to_categorical(y_test)

# Definicja modelu sieci neuronowej
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D((2, 2)),
    Dropout(0.25),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Dropout(0.25),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

# Kompilacja modelu
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Trening modelu
model.fit(x_train, y_train, epochs=2, batch_size=32)

# Ewaluacja modelu
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Dokładność:', test_acc)

# Klasyfikacja nowych obrazów
nowy_obraz = tf.keras.preprocessing.image.load_img("F:\samolot.jpg", target_size=(32, 32))
nowy_obraz = tf.keras.preprocessing.image.img_to_array(nowy_obraz)
nowy_obraz = nowy_obraz.reshape(1, 32, 32, 3)
predykcja = model.predict(nowy_obraz)
print('Klasyfikacja:', predykcja)

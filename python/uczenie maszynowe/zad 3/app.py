# Importowanie niezbędnych bibliotek
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Przykładowe dane - zmienna niezależna X i zmienna zależna y
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Podział danych na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicjalizacja modelu regresji liniowej
model = LinearRegression()

# Dopasowanie modelu do danych treningowych
model.fit(X_train, y_train)

# Przewidywanie wartości dla danych testowych
y_pred = model.predict(X_test)

# Ocena modelu za pomocą metryki MSE (Mean Squared Error)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Wizualizacja regresji
import matplotlib.pyplot as plt

plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.title('Regresja liniowa')
plt.xlabel('X')
plt.ylabel('y')
plt.show()

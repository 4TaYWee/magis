import numpy as np  # Import the numpy library

from sklearn.linear_model import LinearRegression

# Przygotowanie danych
X = [[100], [150], [200]]  # Powierzchnia domu
y = [50000, 65000, 80000]  # Cena domu

# Utworzenie i dopasowanie modelu regresji liniowej
model = LinearRegression()
model.fit(X, y)

# Przewidywanie ceny nowego domu o powierzchni 180 m2
nowa_powierzchnia = np.array([180])  # Convert to a numpy array
nowa_powierzchnia = nowa_powierzchnia.reshape(1, -1)  # Reshape to 2D array with 1 row

# Make prediction
przewidywana_cena = model.predict(nowa_powierzchnia)
print(f"Przewidywana cena domu o powierzchni 180 m2: {przewidywana_cena[0]:.2f}")

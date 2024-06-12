import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Przykładowe dane
X = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
])

y = np.array([0, 1, 1, 2])

# Podział danych na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Wybór wartości K
K = 1

# Klasyfikacja punktów testowych
def classify(point, X_train, y_train, K):
  # Oblicz odległości od punktu do wszystkich punktów w zbiorze treningowym
  distances = np.linalg.norm(X_train - point, axis=1)

  # Znajdź K najbliższych punktów
  nearest_indices = distances.argsort()[:K]

  # Pobierz etykiety najbliższych punktów
  nearest_labels = y_train[nearest_indices]

  # Wybierz najczęściej występującą etykietę
  mode = np.bincount(nearest_labels).argmax()

  return mode

# Klasyfikacja wszystkich punktów testowych
y_pred = np.array([classify(point, X_train, y_train, K) for point in X_test])

# Oblicz dokładność
accuracy = accuracy_score(y_test, y_pred)

print("Dokładność:", accuracy)

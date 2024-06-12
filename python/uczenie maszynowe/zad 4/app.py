# Importowanie niezbędnych bibliotek
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Wczytanie danych (przykładowy zbiór danych IRIS)
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Podział danych na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standaryzacja danych
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Dostosowanie modelu SVM
svm_classifier = SVC(kernel='linear', random_state=42)
svm_classifier.fit(X_train, y_train)

# Predykcja na zbiorze testowym
y_pred = svm_classifier.predict(X_test)

# Ocena skuteczności modelu
accuracy = accuracy_score(y_test, y_pred)
print("Skuteczność modelu SVM:", accuracy)

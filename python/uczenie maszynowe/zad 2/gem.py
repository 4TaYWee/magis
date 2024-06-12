from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz

# Load the Wine dataset
wine = load_wine()
X = wine.data
y = wine.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Build and train the decision tree
tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

# Predict wine types on the test set
y_pred = tree.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Visualize the decision tree (requires Graphviz)
export_graphviz(tree, out_file="wine_tree.dot", feature_names=wine.feature_names)
print("Decision tree visualized in 'wine_tree.dot'. You need Graphviz to view it.")

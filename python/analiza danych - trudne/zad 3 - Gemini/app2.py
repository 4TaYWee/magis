import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Define functions for text preprocessing (optional, customize further)
def preprocess_text(text):
  text = text.lower()  # Lowercase
  # Remove punctuation
  text = "".join([char for char in text if char.isalnum() or char == " "])
  # Remove stopwords (optional)
  # from nltk.corpus import stopwords
  # stop = stopwords.words('english')
  # text = " ".join([word for word in text.split() if word not in stop])
  return text

# Load dataset
data = pd.read_csv("Test.csv")  # Replace with your data file path

# Assuming sentiment label is in "label" column
text = data["text"]
sentiment = data["label"]  # Assuming sentiment is labeled

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(text, sentiment, test_size=0.2, random_state=42)

# Preprocess text data
X_train = X_train.apply(preprocess_text)
X_test = X_test.apply(preprocess_text)

# Feature vectorization
vectorizer = TfidfVectorizer()
X_train_features = vectorizer.fit_transform(X_train)
X_test_features = vectorizer.transform(X_test)

# Build sentiment classification model
model = LogisticRegression(solver='lbfgs')
model.fit(X_train_features, y_train)

# Evaluate model performance
y_pred = model.predict(X_test_features)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred))

# Test on new text (optional)
new_text = "This movie was absolutely fantastic!"
new_text_features = vectorizer.transform([preprocess_text(new_text)])
prediction = model.predict(new_text_features)[0]
print("New text sentiment:", prediction)

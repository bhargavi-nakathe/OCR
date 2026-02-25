import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
with open("data.json", "r") as f:
    data = json.load(f)

texts = [item["text"] for item in data]
labels = [item["label"] for item in data]

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

import joblib
import numpy as np

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def classify_receipt(text):
    X_input = vectorizer.transform([text])
    probs = model.predict_proba(X_input)
    prediction = model.predict(X_input)
    confidence = np.max(probs)
    return prediction[0], confidence

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
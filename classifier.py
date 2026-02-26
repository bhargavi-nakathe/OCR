import joblib
import numpy as np

# Load trained model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def classify_receipt(text):
    X_input = vectorizer.transform([text])
    probs = model.predict_proba(X_input)
    prediction = model.predict(X_input)
    confidence = np.max(probs)
    return prediction[0], float(confidence)
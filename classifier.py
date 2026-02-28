import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def classify_receipt(text):

    if not isinstance(text, str):
        text = str(text)

    text = text.lower()

    X_input = vectorizer.transform([text])

    prediction = model.predict(X_input)[0]
    probability = model.predict_proba(X_input).max()

    return prediction, round(probability * 100, 2)
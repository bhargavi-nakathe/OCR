import json
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
with open("data.json", "r") as f:
    data = json.load(f)

texts = [item["text"] for item in data]
labels = [item["Label"] for item in data]

# Vectorize
vectorizer = TfidfVectorizer(
    ngram_range=(1,2),
    stop_words='english',
    min_df=1
)
X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

# Save both
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved successfully.")
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# -----------------------------
# 1. Initial training data
# -----------------------------
texts = [
    "I love this movie",
    "This is terrible",
    "Amazing experience",
    "I hate this"
]

labels = [1, 0, 1, 0]  # 1 = positive, 0 = negative

# -----------------------------
# 2. Train model
# -----------------------------
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

# -----------------------------
# 3. Predict + ask user if unsure
# -----------------------------
def predict_with_question(text, threshold=0.65):
    X_new = vectorizer.transform([text])
    probabilities = model.predict_proba(X_new)[0]

    confidence = max(probabilities)
    prediction = model.predict(X_new)[0]

    print(f"Confidence: {confidence:.2f}")

    if confidence < threshold:
        print("🤔 I'm not sure about this one.")
        user_label = input("Is this positive (1) or negative (0)? ")
        return int(user_label), True
    else:
        return prediction, False

# -----------------------------
# 4. Run the system
# -----------------------------
while True:
    new_text = input("Enter a sentence: ")

    label, learned = predict_with_question(new_text)

    if learned:
        print("✅ Thanks! I learned from your answer.")
    else:
        print("Prediction:", "Positive" if label == 1 else "Negative")

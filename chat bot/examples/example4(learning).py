import json #data saving
import os #checks for if saved data is exists
from sklearn.feature_extraction.text import TfidfVectorizer #convert text to number
from sklearn.linear_model import LogisticRegression #this is for the confidence score for decide to ask or not

DATA_FILE = "training_data.json" # permanent memory file
CONFIDENCE_THRESHOLD = 0.65 #the value for asking question to user (if the confidence below 65%(0.65) ask question)

# ---------------------------------
# 1. Load or initialize data
# ---------------------------------
if os.path.exists(DATA_FILE): #check for if the saved data exists and load
    with open(DATA_FILE, "r") as f:
        data = json.load(f) #load
        texts = data["texts"]
        labels = data["labels"]
else:
    # default value
    texts = [
        "I love this movie",
        "This is terrible",
        "Amazing experience",
        "I hate this"
    ]
    labels = [1, 0, 1, 0]

# ---------------------------------
# 2. Train model
# ---------------------------------
vectorizer = TfidfVectorizer() 
X = vectorizer.fit_transform(texts) #transfers string to intiger

model = LogisticRegression() 
model.fit(X, labels) #learn the values(logic)

# ---------------------------------
# 3. Prediction + questioning
# ---------------------------------
def predict_with_question(text): #this function calculates the confidence and decides to ask or not(main part of self learing)
    X_new = vectorizer.transform([text]) #transfers 'text' into intiger
    print(f"X_new: {X_new}")
    probs = model.predict_proba(X_new)[0] #calculate the confidence
    print(f"probs: {probs}")
    confidence = max(probs)
    prediction = model.predict(X_new)[0]

    print(f"Confidence: {confidence:.2f}")

    if confidence < CONFIDENCE_THRESHOLD:
        print("I'm not sure.")
        while True:
            answer = input("Is this positive (1) or negative (0)? ")
            if answer in ("0", "1"):
                return int(answer), True
            print("Please enter 0 or 1.")
    else:
        return prediction, False

# ---------------------------------
# 4. Main loop
# ---------------------------------
while True:
    user_input = input("\nEnter a sentence (or type 'quit'): ")
    if user_input.lower() == "quit":
        break

    label, learned = predict_with_question(user_input)

    if learned:
        # Store new knowledge
        texts.append(user_input)
        labels.append(label)

        # Retrain model
        X = vectorizer.fit_transform(texts)
        model.fit(X, labels)

        # Save to disk
        with open(DATA_FILE, "w") as f:
            json.dump({"texts": texts, "labels": labels}, f)

        print("✅ Learned and saved.")
    else:
        print("Prediction:", "Positive" if label == 1 else "Negative")

print("\n👋 Goodbye! Knowledge saved.")

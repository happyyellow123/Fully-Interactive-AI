from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer

# Training data
x = ["Hi", "Bye"] #user answer
y = ["Hello", "Bye"] #machine answer

# Convert text to numbers
vectorizer = CountVectorizer()
x_vec = vectorizer.fit_transform(x) # convert string into intiger(the model[DesisionTreeClassifier] only understands intigers)

# Train model
model = DecisionTreeClassifier()
model.fit(x_vec, y) # teaches the machine

# Predict
while True:
    pe = input("Enter a word: ")
    pe_vec = vectorizer.transform([pe]) # convert string into intiger(the model[DesisionTreeClassifier] only understands intigers)
    answer = model.predict(pe_vec) # making it decide a answer

    print(answer[0]) #this is for print the only one answer(predict only returns list/array)

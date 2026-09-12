# py -m pip install scikit-learn
from sklearn.tree import DecisionTreeClassifier

# Sample data: [height, weight] -> "label"
X = [[150, 50], [160, 60], [170, 70], [180, 80]]  # features
y = ["short", "medium", "tall", "very tall"]       # labels

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Make predictions
print(model.predict([[165, 65]]))  # predicts "medium"

# py -m pip install scikit-learn
from sklearn.tree import DecisionTreeClassifier
x = ["Hi", "Bye"]
y = ["Hello", "Bye"]
model = DecisionTreeClassifier()
model.fit(x,y)
pe = input("")
answer = model.predict([pe])
print(answer)
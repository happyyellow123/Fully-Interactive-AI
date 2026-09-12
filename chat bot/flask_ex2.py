from flask import Flask, render_template, request
import time
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/input')
def input():
    return render_template('input.html')

@app.route("/send", methods=["POST"])
def receive():
    message = request.form["message"]
    print(message)  # prints in terminal
    if message.lower().strip() == "hi":
        return render_template('hello.html')
    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)
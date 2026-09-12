# py -m pip install flask
# py -c "import flask"
# py flask_ex.py
from flask import Flask

app = Flask(__name__) #define the flask app as "app"

@app.route("/") #when someone visit the URL(/ is the base), run the code below
def home():
    return "Hello, world!" #can be html
    # return "<h1>Hello!</h1>"
if __name__ == "__main__": #When this file is run directly by Python run the code below
    app.run(host="0.0.0.0") #start the flask server, this code SHOULD be at the LAST line

# flask calls every functions as it opens
# --You never call home() yourself because Flask is "event-driven". The function runs when a web request happens, not when Python reaches that line.
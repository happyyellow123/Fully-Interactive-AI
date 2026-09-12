from flask import Flask, render_template, request
import ollama
import json
import os
HISTORY = []
sfile = "chat_history_for_AI.json"
MODEL_NAME = "phi3:latest"
if os.path.exists(sfile):
    with open(sfile, "r") as f:
        HISTORY = json.load(f)
web = Flask(__name__)

@web.route("/")
def homepage():
    return render_template('homepage.html')

@web.route("/send", methods=["POST"])
def receive_message():
    message = request.form["message"]
    print(message)
    usermessage = {
        "role" : "user",
        "content" : message
    }
    HISTORY.append(usermessage)
    airesponse = ollama.chat(model=MODEL_NAME, messages=HISTORY)
    botmessagecontent = airesponse.message.content
    print(f"ollama: {botmessagecontent}")
    botmessage = {
        "role" : "assistant",
        "content" : botmessagecontent
    }
    HISTORY.append(botmessage)
    with open(sfile, "w") as f:
        json.dump(HISTORY, f, indent=2)
    return render_template('homepage.html', userm=f"User: {message}", mback=f"Ollama: {botmessagecontent}")
if __name__ == "__main__":
    web.run(host="0.0.0.0")

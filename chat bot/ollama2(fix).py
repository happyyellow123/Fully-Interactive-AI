# py .\chat_bot.py
import ollama
import json
# def savedata(x):
#     with open(f"{x}.json", "w") as saveddata:
#         json.dump(x, saveddata, indent = len(value))
# def loaddata(x):
#     with open(f"{x}.json", "r") as saveddata:
#         value = json.load(saveddata)
HISTORY = []
MODEL_NAME = "phi3:latest"
username = input("what is your name?")

while True:
    userinput = input("You: ")
    if userinput.lower() == "exit" or userinput.lower() == "quit":
        print("exited chat")
        break
    usermessage = {
        "role" : username,
        "message" : userinput
    }
    HISTORY.append(userinput)
    airesponse = ollama.chat(model = MODEL_NAME, messages = HISTORY)
    botmessagecontent = airesponse.message.content
    print(f"ollama: {botmessagecontent}")
    botmessage = {
        "role" : "ollama",
        "message" : botmessagecontent
    }
    HISTORY.append(botmessage)
    
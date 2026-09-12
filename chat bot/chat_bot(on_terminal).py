# pip install ollama
# py .\chat_bot.py
import ollama

history = []
model = "phi3:latest" # the model name of ai

while True:
    prompt = input("You: ").strip() # user's input
    if prompt.lower() in ("exit", "quit"): # codes for exiting chat
        print("Have a nice day!")
        break

    message = { # this values have to be same except the *prompt* part
        "role" : "user",
        "content" : prompt
    }

    history.append(message) # add the role(user) and the content(user's input) in the history
    response = ollama.chat(model=model, messages=history) # call ai, check for model, and give it the history(response is the answer of ai)
    bot_message_content = response.message.content # answer of ai
    print(f"Bot: {bot_message_content}")
    bot_message = {
        "role" : "assistant",
        "content" : bot_message_content
    }
    history.append(bot_message) # adding the answer of ai to the history

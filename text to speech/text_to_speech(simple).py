#py -m pip install pyttsx3
import pyttsx3

while True:
    text = input("Enter text (or 'exit'): ").strip()
    
    if text.lower() in ("exit", "quit"):
        break  
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    del engine
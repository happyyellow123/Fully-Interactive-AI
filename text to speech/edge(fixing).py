# voice options:https://github.com/rany2/edge-tts
import asyncio
import edge_tts
import tempfile
import os
global temp_name

TEXT = ""
operating_system = input("Enter your operating system ( 1:Windows    2:Linux ): ").strip().lower()

if operating_system == "1" or operating_system == "windows":
    def audio_play():
        os.system(f"start {temp_name}")

elif operating_system == "2" or operating_system == "linux":
    def audio_play():
        os.system(f"xdg-open {temp_name}")



while TEXT != "exit":

    TEXT = input("Enter text (or 'exit'): ").strip()

    try:
        # US English male
        VOICE = "en-US-GuyNeural"

        async def main():
            # Create temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
                temp_name = temp_audio.name

            # Generate speech
            communicate = edge_tts.Communicate(TEXT, VOICE)
            await communicate.save(temp_name)

            # Play audio
            audio_play()

        print("language: English")
        asyncio.run(main())

    except:
        # Korean male
        VOICE = "ko-KR-InJoonNeural"

        async def main():
            # Create temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
                temp_name = temp_audio.name

            # Generate speech
            communicate = edge_tts.Communicate(TEXT, VOICE)
            await communicate.save(temp_name)

            # Play audio (Windows)
            os.system(f"start {temp_name}")

            # Play audio (Linux)
            # os.system(f"xdg-open {temp_name}")
        print("language: Korean")
        asyncio.run(main())
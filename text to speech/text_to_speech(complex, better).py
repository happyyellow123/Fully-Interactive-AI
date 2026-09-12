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

    # Detect Korean and set voice model to Korean man voice
    if any('가' <= char <= '힣' for char in TEXT):
        VOICE = "ko-KR-InJoonNeural"
        print("language: Korean")
    # If there is no Korean, set voice model to US man voice
    else:
        VOICE = "en-US-GuyNeural"
        print("language: English")

    async def main():
        global temp_name

        # Create temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_name = temp_audio.name

        # Generate speech
        communicate = edge_tts.Communicate(TEXT, VOICE)
        await communicate.save(temp_name)

        # Play audio
        audio_play()

    asyncio.run(main())
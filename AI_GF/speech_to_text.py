# py -m pip install openai-whisper sounddevice
import whisper
import sounddevice as sd

# Configuration
SAMPLE_RATE = 16000  # Sets the audio sample rate to 16,000 Hz, which is the standard input format required by Whisper
DURATION = 5  # Recording duration in seconds

print("Loading Whisper model (this may take a moment on first run)...")

# Part that actually record the speech and request translation of speech to text
model = whisper.load_model("base")  # Downloads (on first run) and loads the "base" neural network model into memory for transcription
# Options: 'tiny', 'base', 'small', 'medium', 'large'
print(f"\nRecording for {DURATION} seconds... Speak now!")
# Record audio using sounddevice (no PyAudio required)
audio_data = sd.rec(
    int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype="float32"
)


sd.wait()  # Wait until the recording is finished
print("Recording complete. Processing transcript...")

# Flatten the audio array to 1D float32 array
audio_flattened = audio_data.flatten()

# Transcribe audio using Whisper
result = model.transcribe(audio_flattened, fp16=False) # save the translation result to the "result" variable

print("\n--- Result ---")
print("Text:", result["text"])
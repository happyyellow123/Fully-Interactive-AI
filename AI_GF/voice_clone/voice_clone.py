import soundfile as sf 
from pocket_tts import PocketTTS 
tts = PocketTTS() 
audio_data, sample_rate = tts.generate( 
	text="This is a test of local voice cloning running flawlessly on Python 3.14.",
	voice="path/to/english_yamada.wav" 
    )
sf.write("cloned_output_314.wav", audio_data, sample_rate)
print("Saved cloned voice to cloned_output_314.wav")
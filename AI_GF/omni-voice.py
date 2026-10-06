# py -m pip install omnivoice soundfile

from omnivoice import OmniVoice
import torch
import soundfile as sf

MODEL_NAME = "k2-fsa/OmniVoice"
REF_AUDIO = r"E:\AI_GF\english_yamada.wav"
OUTPUT_AUDIO = r"E:\AI_GF\voice_output\english_yamada_cloned.wav"

print("Loading model...")

model = OmniVoice.from_pretrained(
    MODEL_NAME,
    device_map="cuda:0",
    dtype=torch.float16
)

print("Creating voice clone prompt...")

voice_clone_prompt = model.create_voice_clone_prompt(
    ref_audio=REF_AUDIO,
    ref_text="You know what people saying these days, like, nobody want that kind of attitude. If you acting like that, everyone gonna be thinking you're just being stupid, you know what I mean?"
)

print("Generating...")

audio = model.generate(
    text="How are you today?",
    language="en",
    voice_clone_prompt=voice_clone_prompt,
    num_step=16,
    speed=1.05,
)

sf.write(
    OUTPUT_AUDIO,
    audio[0],
    model.sampling_rate
)

print(f"Saved to {OUTPUT_AUDIO}")
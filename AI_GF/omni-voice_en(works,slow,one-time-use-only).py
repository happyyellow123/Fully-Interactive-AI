# py -m pip install omnivoice soundfile
# this will only run when you open only this folder in vs code(i mean when you selecting a folder to open select AI_GF folder)
from omnivoice import OmniVoice
import torch
import soundfile as sf

model = OmniVoice.from_pretrained(
    "k2-fsa/OmniVoice",
    device_map="cuda:0",
    dtype=torch.float16
)

audio = model.generate(
    text="How are you today?.", # what to say
    ref_audio=r"E:\AI_GF\english_yamada.wav", # reference audio file to clone voice
    ref_text="You know what people saying these days, like, nobody want that kind of attitude. If you acting like that, everyone gonna be thinking you're just being stupid, you know what I mean?" # what does the reference audio say
)

sf.write(r"E:\AI_GF\voice_output\en_yamada_cloned.wav", audio[0], 24000)

print(r"Saved to E:\AI_GF\voice_output\english_yamada_cloned.wav")
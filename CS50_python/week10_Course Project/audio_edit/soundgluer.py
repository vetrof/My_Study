from pydub import AudioSegment

sound1 = AudioSegment.from_wav("wav/sound_1.wav")
sound2 = AudioSegment.from_wav("wav/sound_2.wav")

combined_sounds = sound1 + sound2
combined_sounds.export("wav/glued.wav", format="wav")





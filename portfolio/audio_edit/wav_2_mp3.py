from moviepy.editor import VideoFileClip,AudioFileClip

wav_file = "wav/sound_1.wav"#video file name
mp3_file="mp3/movepy2.mp3"#create new audio file

audioclip = AudioFileClip(wav_file)
audioclip.write_audiofile(mp3_file)
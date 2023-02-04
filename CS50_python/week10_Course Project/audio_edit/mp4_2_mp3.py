from moviepy.editor import VideoFileClip,AudioFileClip

mp4_file ="mp4/file.mp4"#video file name
mp3_file="mp3/movepy.mp3"#create new audio file

videoclip = VideoFileClip(mp4_file)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)


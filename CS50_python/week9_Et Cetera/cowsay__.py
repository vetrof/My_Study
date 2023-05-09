import cowsay
import pyttsx3

# engine = pyttsx3.init()
# # this = input("What's this? ")
# # cowsay.cow(this)
# engine.say('Hi')
# engine.say()
# engine.runAndWait()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()
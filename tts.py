from gtts import gTTS
import playsound
tts=gTTS('hello welcome to python world',lang='en')
tts.save('hello.mp3')
playsound.playsound('hello.mp3')
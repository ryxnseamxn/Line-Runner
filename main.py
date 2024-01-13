import speech_recognition as sr 
from gtts import gTTS   
from playsound import playsound 
import elevenlabs


r = sr.Recognizer()
mic = sr.Microphone()   
language = 'en'    

with mic as source:
    print("Speak")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    print("Stop speaking")

# harvard = sr.AudioFile('audio/harvard.wav')
# with harvard as source:
#     audio = r.record(source)

try:
    transcription = r.recognize_google(audio)
    print(transcription)
except sr.RequestError:
    print("Request Error")
except sr.UnknownValueError:
    print("Unknown Value")

tts = elevenlabs.generate(text=transcription, voice="Grace")

elevenlabs.play(tts)
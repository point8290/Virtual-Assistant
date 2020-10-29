import speech_recognition as sr
import webbrowser
import time
import os
import playsound
import random
from gtts import gTTS

r = sr.Recognizer()

def RecordAudio(ask = False):
    with sr.Microphone() as source:
        if ask:
            Speak("Ask")
        audio = r.listen(source)
        voice_data=""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            Speak("SORRY I DID NOT GET THAT")
        except sr.RequestError:
            Speak("SORRY I'M NOT FEELING WELL")
def Speak(audio_str):
    tts = gTTS(text=audio_str, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_str)
    os.remove(audio_file)


def respond(voice_data):
    if "name" in voice_data:
        Speak("Hi I'm Siri")
    if "what time is it" in voice_data:
        Speak(time.ctime())
    if "search" in voice_data:
        search = RecordAudio('What do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        Speak('Here is what i found for you ' + search)
    if "find location" in voice_data:
        location = RecordAudio('Location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        Speak('Here is the location ' + location)
    if "exit" in voice_data:
        exit()

time.sleep(1)
Speak("How can I help you!!")
while 1:
    voice_data = RecordAudio()
    print(voice_data)


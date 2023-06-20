#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from translate import Translator
#from googletrans import Translator
import pyttsx3
from gtts import gTTS
import playsound

# original language setting
#language = "es-ES"
language = "en-US"

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`

    # speech recognition
    input_text = r.recognize_google(audio)
    print("Original text: " + input_text)

    # translate text to chinese (Google API)
    translator= Translator(from_lang = language, to_lang="zh")
    output_text = translator.translate(input_text)
    print("Chinese translation: "+ output_text)

    """# translate text to chinese (Googletrans)
    translator = Translator(src = language, dest="zh")
    output_text = translator.translate(input_text)
    print("Chinese translation: "+ output_text) """

    # text to speech Google gTTS
    tts = gTTS(output_text, lang="zh")
    tts.save("speech.mp3")
    playsound.playsound("speech.mp3")

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


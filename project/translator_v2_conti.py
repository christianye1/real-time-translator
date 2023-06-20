import speech_recognition as sr
from translate import Translator
import pyttsx3
from gtts import gTTS
import playsound


# Original language setting
#language = "en-US"
language = "de"

# Create translator object
translator = Translator(from_lang = language, to_lang="zh")

# Create speech recognizer object
r = sr.Recognizer()

# Create text-to-speech engine
engine = pyttsx3.init()

# Initialize variables
buffer = ""
sentence_enders = [".", "?", "!"]

# Continuously listen for audio input and translate
while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        print("finished listening")

    try:
        # Speech recognition
        input_text = r.recognize_google(audio)
        print("Original text: " + input_text)

    
        # Translate the complete sentence
        output_text = translator.translate(input_text)
        print("Chinese translation: " + output_text)

        # Text-to-speech
        # text to speech Google gTTS
        tts = gTTS(output_text, lang="zh")
        tts.save("speech.mp3")
        playsound.playsound("speech.mp3")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

from pickle import NONE
import speech_recognition as sr
from translate import Translator
import pyttsx3
from gtts import gTTS
import playsound
import threading
import queue

# debug
import time
now = time.time()


# Original language setting
language = "en-US"

# create queues for data transfer between threads
queue_ogaudio = queue.Queue()
queue_transtext = queue.Queue()

# Create translator object
translator = Translator(from_lang = language, to_lang="zh")

# Create speech recognizer object
r = sr.Recognizer()

# Create text-to-speech engine
engine = pyttsx3.init()

def translation():
    while True:
        elapsed_time = int(time.time())- int(now)
        try:
            audio = queue_ogaudio.get()
            # do translation    
            input_text = r.recognize_google(audio)
            print(input_text)
            # Translate the complete sentence
            output_text = translator.translate(input_text)
            # save audio to queue
            queue_transtext.put(output_text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        print("elapsed time: "+ str(elapsed_time))
        now = time.time()

def speak():
    while True:
        # get audio from queue
        output_text = queue_transtext.get()
        # text to speech Google gTTS
        tts = gTTS(output_text, lang="zh")
        tts.save("tanslated_text.mp3")
        playsound.playsound("tanslated_text.mp3")


# define threads
trans_thread = threading.Thread( target = translation, daemon=True )
speak_thread = threading.Thread( target = speak, daemon=True )

# run threads
try:
    trans_thread.start()
    speak_thread.start()
except: 
    print("Error: unable to start thread")

# main thread: Continuously listen for audio input and save in a str 
while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        #audio = r.recognize_google(source)
        # put data in queue
        queue_ogaudio.put(audio)

        
        #print(queue_transtext.qsize())
        #print(trans_thread.is_alive())
        #elapsed_time = int(time.time())- int(now)
        #now = time.time()
        #print("elapsed time: "+ str(elapsed_time))
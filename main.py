import pyttsx3
# This is a text to voice module. (basically the voice of our AI)
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Raph: active")

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning J!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon J!")
    else:
        speak("Good Evening J!")
wish()
speak("I am Raphael. Please tell me how can I help you today.")

# Real work. 

def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try : 
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except :
        print("Unable to recognize your voice. Please try again.")
takecommand()
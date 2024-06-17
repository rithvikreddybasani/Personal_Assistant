import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "f611a7cb2d7a4570a42697237a518134"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
  tts = gTTS(text)
  tts.save('temp.mp3')
  pygame.mixer.init()
  
  pygame.mixer.music.load('temp.mp3')
  pygame.mixer.music.play()
  
  while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
    
  pygame.mixer.music.unload()
  os.remove('temp.mp3')
  
    
def processCommand(c):
  if "open google" in c.lower():
    webbrowser.open("https://google.com")
  elif "open facebook" in c.lower():
    webbrowser.open("https://facebook.com")
  elif "open youtube" in c.lower():
    webbrowser.open("https://youtube.com")
  elif c.lower().startswith("play"):
    song = c.lower().split(" ")[1]
    link = musicLibrary.music[song]
    webbrowser.open(link)
  elif "news" in c.lower():
    r = requests.get('https://newsapi.org/v2/top-headlines?country=us&apikey=f611a7cb2d7a4570a42697237a518134')
    if r.status_code == 200:
      data = r.json()
      articles = data.get('articles',[])
      for article in articles:
        speak(article['title'])
  else:
    speak("Ask me anything")
  
if __name__ == '__main__':
    speak("Initializing Elina")
    while True:
      # listen for the wake word "Jarvis"
      # obtain audio from the microphone
        r = sr.Recognizer()
          
          
        print("recognizing...")  
        try:
          with sr.Microphone() as source:
              print("Listening....")
              audio = r.listen(source,timeout=2)
          command = r.recognize_google(audio)
          if(command.lower()=='elina'):
            speak("Ya")
            with sr.Microphone() as source:
              print("Jarvis Active...")
              audio = r.listen(source)
              command = r.recognize_google(audio)
              
              processCommand(command)
              
        
        except  Exception as e:
            print("Sphinx error;{0}".format(e))
        

import os
import speech_recognition as sr
import webbrowser
import pyttsx
import random
import ssl
import json
import urllib
import ctypes
import requests
from bs4 import BeautifulSoup

engine = pyttsx.init()
chrome_path = '/usr/bin/google-chrome %s'

def terminal():
        os.system("gnome-terminal -e 'bash -c \"cd; exec bash\"'")
        engine = pyttsx.init()
        engine.say('Welcome to the terminal')
        engine.runAndWait()

def internet():
        engine = pyttsx.init()
        engine.say('Welcome to Google')
        engine.runAndWait()
        webbrowser.get(chrome_path).open(url)

def sublime():
        os.system("start sublime-text.exe")

def mainfunction(source):

    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    put = r.recognize_google(audio)
    put =put.lower()
    link = put.split()
    if put == '':
        with sr.Microphone() as source:
            audio = r.listen()
        try:
            mainfunction(source)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google STT; {0}"
                  .format(e))
        except:
            print("Unknown exception occurred!")


    if put.startswith('open '):
        try:
            engine = pyttsx.init()
            engine.say("opening " + link[1])
            engine.runAndWait()
            webbrowser.get(chrome_path).open('http://www.' + link[1] + '.com')
        except:
            print('Sorry, No Internet Connection!')

    if put.startswith('play '):
        try:
                    link = '+'.join(link[1:])
                    say = link.replace('+', ' ')
                    url = 'https://www.youtube.com/results?search_query=' + link

                    engine = pyttsx.init()
                    engine.say("playing " + say)
                    engine.runAndWait()
                    webbrowser.get(chrome_path).open(url)
        except:
                    print('Sorry, No internet connection!')

                    # Google Search
    if put.startswith('search '):
        try:
                    link = '+'.join(link[1:])
                    say = link.replace('+', ' ')
                    # print(link)
                    engine = pyttsx.init()
                    engine.say("searching on google for " + say)
                    engine.runAndWait()
                    webbrowser.get(chrome_path).open('https://www.google.co.in/search?q=' + link)
        except:
                    print('Sorry, No internet connection!')
    if put.startswith('science '):
        try:
            jsonObj = urllib.request.urlopen('''https://newsapi.org/v1/articles?source=new-scientist&sortBy=top&apiKey=31c5e635e0764845a2c265265ffbe0af''')
            data = json.load(jsonObj)
            i = 1
            engine = pyttsx.init()
            engine.say('''Here are some top science
                         news from new scientist''')
            engine.runAndWait()
            print('''             ================NEW SCIENTIST=============
                  ''' + '\n')
            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                i += 1
        except:
            print('Sorry, No internet connection')

    if put.startswith('headlines '):
        try:
            jsonObj = urllib.request.urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=31c5e635e0764845a2c265265ffbe0af''')
            data = json.load(jsonObj)
            i = 1
            engine = pyttsx.init()
            engine.say('here are some top news from the times of india')
            engine.runAndWait()
            print('''             ===============TIMES OF INDIA============'''+ '\n')
            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                i += 1
        except Exception as e:
            print(str(e))

    if put.startswith('lock '):
        try:
            engine=pyttsx.init()
            engine.say("locking the device")
            engine.runAndWait()
            os.system("gnome-terminal -e 'bash -c \"cd; exec bash\"'")

        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            mainfunction(source)
#pip install all of these some may already be installed.
import pickle
import os.path
import os
import time
import pyttsx3
import speech_recognition as sr#needs pyaudio (pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl) copy this
import subprocess
import random
import requests
import winwifi






#winwifi.WinWiFi.connect('Hanauma Bay')
welcome = ["Your Welcome", "Welcome", "welcome Sir", "Your Welcome Sir"]
hello = ["Hello", "Hi", "Hello Sir"]
unknown = ["You are still trying to upgrade my knowlage", "rephrase", "i didn't catch that can you say it agian", "I don't understand"]

randhello = random.choice(hello)
randwelcome = random.choice(welcome)
randunknown = random.choice(unknown)








    

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october","november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]



    


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        import pandas as pd

        df = pd.DataFrame({said})

        df.to_excel('./states.xlsx')
                
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("e" + str(e))
            
    return said.lower()







def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

speak("Start")


    
    
while True:
    import datetime
    ctm = datetime.datetime.now() 
      
    ct = ctm.strftime("%H%M")
    
    
    text = get_audio()
    
    
    
    
    
    
    try:    

        if text == "what is your name":
            speak("My name is Pixel")

        elif text == "who made you" or text == 'who designed you':
            speak("i was made for Journey Tech by Jed Johnson")

        elif text == "pixel" or text == "p" or text == "hey pixel" or text == "hey p":
            speak("Yes Sir")

        elif text == "how are you" or text == 'how was your day' or text == 'how is your day':
            speak("Im having a good day. How was Yours?")

        elif text == "hello" or text == "hi":
            speak(randhello)

        elif text == "system":
                ssid1 = winwifi.WinWiFi.connect('Hanauma Bay')
                if ssid1 == False:
                    ssid2 = winwifi.WinWiFi.connect('Kahuku Beach')
                elif ssid1 == True:
                    speak("We are online and ready")
                elif ssid1 == False and ssid2 == False:
                    ("offline")

        elif text == 'connect to wifi' or text == 'Wi-Fi':
            ssid1

        elif text == "shut down":
            os.system("shutdown /s")

        elif text == "what time is it" or text == "time" or text== "whats the time":
            speak("its" +ct)

        elif text == "reboot":
            os.system("wmic os where Primary='TRUE' reboot")

        elif text == "good morning" or text == "morning" or text == "morning pixel" or text == "good morning pixel" or text == "morning p" or text == "good morning p":
            speak("Good Morning Sir")

        elif text== "calculator" or text == "open Calculator":
            import calculator

        elif text == "what did i say" or text == "what did i just say" or text == "what i just say":
            speak("You said" + text)

        elif text == "thank you" or text == "thanks":
            speak(randwelcome)

        elif text == "run diagnostic" or text == "diagnostic":
            system = os.system("netsh wlan show profiles")
            speak(system)
        
        elif text == "it's been a day" or text == "tiring":
            speak("I am sorry to hear that" + "would you like to open your scheadule to see what events are happening today???")
            
        
        elif text == "open Minecraft":
            open("C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher")
            speak('opening minecraft')

        elif text == 'decent' or text == 'its been a good day' or text == 'good' or text == 'pretty good':
            speak('Im glad to hear that, what can i do for you today?')

        elif text == 'cancel':
            pass
        
        
    
    except:
        speak('That didnt work. Please Try agian')

  

                
                


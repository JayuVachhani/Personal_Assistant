import pyttsx3
from datetime import datetime
import speech_recognition as sprc
import wikipedia
import webbrowser
import os
import random

''' sapi5 is a microsoft's speech api
 it is used to take different voices '''
speech_api = pyttsx3.init('sapi5')

# it provides available voices
voices = speech_api.getProperty('voices')

''' there are two voices available
1. 0 id is for male
2. 1 id is for female '''
speech_api.setProperty('voice',voices[1].id)



def speak(audio):
    # say function is used to speak the message 
    speech_api.say(audio)
    speech_api.runAndWait()

def wishme():
    speak("Please Enter your Name")
    name = input()
    hour = datetime.now().hour    

    if hour > 0 and hour <= 12:
        speak(f"Hello {name} Good Morning")
    elif hour > 12 and hour <= 15:
        speak(f"Hello {name} Good Noon")
    elif hour > 15 and hour <= 18:
        speak(f"Hello {name} Good Afternoon")
    elif hour > 18 and hour <= 21:
        speak(f"Hello {name} Good Evening")
    else:
        speak(f"Hello {name} Good Night")
    speak("My name is Zira, How may i help you today?")


def command():
    '''
    it take microphone voice input from the user
    and returns string output
    for that recognizer is used
    '''
    
    listen_voice = sprc.Recognizer()
    with sprc.Microphone() as srmc:
        print("Listening.....")

        # it will wait for 1 second
        # listen_voice.pause_threshold = 1

        audio = listen_voice.listen(srmc)
    
        
    
    try:
        print("Recognizing......")
        query = listen_voice.recognize_google(audio, language='en-in')
        print("You said ",query)
    
    except Exception as e:
        print(e)
        print("Result not Found, Please try again")
    return query


if __name__ == '__main__':    
    wishme()
    if 1:
        query = command().lower()

        if 'wikipedia' in query:
            speak("Searching in Wikipedia")
            query = query.replace("wikipedia", "")
            output = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            speak(output)

        elif 'youtube' in query:
            speak('Opening Youtube')
            webbrowser.open('youtube.com')

        elif 'google' in query:
            speak('Opening Google')
            webbrowser.open('google.com')

        elif 'spotify' in query:
            speak('Opening Spotify')
            webbrowser.open('spotify.com')
        
        elif 'time' in query:
            time = datetime.now()
            print(time)
            speak(f"Current time is {time}")

        elif 'music' in query or 'song' in query:
            speak("Playing Music for you")
            music_dir = 'D:\\Music\\FL'
            music = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,random.choice(music)))
            print(random.choice(music))
        
        elif 'code' in query:
            speak("Opening Visual Studio Code")
            path = 'C:\\Users\\Jay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(path)
        
        elif 'notepad' in query:
            speak("Opening NotePad")
            path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad'
            os.startfile(path)
        
        else:
            speak("Sorry service is not available for this command, i apologies for that, You can give other commands thank you")

        

        


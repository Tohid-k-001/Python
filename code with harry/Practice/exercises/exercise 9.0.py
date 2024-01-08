#Write  a programme to give shout out to the names listed in list
# --> for mac
# from os import system
list=["tohid","rahul","yug","sanmay"]
# for name in list:
#     print(f"Say Shout out to {name}")

# for windows:-
import pyttsx3 as pt        # --> import a voice from windows
engine=pt.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty("voice",voice[0].id)

def speak(str):         # --> to speak function
    engine.say(str)
    engine.runAndWait()

if __name__=='__main__':
    for name in list:
        speak(f"Shout out to {name}")




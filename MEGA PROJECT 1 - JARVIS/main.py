import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLiberary
import requests

# pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "a7026cc3e9e94dd7bcde28de0e0ad2ab"
 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkdin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLiberary.music[song]
        webbrowser.open(link)

    elif "news" in  c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=a7026cc3e9e94dd7bcde28de0e0ad2ab")
        if r.status_code == 200:
            #pase the json responce
            data = r.json()

            # Extract titles into a list
            articles = data.get("articles",[])

            #speak the headlines
            for article in articles:
                speak(article["title"])

    else:
        # let openAI handle the request
        pass


if __name__ == "__main__":
    speak("initilizing Jarvis....")
    while True :
        # listen for the wake word "jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening....")
            audio = r.listen(source, timeout =2)

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening....")
                audio = r.listen(source, timeout =2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("ya")
                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)
       
        except Exception as e:
            print(" error; {0}".format(e))




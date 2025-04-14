import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLiberary
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
newsapi = os.getenv("NEWS_API_KEY")

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")  # typo fixed

    elif c.startswith("play"):
        song = c.split(" ")[1]
        link = musicLiberary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"I couldn't find the song {song} in your music library.")

    elif "news" in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            if articles:
                speak("Here are the latest headlines:")
                for article in articles:
                    title = article.get("title")
                    print(title)
                    speak(title)
            else:
                speak("Sorry, I couldn't find any news articles.")
        else:
            speak("Failed to fetch news.")

    else:
        speak("Sorry, I didn’t understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)

            word = recognizer.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                print(f"Command: {command}")
                processcommand(command)

        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, I didn't catch that.")



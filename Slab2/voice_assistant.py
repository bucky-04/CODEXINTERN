import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

def talk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        return listener.recognize_google(voice)

def run_assistant():
    command = listen().lower()
    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"Current time is {time}")
    elif "youtube" in command:
        topic = command.replace("youtube", "")
        talk(f"Searching YouTube for {topic}")
        pywhatkit.playonyt(topic)

if __name__ == "__main__":
    run_assistant()

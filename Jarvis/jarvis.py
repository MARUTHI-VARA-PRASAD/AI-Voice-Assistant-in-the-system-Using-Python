import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import pyautogui
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    """Make Jarvis speak"""
    engine.say(audio)
    engine.runAndWait()

def wishme():
    """Wish the user according to time"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("Jarvis at your service. Please tell me how may I assist you.")

def takecommand():
    """Take microphone input from user and return string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except Exception:
            return "none"
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception:
        speak("Say that again please...")
        return "none"
    return query.lower()

def screenshot():
    """Take a screenshot and save it to Pictures"""
    import os
    save_dir = os.path.join(os.path.expanduser("~"), "Pictures")
    os.makedirs(save_dir, exist_ok=True)
    img_path = os.path.join(save_dir, "screenshot.png")
    img = pyautogui.screenshot()
    img.save(img_path)
    speak(f"Screenshot saved to {img_path}")

# ---------------- MAIN PROGRAM ----------------

if __name__ == "__main__":
    speak("Welcome back, sir!")
    wishme()

    while True:
        query = takecommand()

        if query == "none":
            continue

        # -------- Basic Commands --------
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open notepad' in query:
            os.startfile("C:\\Windows\\system32\\notepad.exe")

        elif 'open chrome' in query:
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            if os.path.exists(chrome_path):
                os.startfile(chrome_path)
            else:
                speak("Chrome not found, please check its path.")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")

        elif 'open calculator' in query:
            os.startfile("C:\\Windows\\System32\\calc.exe")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'screenshot' in query:
            screenshot()

        elif 'what is the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'shutdown system' in query:
            speak("Shutting down the system")
            os.system("shutdown /s /t 5")

        elif 'quit' in query or 'exit' in query:
            speak("Goodbye sir, have a nice day!")
            break

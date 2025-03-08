import speech_recognition as sr
import pyttsx3
import webbrowser
import urllib.parse
import datetime

# Initialize text-to-speech engine
eng = pyttsx3.init()

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to speak text
def speak(text):
    eng.say(text)
    eng.runAndWait()

# Function to listen for commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
        audio = recognizer.listen(source)  # Listens to the microphone
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()  # Recognizes speech
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, couldn't process the request.")
            return ""

# Function to play a song on YouTube
def play_on_youtube(song):
    search_query = urllib.parse.quote(song)
    url = f"https://www.youtube.com/results?search_query={search_query}"
    webbrowser.open(url)

# Function to get the current date
def get_date():
    date = datetime.datetime.now()
    speak(f"Today's date is {date.strftime('%B %d, %Y')}")

# Function to get the current time
def get_time():
    time = datetime.datetime.now()
    speak(f"The current time is {time.strftime('%I:%M %p')}")

# Main function for the voice assistant
def main():
    speak("Hello! I'm your voice assistant. How can I help you?")
    while True:
        command = listen()
        if "hello" in command:
            speak("Hello there!")
        elif "how are you" in command:
            speak("I'm doing well, thank you for asking!")
        elif "open google" in command:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")
        elif "open youtube" in command:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")
        elif "play" in command and "on youtube" in command:
            song = command.replace("play", "").replace("on youtube", "").strip()
            speak(f"Playing {song} on YouTube.")
            play_on_youtube(song)
        elif "date" in command:
            get_date()
        elif "time" in command:
            get_time()
        elif "stop" in command:
            speak("Goodbye!")
            break
        else:
            speak("Unable to give the response. Can you please try again?")

if __name__ == "__main__":
    main()

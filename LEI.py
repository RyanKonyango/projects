import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyttsx3
import subprocess

# Initialize Text-to-Speech Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    """Speaks the provided audio string."""
    engine.say(audio)
    engine.runAndWait()


def is_spotify_installed():
    """Checks if Spotify is installed on the system."""
    installed_apps = subprocess.check_output('powershell "Get-AppxPackage -Name SpotifyAB.SpotifyMusic"', shell=True)
    return 'SpotifyAB.SpotifyMusic' in installed_apps.decode()


def play_music(source=None, song_title=None):
    """Plays music based on user preference: YouTube, Spotify, local files,
       and song requests.

    Args:
        source (str, optional): The preferred source for music playback.
                                 Can be 'youtube', 'spotify', or 'local'.
                                 Defaults to None.
        song_title (str, optional): The specific song to play. Defaults to None.
    """

    if source:
        source = source.lower()
        if source == 'youtube':
            if not song_title:
                speak("What song would you like to play on YouTube?")
                song_title = take_command().lower()
                
            open_youtube_video(song_title)
        elif source == 'spotify':
            if not song_title:
                speak("What song would you like to play on Spotify?")
                song_title = take_command().lower()
            # Search for the song on Spotify (assuming Spotify Premium for ad-free playback)
            webbrowser.open(f"https://open.spotify.com/search/{song_title}")
            speak(f"Playing '{song_title}' on Spotify.")
        elif source == 'local':
            music_directory_path = 'C:/User/Lenovo/Music'  # Adjust path as needed
            play_music_from_directory(music_directory_path)
        else:
            speak(f"Invalid source: {source}. Please choose YouTube, Spotify, or local.")
    else:
        # Ask user for preference if no source is specified
        speak("Where would you like to play music? (YouTube, Spotify, or local files)")
        source = take_command().lower()
        play_music(source)



def play_music_from_spotify():
    """Opens Spotify in the web browser."""
    webbrowser.open('https://open.spotify.com')


def play_music_from_directory(directory_path):
    """Plays music from the specified directory."""
    music_files = [f for f in os.listdir(directory_path) if f.endswith(('.mp3', '.wav'))]
    if music_files:
        os.startfile(os.path.join(directory_path, music_files[0]))
    else:
        print("No music files found in the directory.")

def open_youtube_video(video_title=None):
    """
    Searches and opens the specified YouTube video in the web browser,
    prompting the user for input if no title is provided.

    Args:
        video_title (str, optional): The title of the YouTube video to open.
                                    Defaults to None.
    """

    if not video_title:
        speak("What YouTube video would you like to watch?")
        video_title = take_command().lower()

    # Escape special characters in the user's query to prevent errors in the URL
    escaped_title = video_title.replace(" ", "%20")  # Replace spaces with "%20"

    webbrowser.open(f"https://www.youtube.com/results?search_query={escaped_title}")
    speak(f"Opening YouTube video: {video_title}")


def send_email(to, content):
    """Sends an email to the specified recipient."""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com', 'your_app_password')  # Use a secure app password
    server.sendmail('your_email@gmail.com', to, content)
    server.close()
    speak("Email has been sent!")
    
def open_google(search_query=None):
    """Performs a Google search using the webbrowser library,
       prompting the user for input if no search query is provided.

    Args:
        search_query (str, optional): The search query to use. Defaults to None.
    """

    if not search_query:
        speak("What would you like to Google?")
        search_query = take_command().lower()

    speak("Ah, excellent choice! Exquisite taste might I add sir")
    webbrowser.open(f"https://www.google.com/search?q={search_query}")
    speak(f"Searching Google for: {search_query}")
    
def quit_program():
    """Ends the program gracefully with a goodbye message."""
    speak("Thank you for interacting with me! It was a pleasure assisting you. Have a great day! Don't forget to support my creator, Ryan.")
    exit()  # Use exit() to terminate the program



def wish_me():
    """Greets the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir! How may i help you?")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir! Lovely weather we are having today.")
    else:
        speak("Good Evening Sir! Hope you had a wonderful day.")


def take_command():
    """Takes microphone input from the user and returns it as a string."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


def main():
    """Main function that runs the virtual assistant with enhanced features."""

    while True:
        wish_me()  # Call wish_me function inside the loop

        query = take_command().lower()

        # Execute commands based on user input
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            open_youtube_video()

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            play_music()

        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {str_time}")

        elif 'open code' in query:
            code_path = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'open epic' in query:
            epicPath= "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(epicPath)
            
if __name__ == "__main__":
    wish_me()
    while True:
    # if 1:
        query = take_command().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            open_youtube_video()

        elif 'open google' in query:
            open_google()

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
             # Check for specific source mentioned
            speak("I can't directly play music myself yet, but I can help you find it on YouTube, Spotify, or your local music files.")

            if 'youtube' in query:
                play_music('youtube')
            elif 'spotify' in query:
                play_music('spotify')
            else:
                play_music()  # No specific source mentioned, prompt user

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # elif 'open code' in query:
        #     codePath = "C:\Users\LENOVO\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        #     os.startfile(codePath)

        elif 'email to john' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "omondikor@gmail.com"
                send_email(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Boss. I am not able to send this email")
                
        elif 'open epic' in query:
            epicPath= "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(epicPath)
            
        elif 'open code' in query:
            code_path = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        
        elif 'exit' in query:
            quit_program()
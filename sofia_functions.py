import os
from time import sleep

from gtts import gTTS  # Google's Text to Speech
import pyttsx3
from platform import system


def clearer():
    '''Clears the CLI'''

    os.system("cls" if os.name == "nt" else "clear")


def cache_clearer():
    '''Removes past session\'s activity'''

    try:
        os.remove("output.mp3")
        os.remove(".google-cookie")
    except OSError:
        pass


# Use Google's Text to Speech, save it as mp3, play it, and then delete it
def say1(lines):
    '''Text parsed to Google\'s Text-to-Speech API
        to return a playable voice'''

    if os.name == "nt":
        tts = gTTS(text=lines, lang='en', slow=False)
        tts.save("output.mp3")

        import pygame.mixer
        pygame.mixer.init()
        pygame.mixer.music.load(open(f"{os.getcwd()}/output.mp3", "rb"))
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            sleep(1)

        cache_clearer()

    else:
        import pygame
        gTTS(text=lines, lang='en', slow=False).save("output.mp3")
        pygame.init()
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()

        clock = pygame.time.Clock()
        clock.tick(10)

        # Don't let the function finish until the entire mp3 is loaded
        # to prevent the program from hearing itself
        while pygame.mixer.music.get_busy():
            pygame.event.poll()
            clock.tick(10)

        cache_clearer()


# Use pyttsx3's offline Text to Speech
def say2(lines):
    '''Text parsed to pyttsx3's offline Text-to-Speech'''

    engine = pyttsx3.init()
    engine.setProperty('volume', 1)

    if os.name != "nt":  # Set the female voice for Linux systems
        engine.setProperty('voice', 'english+f4')
        engine.setProperty('rate', 140)
    else:
        voices = engine.getProperty('voices')  # Set the female voice for Windows systems
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 120)

    engine.say(lines)
    engine.runAndWait()
    clearer()
    print("Listening...")


def inputName(say):
    '''Takes user\'s name and stores it in a .txt file'''

    while 1:
        name = input("Your name: ")
        if len(name) < 2:
            print("The written name is too short, try again.\n")
        else:
            break
    with open("user_information.txt", "w") as f:
        f.write(f"name='{name}'")
    say(f"Alright. Nice to meet you {name}")
    sleep(2)
    clearer()
    print("Listening...")


# Returns time differece between a set date and today's date
def sofiaAge():
    '''Calculate and return Sofia\'s age'''

    import datetime

    today = datetime.datetime.today().strftime('%Y-%m-%d').split('-')
    today = [int(item) for item in today]
    today = datetime.date(today[0], today[1], today[2])
    creationDate = datetime.date(2019, 5, 13)
    sofiaAge = today - creationDate
    return sofiaAge.days

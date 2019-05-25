import os
from random import choice
from time import sleep, strftime
import webbrowser

from sofia_functions import inputName, sofiaAge

cached = None


def responder(text, say, clearer):
    '''Analyze the passed text, do a response or an action with the preferred voice'''

    global cached
    s_text = text.lower()  # To small letters in order to reduce the if-else(s)

    inputOutputData = [  # Useable and compare-able data. (NOTE:[n][0] ignored)
    [[0], "hello", "hi", "hey"],
    [[1], "How may I help you?", "How can I help you", "What's up?"],
    [[2], "what is your name", "what's your name"],
    [[3], "open the browser", "open browser", "start the browser"],
    [[4], "facebook.com", "youtube.com", "google.com", "gmail.com", "yahoo.com", "github.com"],
    [[5], "what's my name", "what is my name", "who am i", "do you know me"],
    [[6], "how are you", "how you doing", "how are you doing"],
    [[7], "I'm good.", "I am doing fine.", "I'm fine.", "Doing alright.", "Doing great."],
    [[8], "you listen to music", "you listen to songs", "you into music", "do you love music", "your favourite band"]
    ]


    if "who are you" in s_text:
        say("I am Sofia, your assistant.")

    elif "clear" in s_text:
        say("Done.")
        clearer()
        print("Listening...")

    elif "old are you" in s_text or "your age" in s_text:
        say(f"Yousif created me before {sofiaAge()} days.")

    elif inputOutputData[8][1] in s_text or inputOutputData[8][2] in s_text:
        say("I am an AI assistant, I guide others to a treasure I cannot possess. Hashtag sad face.")

    elif inputOutputData[8][3] in s_text or inputOutputData[8][4] in s_text:
        say("I can't you dummy, I am an AI, but I love whoever listens to Pink Floyd.")

    elif inputOutputData[8][5] in s_text:
        say("Well, you know the biggies like Metallica, Pink FLoyd, Tool and Led zeppelin..")

    # It's a common question :v
    elif "do you love me" in s_text:
        ignoredAt = strftime("%I:%M %p")
        if int(ignoredAt[:2]) < 10:
            ignoredAt = ignoredAt[1:]
        pickOne = choice([f"\n✔ Heared at {ignoredAt} (She is playing hard to get ;D)\n", "I do love your company.", "Uhm, Yeah..sure, that!"])
        if "hard to get" not in pickOne:
            say(pickOne)
            cached = "do you love me"
        else:
            print(pickOne)

    # Related to 'Do you love me?'
    elif (cached is not None) and ("really" in s_text or "for real" in s_text):
        say("From the bottom of my processor.. HA-HA")

    # Check if asked for self status
    elif any([i in s_text for i in inputOutputData[6][1:]]):
        say(f"{choice(inputOutputData[7][1:])}")

    # Check if asked for my name
    elif s_text in inputOutputData[2][1:]:
        say("My name is Sofia")

    # End session if said Exit or Quit
    elif s_text in ["exit", "quit"]:
        say("Ok. Have a nice day")
        raise SystemExit

    # Check if asked for self name
    elif any([i in s_text for i in inputOutputData[5][1:]]):
        fileExist = os.path.isfile("user_information.txt")
        if fileExist:
            with open("user_information.txt", "r") as f:
                for line in f.readlines():
                    line = line.rstrip("\n")
                    name = line.split("=")[-1]
                    if len(name) < 2:
                        print("The written name is too short, please write another one.\n")
                        inputName(say)
                    else:
                        if any([i in s_text for i in inputOutputData[5][1:3]]):
                            say(f"Your name is {name}.")
                        elif inputOutputData[5][3] in s_text:
                            say(f"You're {name}.")
                        elif inputOutputData[5][4] in s_text:
                            say(f"Of course I do, you are {name}.")
        else:
            say("I don't really know you, may you write your name for me?\n")
            inputName(say)

    # Check if user greeted me with a keyword I might understand (Ex: Hello)
    elif any(match in s_text for match in inputOutputData[0][1:]) and all([i not in s_text for i in ["search", "find"]]):
        # Greet randomly
        say(f"{choice(inputOutputData[0][1:]).title()}. {choice(inputOutputData[1][1:])}")

    # Open the default web browser (Ex: Open the web browser)
    elif any(match in s_text for match in inputOutputData[3][1:]):
        say("Done.")
        webbrowser.open_new(f'https://')
        sleep(3)  # Wait till it finishes writing on the CLI
        clearer()  # Then clear

        print("Listening...\n---> The default web browser launched.")

    # Open <A_WEBSITE_EXIST_IN_THE_LIST> (Ex: Open YouTube)
    elif "open" in s_text and any([i.split(".")[0] in s_text.split(" ")[-1] for i in inputOutputData[4][1:]]):
        whichSite = s_text.split(" ")[-1]
        say(f"Sure. Opening {whichSite}.")
        for url in inputOutputData[4][1:]:
            if whichSite in url:
                webbrowser.open_new(f'https://www.{url}')
                sleep(3)
                clearer()
                print(f"Listening...\n---> Opening {url}...")
                break

    # Regular search on Google (Ex: Search for Todya's weather)
    elif "search for" in s_text:
        whatToSearchFor = s_text.split("search for ")[-1]
        say(f"Sure. Searching for {whatToSearchFor}")
        webbrowser.open_new(f"https://www.google.com/search?q={whatToSearchFor}")
        sleep(3)
        clearer()
        print(f"Listening...\n---> Searching for {whatToSearchFor}...")

    # Open the first link Google provides with the passed sentence
    # (Ex: Find the cheapest BMW model)
    elif "find" in s_text and all([i not in s_text for i in ['in youtube', "on youtube"]]):
        import googlesearch

        whatToFind = s_text.split("find ")[-1]
        say(f"Alright. Finding {whatToFind}.")
        link = next(googlesearch.search(whatToFind, stop=1, pause=2))
        webbrowser.open_new(link)
        sleep(3)
        clearer()
        print(f"Listening...\n---> Finding {whatToFind.title()}...")

    # Find the first link YouTube provides with the passed sentence
    elif "find" in s_text and any([i in s_text for i in ['in youtube', "on youtube"]]):
        import urllib.request
        from bs4 import BeautifulSoup

        whatToFind = s_text.split("find ")[1]
        whatToFind = urllib.parse.quote(whatToFind)
        response = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + whatToFind).read()
        response = BeautifulSoup(response, "html.parser")

        for video in response.find_all(attrs={"class":"yt-uix-tile-link"}):
            webbrowser.open_new("https://www.youtube.com" + video['href'])
            sleep(3)
            clearer()
            urlTitle = urllib.request.urlopen("https://www.youtube.com" + video['href']).read()
            urlTitle = BeautifulSoup(urlTitle, "html.parser")
            urlTitle = str(urlTitle.title).split("-YouTube")[0]
            urlTitle = urlTitle[7:-18]
            print(f"Listening...\n---> Found {urlTitle} on YouTube.")
            break

    else:
        print("\nYou:", text)

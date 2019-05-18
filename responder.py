import os
import random
from platform import system

from sofia_functions import sofiaAge, selfName, cached

if system() == "Windows":
    linkOpener = "start"
elif system() == "Darwin":
    linkOpener = "open"
else:
    linkOpener = "xdg-open"


def responder(text, say, clearer):
    '''Analyze the passed text, does a response or an action with the preferred voice'''

    global selfName, cached


    def selfNameFunc():
        '''Sets a self name when triggered for that session'''
        global selfName
        say("I don't really know you, may you write your full name for me please?\n")
        while 1:
            selfName = input("Your name: ")
            selfName = selfName.title()
            if len(selfName) < 3:
                print("Sorry, your name is too short, try again please.\n")
            else:
                break
        if selfName:
            say(f"Alright, nice to meet you {selfName}")
            clearer()


    s_text = text[:].lower()

    if s_text == "quit" or text == "exit":
        say("Ok. See you later.")
        print("Exiting...")
        raise SystemExit
    elif "hi" == s_text or "hello" == s_text or "hello sophia" in s_text or "hi sophia" in s_text:
        if selfName != None:
            say(f"Hello {selfName.split(' ')[0]}, how can I help you?")
        elif selfName == None:
            say("Well, hello there.")
            selfNameFunc()
    elif "how are you" in s_text:
        say("I am actually fine, what about you?")
        cached = s_text
    elif ("i am good" in s_text or "i'm good" in s_text or "i am fine" in s_text or "i'm fine" in s_text) and cached != None:
        say("Alright, hopefully you remain so!")
    elif "your name" in s_text or "who are you" in s_text:
        say("My name is Sofia.")

    elif ("my name" in s_text or "do you know me" in s_text or "who am i" in s_text) and "change" not in s_text:
        if selfName == None:
            selfNameFunc()
        elif (selfName.split(" ")[0][0].lower() == "y" and selfName.split(" ")[0][-1].lower() == "f") and (selfName.split(" ")[-1].lower() == "adnan"
        ):
            say("You're my creator, Yusif!")
        else:
            say(f"You are {selfName}, my lovely guest!")
    elif "old are you" in s_text or "your age" in s_text:
        say(f"Yusif created me before {sofiaAge()} days.")
    elif s_text == "open facebook":
        say("Sure, opening Facebook")
        os.system(f"{linkOpener} http://facebook.com")
        clearer()
    elif "youtube" in s_text and "search for" in s_text:
        import urllib.request
        from bs4 import BeautifulSoup
        textToSearch = text.split("search for")[-1]
        query = urllib.parse.quote(textToSearch)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            say(f"Sure. Searching for {textToSearch}...\n")
            os.system(f'{linkOpener} https://www.youtube.com' + vid['href'])
            clearer()
            print(f"Finding {textToSearch}...\n")
            break
    elif "find" in s_text:
        import requests
        from googlesearch import search

        query = s_text.split("find")[-1]
        link = requests.get(next(search(query, tld="co.in", num=10, stop=1, pause=2)))
        os.system(f"{linkOpener} " + link.url)
        say(f"Ok. Searching for {query}")

    elif "open" in s_text and "youtube" in s_text:
        say("Sure, opening YouTube")
        os.system(f"{linkOpener} http://youtube.com")
        clearer()
    elif "open" in s_text and "google" in s_text:
        say("Sure, opening Google")
        os.system(f"{linkOpener} http://google.com")
        clearer()
    elif "change my name" in s_text:
        selfName = s_text.split("change my name to ")[-1].title()
        say(f"Ok. Your name changed to {selfName}")
        print(f"Your name is: {selfName}")
    elif s_text == "open google chrome" or s_text == "open chrome":
        say("Sure, opening Google chrome")
        if system() == "Windows":
            os.system("start chrome")
        elif system() == "Darwin":
            os.system("open -a 'Google Chrome'")
        else:
            os.system("google-chrome")
        clearer()
    elif "clear" in s_text:
        say("Done.")
        clearer()
    elif "search for" in s_text and "youtube" not in s_text:
        randomer = ["Ok", "Sure", "Alright"]
        textCopy = s_text[:]
        textCopy = textCopy.split("search for")
        os.system(f"{linkOpener} " + f'"https://www.google.com/search?q={textCopy[-1]}"')
        say(random.choice(randomer) + f". Searching for {textCopy[-1]}")
        clearer()
        print("")
        print("\nSearching for:", textCopy[-1])
    else:
        clearer()
        print("-->", text)

A mini artificial intelligence that can be used as an OS assistant to perform regular tasks and answer common questions.

# How to Launch Sofia
**`cd`** to Sofia's root directory and write in terminal:-

**`python sofia.py`**
# Handling common errors
Some Linux users might face problems with SpeechRecognition library for not detecting their input mic devices, this problem can be solved by downloading the follow two libraries:
- Pyaudio
- Portaudio

> If that didn't help, you can try **`Conda`** to install the mentioned repository in [this comment](https://github.com/ContinuumIO/anaconda-issues/issues/4139#issuecomment-433710003).

# Changing voice settings
In order to change the outputted voice you can do the following:-
1. Go to sofia.py
2. Find **responder()** function
3. Second parameter can be:-
    - "**sf.say1**" for a slow human-like voice. (Internet speed makes difference)
    - "**sf.say2**" for a fast robotic voice.

*NOTE: For extra voice control view **sofia_functions.say1()** or **sofia_functions.say2()***
# Dependencies
- Pyaudio
- gTTS
- urllib
- google
- SpeechRecognition
- BeautifulSoup4
- requests
- pyttsx3
- pygame


# Basic voice inputs
`Voice input: Hello Sofia / Hi Sofia / Hello / Hi / Who are you?..`

Voice output: Some action or respond...

`Voice input: Do you know me? / Who am I? / What is my name?`

Voice output: Some action or respond...

`Voice input: How are you? `

Voice output: Some respond...

`Voice input: Find the best BMW model`

Voice output: Opens the first link Google provides automatically...

`Voice input: Search for Eminem`

Voice output: A regular search in Google...

`Voice input: Search for Comfortably numb by Pink Floyd in YouTube`

Voice output: Opens the first result YouTube provides...

`Voice input: Change my name to <A_NAME>`

Voice output: Changes the name if previously set...

`Voice input: Open chrome / open Google Chrome`

Voice output: Opens Google Chrome (*No Sh\*t, ha?*)...

`Voice input: Open Google / Fscebook / YouTube`

Voice output: Opens one of the three mentioned above (*shocking*)...

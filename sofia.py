def main():
    import os
    import sys
    from time import sleep

    import speech_recognition as sr

    import responder
    import sofia_functions as sf

    r = sr.Recognizer()
    _breaker = 0
    _i = 0
    _worked = None
    while True:
        try:
            # Set listening port
            with sr.Microphone(device_index=_i) as source:
                _worked = _i
                sf.clearer()
                sf.cacheClearer()
                while 1:  # Keep listening

                    # Filter noise
                    r.adjust_for_ambient_noise(source)
                    # Listen to the port(The source)
                    audio = r.listen(source)

                    try:
                        # Hold what Googgle Speech-to-Text returns
                        text = r.recognize_google(audio)

                        # Respond or do an action
                        responder.responder(text, sf.say1, sf.clearer)

                    # Exit from Listening loop if session ended
                    except SystemExit:

                        _breaker = 1  # End the main loop
                        break  # Break listening loop at

                    except sr.UnknownValueError:
                        print("Sorry I didn't hear that. Please try again.")
                    except Exception as e:
                        printe(e)

        # Fail silently if device at 'i' was not found
        except Exception:
            print((f"No voice input device found at 'device_index={_i}',"
            " trying another one."))
            sleep(3)

        if _breaker == 1:
            break

        # If no voice input device found, then try another one
        if _worked is None:
            _i += 1

    sf.cacheClearer()

# Check if the dependencies exist
libs = ['pyaudio', 'googlesearch', 'gtts', 'speech_recognition',
                         'pyttsx3', 'requests', 'bs4', 'pygame']
_satisfied = 1
notInstalled = []

for lib in libs:
    try:
        exec(f"import {lib}")
    except:
        notInstalled += [lib]
        _satisfied = 0

if _satisfied == 1:
    main()
else:
    import os
    os.system('cls' if os.name == "nt" else "clear")
    print("The following packages are missing:-\n---------------")
    for lib in notInstalled:
        print("- ", lib)
    print("---------------\nInstall them and try again.\n")

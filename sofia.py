def goSofia():
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
                _worked = _i  # If no error raised at device_index=_i,
                              # then said _i is a source of voice input

                sf.clearer()  # Clear the screen
                print("Listening...")
                sf.cache_clearer()  # Clear the past session's data
                while 1:  # Keep listening

                    # Filter noise
                    r.adjust_for_ambient_noise(source)

                    # Listen to the port(The source)
                    audio = r.listen(source)
                    try:
                        # Send then hold what Googgle's Speech-to-Text returns
                        text = r.recognize_google(audio)

                        # Respond or do an action
                        responder.responder(text, sf.say1, sf.clearer)

                    # Exit from Listening loop if session ended
                    except SystemExit:
                        _breaker = 1  # End the main loop
                        break  # Break listening loop

                    # Handle it if voice was not recognized
                    except sr.UnknownValueError:
                        print("Sorry I didn't hear that. Can you repeat that?")
                    except Exception as e:
                        print(e)

        # Inform the user if the device at index of '_i' was not found
        except AssertionError:
            print(f"Device at device_index={_i} was not found, trying another one.")
            sleep(3)

        # Check if Sofia already running in another window
        except OSError as e:
            if e.errno == -9998:
                sf.clearer()
                print(f"device_index at {_i} is being used by another program or not available. Trying another one")
                sleep(2)
            else:
                print(e)

        if _breaker == 1:
            break

        # If no input device found at index of '_i', then try another one
        if _worked is None:
            _i += 1

    sf.cache_clearer()


def main():
    # Check if the dependencies are installed
    libs = ['pyaudio',
            'gtts',
            'speech_recognition',
            'pyttsx3',
            'pygame',
            'googlesearch',
            'bs4']

    _satisfied = 1
    notInstalled = []

    for lib in libs:
        try:
            exec(f"import {lib}")
        except:
            notInstalled += [lib]
            _satisfied = 0

    # If all set, launch Sofia
    if _satisfied == 1:
        goSofia()
    # If not, inform the user with the missing dependencies
    elif _satisfied == 0 and len(notInstalled) >= 1:
        import os
        os.system('cls' if os.name == "nt" else "clear")
        print("The following packages are missing:-\n---------------")
        for lib in notInstalled:
            print("- ", lib)
        print("---------------\nInstall them and try again.\n")


if __name__ == "__main__":
    main()

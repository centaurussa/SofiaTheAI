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


with open("requirements.txt", "r") as f:
    _satisfied = 1
    for index, lib in enumerate(f.readlines()):
        if index > 2:
            lib = lib.rstrip("\n")
            try:
                exec(f"import {lib.split('  #')[-1]}")
            except ImportError:
                whichLib = lib.split("  #")[0]
                print(f"A library called '{whichLib}' is missing.")
                _satisfied = 0
    if _satisfied == 1:
        main()

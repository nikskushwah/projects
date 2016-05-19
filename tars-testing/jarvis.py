import speech_recognition as sr
import os
from utilities import *
from weather import *
import time

# For Speech Recognition
recorder = sr.Recognizer()
microphone = sr.Microphone()

weather = Weather()
print(weather.get_current_forcast())
print(weather.get_tomorrow_forcast())


try:
    # Configuring Speech
    with microphone as source: recorder.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(recorder.energy_threshold))
    recorder.non_speaking_duration = 0.3
    recorder.pause_threshold = 0.4

    while True:
        print("Say something!")
        with microphone as source: audio = recorder.listen(source)
        print("Got it! Now to recognize it...")
        try:
            text = recorder.text(audio).lower()
            print(u"You said {}".format(text).encode("utf-8"))

            if asking_for_joke(text):
                tell_joke()
                continue
            if asking_for_open(text):
                open_app(text)
                continue
            if asking_for_site(text):
                open_site(text)
                continue
            if asking_for_tab(text):
                if text == "open tab":
                    open_new_tab(driver)
                continue

            if closing_tab(text):
                if text == "close tab":
                    closeTab(driver)

                
                continue

            if open_new_window(text):
                if text == "start window":
                    openNewWindow(driver)
                continue

            if closing_window(text):
                if text == "close window":
                    closeWindow(driver)
                continue

            if reload_page(text):
                if text == "reload page":
                    reloadPage(driver)
                continue

            if reopen_tab(text):
                if text == "reopen tab":
                    reOpenTab(driver)
                continue

            if go_back(text):
                if text == "go back":
                    goBack(driver)
                continue

            if go_forward(text):
                if text == "go forward":
                    goForward(driver)
                continue

            if switch_tab(text):
                if text == "switch tab":
                    switchTab(driver)
                continue

            if scroll_down(text):
                if text == "scroll down":
                    scrollDown(driver)
                continue

            if scroll_up(text):
                if text == "scroll up":
                    scrollUp(driver)
                continue

            







            if asking_for_folder(text):
                open_folder(text)
                continue
            if play_song(text):
                play_local_song(text)
                continue
            if pause_song(text):
                pause_local_song()
                continue
            if asking_for_tomorrow_weather(text):
                speak(weather.get_tomorrow_forcast())
                continue
            if asking_for_current_weather(text):
                speak(weather.get_current_forcast())
                continue
            if asking_for_search(text):
                search(text)
                continue
            if asking_for_song(text):
                play_youtube(text)
            if re.search(re.compile("Goodbye Jarvis"), text):
                speak("Goodbye")
                break

            if re.search(re.compile("ssh16b"), text):
                os.system("osascript -e 'tell application \"Terminal\" to activate' -e 'tell application \"System Events\" to tell process \"Terminal\" to keystroke \"n\" using command down' -e 'tell application \"Terminal\" to do script \"ssh16b\" in selected tab of the front window'")

            check = re.search(re.compile("^haha(.+)"), text)
            if check:
                speak("haaahahahaahahahahhahahaaaaaaaaaaa")
            check = re.search(re.compile("laugh"), text)
            if check:
                speak("teheheeeheeeheeeheeheeheeeheeee")
        except sr.UnknownValueError:
            print("Oops! Didnt catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass

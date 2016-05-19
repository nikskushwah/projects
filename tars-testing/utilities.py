import pyglet
import os
import re
import random
import webbrowser
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ERROR = 256


driver = webdriver.Firefox()
scrollDownVar=0
scrollUpVar=0

def speak(text):
    cmd = 'say -v "Samantha" "' + text + '"'
    print(cmd)
    text_speak = "opening" + text

    os.system("espeak " + text_speak)

def play(file):
    pyglet.resource.media(file).play()

def asking_for_tomorrow_weather(text):
    return re.search(re.compile("(.+)weather tomorrow"), text) or re.search(re.compile("(.+)weather like tomorrow"), text)

def asking_for_current_weather(text):
    return re.search(re.compile("(.+)weather (.+)"), text)

def asking_for_open(text):
    return re.search(re.compile("^open (.+)"), text)

def asking_for_site(text):
    return re.search(re.compile("^browser (.+)"), text)

def asking_for_search(text):
    return re.search(re.compile("^search (.+)"), text)

def asking_for_joke(text):
    return re.search(re.compile("tell me a joke"), text)

def asking_for_song(text):
    return re.search(re.compile("youtube song (.+)"), text)

def pause_song(text):
    return re.search(re.compile("pause(.+)"), text)

def pause_local_song(text):
    os.system("rhythmbox-client --pause " +" "+text)

def asking_for_folder(text):
    return re.search(re.compile("folder (.+)"), text)

def asking_for_tab(text):
    return re.search(re.compile("open(.+)"), text)




def open_new_tab(driver):
    
    

    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')


def open_app(text):
    term = re.search(re.compile("^open (.+)"), text).group(1)
    speak(term)
    cmd = os.system("'" + term + "'")
    if cmd == ERROR:
        term_speak = term.title()
        os.system("nautilus " + term_speak)

def open_folder(text):
    
    
    speak(text)
    term_final = text.split(' ', 1)[1]
    term_speak = term_final.title()
    print(term_speak)
    
    cmd = os.system("cd && nautilus " + term_speak)


def open_site(text):
    term = re.search(re.compile("^browser (.+)"), text).group(1)
    speak(term)
    os.system("firefox http://" + term + ".com")





def search(text):
    terms = re.search(re.compile("^search (.+)"), text).group(1).split()
    speak("Searching " + " ".join(terms))
    os.system("firefox http://google.com/search?q=" + "+".join(terms))

def tell_joke():
    jokes = ["How do you kill vegetarian vampires? With a steak to the heart.",
    "So this guy with a premature ejaculation problem comes out of nowhere.",
    "What kind of shoes do ninjas wear? Sneakers. Hahahaha",
    "How come bikes cannot stand on their own? Because they are two tired.",
    "Last night I almost had a threesome. but I only needed two more people",
    "When you get a bladder infection, urine trouble.",
    "You want to hear a pizza joke? Never mind, it is pretty cheesy."]
    speak(random.choice(jokes))

def play_youtube(text):
    terms = re.search(re.compile("youtube song (.+)"), text).group(1).split()
    speak("Playing " + " ".join(terms) + " on youtube.")
    terms.append("youtube")
    controller = webbrowser.get()
    controller.open("http://google.com/search?q=" + "+".join(terms) + "&btnI")

def play_song(text):
    return re.search(re.compile("play (.+)"), text)

def play_local_song(text):
    os.system("rhythmbox-client --play " + text)


def closing_tab(text):
    return re.search(re.compile("close (.+)"), text)

def closeTab(driver):
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

def open_new_window(text):
    return re.search(re.compile("start(.+)"), text)

def openNewWindow(driver):
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'N')

def closing_window(text):
    return re.search(re.compile("close(.+)"), text)

def closeWindow(driver):
    driver.find_element_by_tag_name('body').send_keys(Keys.LEFT_ALT + Keys.F4);


def reload_page(text):
    return re.search(re.compile("reload(.+)"), text)

def reloadPage(driver):
    driver.find_element_by_tag_name('body').send_keys(Keys.F5)

def reopen_tab(text):
    return re.search(re.compile("reopen(.+)"), text)

def reOpenTab(driver):
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.SHIFT +'t')

def openFacebook(driver):
    driver.get("http://www.facebook.com")

def openYoutube(driver):
    driver.get("http://www.youtube.com")

def searchYoutube(driver, query):
    driver.get("http://www.youtube.com")
    searchbox=driver.find_element_by_id("masthead-search-term").send_keys(query)
    searchbutton=driver.find_element_by_id("search-btn")
    searchbutton.click()


def go_back(text):
    return re.search(re.compile("go(.+)"), text)

def goBack(driver):
    driver.back()

def go_forward(text):
    return re.search(re.compile("go(.+)"), text)

def goForward(driver):
    driver.forward()




def searchGoogle(driver, query):
    driver.get("http://www.google.com")
    searchbox=driver.find_element_by_id("lst-ib").send_keys(query)
    searchbutton=driver.find_element_by_name("btnG")
    print(searchbutton)
    searchbutton.click()

def searchGoogleImages(driver, query):
    driver.get("http://images.google.com")
    searchbox=driver.find_element_by_id("lst-ib").send_keys(query)
    searchbutton=driver.find_element_by_name("btnG")
    searchbutton.click()

def switch_tab(text):
    return re.search(re.compile("switch (.+)"), text)   

def switchTab(driver):
    driver.find_element_by_tag_name('body').send_keys(Keys.LEFT_CONTROL + Keys.TAB)

def scroll_down(text):
    return re.search(re.compile("scroll(.+)"), text)

def scrollDown(driver):
    global scrollDownVar
    down=scrollDownVar+200
    driver.execute_script("window.scrollTo(0, {0});" . format(down))
    scrollDownVar=scrollDownVar+200

def scroll_up(text):
    return re.search(re.compile("scroll(.+)"), text)

def scrollUp(driver):
    global scrollUpVar
    up=scrollUpVar+200
    driver.execute_script("window.scrollTo({0}, 0);" . format(up))
    scrollUpVar=scrollUpVar+200

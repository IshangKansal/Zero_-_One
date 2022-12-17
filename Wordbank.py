from time import *
from Display import *
from art import *
from colorama import Fore, Back, Style, init
from threading import *
from pynput.keyboard import Key, Controller


def f():
    keyboard = Controller()
    sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

# Print the easy mode pattern -----------------------
def menu():
    init()
    f_t = Thread(target=f)
    f_t.start()
    x = input(Fore.GREEN)
    tprint("Easy Mode")
    print()

# Print the medium mode pattern ------------------
def menu2():
    init()
    f_t = Thread(target=f)
    f_t.start()
    x = input(Fore.YELLOW)
    tprint("Medium Mode")
    print()

# Print the hard mode pattern -----------------------
def menu3():
    init()
    f_t = Thread(target=f)
    f_t.start()
    x = input(Fore.LIGHTRED_EX)
    tprint("Hell Mode")
    print()


# This function take easy words from wordbankeasy file -------------------------------
def sel(x):
    L = []
    string = ""
    import random

    for i in range(x):
        f = open("Wordbank_Easy.txt", 'r')
        y = random.choice(f.readlines())
        L.append(y)
        f.close()
    for j in L:
        string += j[:-1] + " "
    return string


# This function take medium words from wordbankmedium file ------------------------------
def sel1(x):
    L = []
    string = ""
    import random

    for i in range(x):
        f = open("Wordbank_Medium.txt", 'r')
        y = random.choice(f.readlines())
        L.append(y)
        f.close()
    for j in L:
        string += j[:-1] + " "
    return string


# This function take hard words from wordbankhard file ----------------------------
def sel2(x):
    L = []
    string = ""
    import random

    for i in range(x):
        f = open("Wordbank_Hard.txt", 'r')
        y = random.choice(f.readlines())
        L.append(y)
        f.close()
    for j in L:
        string += j[:-1] + " "
    return string

# This function picks up paragraph to be typed ----------------------
def sel3():
    import random
    f = open("Wordbank_Time.txt", 'r')
    string = random.choice(f.readlines())
    f.close()
    return string
from time import *
from Display import *
from art import *
def menu():
    tprint("Easy Mode")
    print()


def menu2():
    tprint("Medium Mode")
    print()


def menu3():
    tprint("Hard Mode")
    print()



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
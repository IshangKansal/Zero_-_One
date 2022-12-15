from time import *
import os
def menu():
    print("========== Menu ==========")
    print("1 : 10 Words")
    print("2 : 25 Words")
    print("3 : 50 Words")
    print("4 : 100 Words")
    print()


def menu2():
    print("Medium Menu")
    print()


def menu3():
    print("Hard menu")
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
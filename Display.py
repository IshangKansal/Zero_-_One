from time import *
import os


def dis():
    l = "Welcome to Zero_&_One's Typing Test"
    l1 = ""
    for i in range(len(l)):
        os.system("cls" if os.name == "nt" else "clear")
        l1 += l[i]
        print(l1)
        sleep(0.15)
    for i in range(5):
        os.system("cls" if os.name == "nt" else "clear")
        print(l1)
        sleep(0.15)
    os.system("cls" if os.name == "nt" else "clear")


def countdown():
    l = ["5", "4", "3", "2", "Start Typing!"]
    l1 = ""
    print("Test will start in 5 seconds.\n")
    sleep(1)
    for i in range(len(l)):
        l1 = l[i]
        print(l1)
        sleep(1)
        print("\033[A                              \033[A")
    print("\033[A                              \033[A")
    print("\033[A                              \033[A")
    print("Your sentence: ")




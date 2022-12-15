import os
from time import *
from Display import *
from Wordbank import *


def Mistakes(a, b):
    errors = 0
    for i in range(len(a)):
        try:
            if a[i] != b[i]:
                errors += 1
        except:
            errors += 1
    return (errors/len(a))*100


def wpm(c, d, e):
    tt = d - c
    tr = round(tt, 2)
    sp = (e*60)/tr
    return round(sp)


def speed():
    dis()
    print("Welcome to Zero_&_One's Typing Test")
    f1 = input("\nPress ENTER to start")
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("""Choose your Mode:

1. Easy - Simple words but input is Case-Sensitive
2. Medium - Words with symbols and numbers, to test your speed on whole keyboard
3. Hell - Try it if you want, although i don't think you will finish it""")
        y1 = input("\nEnter difficulty level(E/M/H): ")
        if y1.upper() == "E":
            print("Easy, I see, All The Best!")
            sleep(2)
            os.system("cls||clear")
            menu()
        elif y1.upper() == "M":
            print("Pushing Limits i see, All the Best!")
            sleep(2)
            os.system("cls||clear")
            menu2()
        elif y1.upper() == "H":
            print("Well, Bravo for choosing this even after my warning.")
            sleep(2)
            print("Welcome to Hell!!")
            sleep(2)
            os.system("cls||clear")
            menu3()
        user_input = int(input("\nEnter No. of words you want to test your skills on: "))
        os.system("cls||clear")
        if y1.upper() == "E":
            t = sel(user_input)
        elif y1.upper() == "M":
            t = sel1(user_input)
        elif y1.upper() == "H":
            t = sel2(user_input)
        t3 = t.split()
        t4 = len(t3)
        print(f"\nYour sentence to write is: \n\n{t}\n")
        countdown()
        t1 = time()
        y = input("\n").split()
        t2 = time()
        z1 = Mistakes(t3, y)
        z2 = wpm(t1,t2,len(y))
        print("\nSpeed: " + str(z2) + " WPM")
        print("Accuracy: " + str(100-z1) + " %")
        f = input("Do you want to continue(Y/N): ")
        if f.upper() == "N":
            print("\nSee Ya!\n")
            sleep(5)
            break
        elif f.upper() == "Y":
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print("I take that as a YES")
            sleep(3)
            os.system("cls" if os.name == "nt" else "clear")


speed()

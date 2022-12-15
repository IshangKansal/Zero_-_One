import os
from time import *
from Display import *
from Wordbank import *
from test1 import *


def Mistakes(a, b):
    errors = 0
    for i in range(len(a)):
        try:
            if a[i] != b[i]:
                errors += 1
        except:
            errors += 1
    return (errors/len(a))*100


def Mistakes1(a, b):
    errors = 0
    for i in range(len(b)):
        try:
            if a[i] != b[i]:
                errors += 1
        except:
            errors += 1
    z1 = 100 - (errors/len(b))*100
    print("Accuracy: " + str(z1) + " %")
    print("Correct words: "+str(len(b)-errors))
    print("Wrong words: "+ str(errors))


def wpm(c, d, e):
    tt = d - c
    tr = round(tt, 2)
    sp = (e*60)/tr
    return round(sp)


def speed():
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
        print("Your Sentence: \n")
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


def speed1():
    while True:
        print("""Choose your Mode

1. 30 seconds
2. 60 seconds
3. 120 seconds""")
        a1 = int(input("\nEnter your choice(1-3): "))
        os.system("cls||clear")
        if a1 == 1:
            t = 30
        elif a1 == 2:
            t = 60
        elif a1 == 3:
            t = 120
        t1 = sel(150)
        t2 = t1.split()
        t3 = len(t2)
        print(f"\nYour sentence to write is: \n\n{t1}\n")
        countdown()
        t4 = time()
        y1 = cd1(t)
        y = y1.cd()
        t5 = time()
        z2 = wpm(t4,t5,len(y))
        print("\nSpeed: " + str(z2) + " WPM")
        z1 = Mistakes1(t2, y)
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
    

dis()
print("Welcome to Zero_&_One's Typing Test")
f1 = input("""\nHow do you want to Test:
1. By Time
2. By Words
Enter your choice(1-2): """)
os.system("cls" if os.name == "nt" else "clear")
if f1 == "2":
    speed()
elif f1 == "1":
    speed1()

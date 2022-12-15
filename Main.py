import os
from time import *
from Display import *
from Wordbank import *
from test1 import *


def Mistakes_Word(a, b):
    errors = 0
    for i in range(len(a)):
        try:
            if a[i] != b[i]:
                errors += 1
        except:
            errors += 1
    return (errors/len(a))*100


def Mistakes_Time(a, b):
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


def Speed_word():
    while True:
        y2 = words("a",1)
        y2.preinput()
        y1 = input("\nEnter difficulty level: ")
        y2 = words(y1,1)
        y2.postinput()
        user_input = int(input("\nEnter No. of words you want to test your skills on: "))
        os.system("cls||clear")
        y2 = words(y1,user_input)
        t = y2.postsel()
        t3 = t.split()
        print(f"\nYour sentence to write is: \n\n{t}\n")
        countdown()
        print("Your Sentence: \n")
        t1 = time()
        y = input("\n").split()
        t2 = time()
        z1 = Mistakes_Word(t3, y)
        z2 = wpm(t1,t2,len(y))
        print("\nSpeed: " + str(z2) + " WPM")
        print("Accuracy: " + str(100-z1) + " %")
        f = input("Do you want to continue(Y/N): ")
        f1 = continue_loop(f)
        f1.condition_check()


def Speed_time():
    while True:
        a2 = times(1)
        a2.preinput()
        a1 = int(input("\nEnter your choice: "))
        os.system("cls||clear")
        a2 = times(a1)
        t = a2.postinput()
        t1 = sel(150)
        t2 = t1.split()
        print(f"\nYour sentence to write is: \n\n{t1}\n")
        countdown()
        t4 = time()
        y1 = cd1(t)
        y = y1.cd()
        t5 = time()
        z2 = wpm(t4,t5,len(y))
        print("\nSpeed: " + str(z2) + " WPM")
        z1 = Mistakes_Time(t2, y)
        f = input("Do you want to continue(Y/N): ")
        f1 = continue_loop(f)
        f1.condition_check()
    

dis()
sleep(0.75)
tprint("Zero_&_One's Typing Test")
f1 = input("""\nHow do you want to Test:
1. By Time
2. By Words
Enter your choice(1-2): """)
os.system("cls" if os.name == "nt" else "clear")
if f1 == "2":
    Speed_word()
elif f1 == "1":
    Speed_time()

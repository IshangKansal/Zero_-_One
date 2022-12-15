from time import *
from Wordbank import *
import os

class words():
    def __init__(self,y1,user_input):
        self.y1 = y1
        self.ui = user_input
    
    def preinput(self):
        print("""Choose your Mode:

1. Easy - Simple words but input is Case-Sensitive
2. Medium - Words with symbols and numbers, to test your speed on whole keyboard
3. Hell - Try it if you want, although i don't think you will finish it""")

    def postinput(self):
        if self.y1.upper() == "E" or self.y1 == "1":
            print("Easy, I see, All The Best!")
            sleep(2)
            os.system("cls||clear")
            menu()
        elif self.y1.upper() == "M" or self.y1 == "2":
            print("Pushing Limits i see, All the Best!")
            sleep(2)
            os.system("cls||clear")
            menu2()
        elif self.y1.upper() == "H" or self.y1 == "3":
            print("Well, Bravo for choosing this even after my warning.")
            sleep(2)
            print("Welcome to Hell!!")
            sleep(2)
            os.system("cls||clear")
            menu3()

    
    def postsel(self):
        if self.y1.upper() == "E":
            return sel(self.ui)
        elif self.y1.upper() == "M":
            return sel1(self.ui)
        elif self.y1.upper() == "H":
            return sel2(self.ui)


class times():
    def __init__(self,a1):
        self.a1 = a1

    def preinput(self):
        print("""Choose your Mode

1. 30 seconds
2. 60 seconds
3. 120 seconds""")

    def postinput(self):
        if self.a1 == 1 or self.a1 == 30:
            return 30
        elif self.a1 == 2 or self.a1 == 60:
            return 60
        elif self.a1 == 3 or self.a1 == 120:
            return 120


class continue_loop():
    def __init__(self,f):
        self.f = f
    
    def condition_check(self):
        if self.f.upper() == "N":
            print("\nSee Ya!\n")
            sleep(5)
            quit()
        elif self.f.upper() == "Y":
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print("I take that as a YES")
            sleep(3)
            os.system("cls" if os.name == "nt" else "clear")


        

def dis():
    l = "Welcome to Zero_&_One's Typing Test"
    l1 = ""
    for i in range(len(l)):
        os.system("cls" if os.name == "nt" else "clear")
        l1 += l[i]
        print(l1)
        sleep(0.075)
    for i in range(5):
        os.system("cls" if os.name == "nt" else "clear")
        print(l1)
        sleep(0.075)
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

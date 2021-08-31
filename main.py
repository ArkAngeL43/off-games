
import turtle
import time
import os
import sys 
from sys import platform  
import random
import datetime 
from datetime import datetime 
import colorama 
import subprocess
from colorama import Fore 
from colorama import init 
import pynput
from pynput.keyboard import Key, Listener
#str


# game time 
startTime = datetime.now()


def dev():
    if sys.platform == 'win32':
        time.sleep(1)
        print("                              |your system is            |")
        print("----V1.0 YAY!-------          |windows :(                |")
        print("                              | options arent avalible   |")
        print("                              |for this sys yet          |")
        print("                              |unless you have gnome term|")
        if sys.platform == 'win64':
            print("                              |your system is            |")
            print("----V1.0 YAY!-------          |windows :(                |")
            print("                              | options arent avalible   |")
            print("                              |for this sys yet          |")
            print("                              |unless you have gnome term|")
            if sys.platform == 'linux1':
                time.sleep(1)
                print("                              |your system is.....    |")
                print("----V1.0 YAY!-------          |windows LINUX YAY      |")
                print("                              | Commands are supported|")
                if sys.platform == 'linux2':
                    time.sleep(1)
                    print("                              |your system is.....    |")
                    print("----V1.0 YAY!-------          |windows LINUX YAY      |")
                    print("                              | Commands are supported|") # check system name 
                    dev()

def CS(X): # change cs's clear command pending system for compatibility 
    import os 
    clear()
    time.sleep(X)
    if sys.platform == 'linux':
        os.system('clear')
    if sys.platform == 'win32':
        os.system('cls') 

def clear():
    if sys.platform == 'win32':
        CS()
        if sys.platform == 'darwin':
            CS()
            os.system('clear')
            if sys.platform == 'win64':
                CS()
                os.system('cls')
                if sys.platform == 'linux1':
                    CS()
                    os.system('clear')
                    if sys.platform == 'linux2':
                        CS()
                        time.sleep()
                        os.system('clear')
                        if sys.platform == 'linux':
                            CS(X)
                            time.sleep(1)
                            os.system('clear') # clear sleep func 

def banner(): # pretify using colorama 
    print(Fore.MAGENTA+"""
  ___  _____ _____      ____    _    __  __ _____ ____  
 / _ \|  ___|  ___|    / ___|  / \  |  \/  | ____/ ___| 
| | | | |_  | |_ _____| |  _  / _ \ | |\/| |  _| \___ \ 
| |_| |  _| |  _|_____| |_| |/ ___ \| |  | | |___ ___) |
 \___/|_|   |_|        \____/_/   \_\_|  |_|_____|____/ 
                                                        

    """)

banner()
print(Fore.WHITE+"-------------FIRST QUESTIONS---------------------|")
print("|what would you like to run in a second terminal |")
print("|------------------------------------------------|")
print(Fore.BLUE+"|[1] ==> Live Game Time [2] ==> Game Keylogger   |")
print("|[3] ==> None           [4] ==> Both             |")
print("|[00] ==> Run tetris and both                    |")
print("|[tet] ==> Just run tetris ")
print("|________________________________________________|")
dev()

options = str(input(" Options ==> "))

time.sleep(1)

if options == 'dev': #test 
    time.sleep(1)
    print("-------------------------------------------------------------------")
    print(" now navigate to the new terminal windows and enter your username! ")
    print(" these windows will appear in 10 seconds, these are game logs of   ")
    print(" you're gameplay, time, game time, and keyes, enjoy!!!!            ")
    print("-------------------------------------------------------------------")
    print("|")
    print("|")
    print(" Note ==> when you are done you can control c out of them they exit ")
    print(" automatically ")
    time.sleep(10)
    os.system('gnome-terminal --tab -- python3 time.py ') # call gnome-terminal in a new tab 
    os.system('gnome-terminal --tab -- python3 log.py ')

# using elif, if, and == 

if options == '1':
    print(" [*] spawning xterm shell [*] ")
    print(" [*] this will be glitchy [*]")
    os.system('gnome-terminal --tab -- python3 time.py')

elif options == '00':
    print(" [!] Spawning shells [!] ")
    os.system('gnome-terminal --tab -- python3 tetris.py && gnome-terminal --tab -- python3 time.py && gnome-terminal --tab -- python3 log.py ')

elif options == 'tet':
    print(" [!] spawning secondary shell [!] ")
    print(" [!] this menu will stay open [!] ")
    print(" [!] tetris is a GUI and will start auto [!] ")
    time.sleep(5)
    os.system('gnome-terminal --tab -- python3 tetris.py ')

elif options == '2':
    time.sleep(1)
    print(" [*] spawning xterm shell [*] ")
    print(" [*] this will be glitchy [*]")
    os.system('gnome-terminal --tab -- python3 log.py') # spawn termina, 

# spawn term in a new tab, this will be able 
# to create more organization 
# in case user uses 1 screen or on laptop 

elif options == '3':
    print(" [+] sure, continuing have fun! ")

elif '4' in options:
    time.sleep(1)
    print(" [*] spawinging shell's [+] ")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    os.system('gnome-terminal --tab -- python3 time.py && gnome-terminal --tab -- python3 log.py ')
    print(" have fun!!!!!!!!!!!")

#os.system(' chmod +x ./spawn.sh && ./spawn.sh')

u1 = str(input(" Whats the chosen username => "))
#game title/banner stats 
delay = 0.1
score = 0
high_score = 0
date = str(datetime.now())
sore_beat = 10000


wn = turtle.Screen()
wn.title("Snake Game by ArkAngeL43")
wn.bgpic("2.png")
wn.bgcolor("black")
wn.setup(width=1000, height=1000)
wn.tracer(0) #
# character
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

# foodie 
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("Blue")
food.penup()
food.goto(0,100)
segments = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(155, 435)
pen.write("Date => {}".format(date), align="center", font=("Courier", 24, "normal"))
pen.goto(0, 260)
pen.write("Score => 0  High Score => 0", align="center", font=("Courier", 24, "normal"))

#
# directions 

def clear():
    os.system(' clear ')
    print(" [*] Have a nice day [*] ==> ", f"{u1}")
    print("------------time Defualt-------------")
    print(datetime.now() - startTime)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# controls 
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
########## ARROW KEY SUPPORT #######
wn.onkeypress(go_up, "Up",)
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

while True:
    wn.update()
    pen.goto(220, 220)
    pen.write("boarder")
    if head.xcor()>220 or head.xcor()<-220 or head.ycor()>220 or head.ycor()<-220: # if the body touches body then break 
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
    
        segments.clear()
        # reset the score
        score = 0
        # reset the delay
        delay = 0.1
        pen.clear()
        pen.goto(155, 435)
        pen.write("Date => {}".format(date), align="center", font=("Courier", 24, "normal"))
        pen.goto(0, 260)
        pen.write("Score => {}  High Score => {}".format(score, high_score, sore_beat), align="center", font=("Courier", 24, "normal")) 

    if head.distance(food) < 20:
        x = random.randint(-190, 190)
        y = random.randint(-190, 190) # keep food within the box 
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    #head segs
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            for segment in segments:
                segment.goto(1000, 1000)
        
            segments.clear()
            # Reset the score
            score = 0
            # Reset the delay
            delay = 0.1
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score, sore_beat), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
    clear()

wn.mainloop()


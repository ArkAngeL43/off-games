import time
import datetime 
from datetime import datetime 
import colorama 
from colorama import init 
# keylogger using pynput module
   
import pynput
from pynput.keyboard import Key, Listener

init()

A = str(input(" Player Username ===> "))

# keylogger for function base and player data in game to show datetime player pressed current key, log as well as.txt hhhhhhhhhhhhhhhhhhhhhhhhhbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

def logger():
    keys = []

    def on_press(key):
        
        keys.append(key)
        write_file(keys)
        
        try:
            print('\033[34m [DATA] ====>  [KEY PRESS BY] ====>  \033[36m'f'[{A}]', ' \033[35m [AT] ===> ' + str(datetime.now()))
            #print('alphanumeric key {0} pressed by User ===> '.format(key.char))
            
        except AttributeError:
            print('\033[34m [DATA] ====> [KEY PRESS BY] ====> 'f'[{A}]', '[AT] ===> ' + str(datetime.now()))
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

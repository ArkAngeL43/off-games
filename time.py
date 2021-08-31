import os 
import time 
import datetime
from datetime import datetime
import sys 
import colorama 

A = str(input(" Username ===> "))

def banner():
    print(Fore.BLUE+"""
  ___  _____ _____      ____    _    __  __ _____ ____  
 / _ \|  ___|  ___|    / ___|  / \  |  \/  | ____/ ___| 
| | | | |_  | |_ _____| |  _  / _ \ | |\/| |  _| \___ \ 
| |_| |  _| |  _|_____| |_| |/ ___ \| |  | | |___ ___) |
 \___/|_|   |_|        \____/_/   \_\_|  |_|_____|____/ 
    """)

def live_time():
    while True:
        print('\033[34m [DATA] ===> \033[36m [USER] ===> ' f'{A}')
        print('\033[34m [DATA] ===> \033[36m [GAME TIME] ===> ' + str(datetime.now()))

#banner() could not spawn banner command since xterm closed 
live_time()

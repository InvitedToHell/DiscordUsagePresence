import os
import psutil
from pypresence import Presence
import time
import GPUtil
import numpy as np
import pyautogui as pag
from time import sleep
import os
os.system("cls")
client_id = '896723850782461964'
RPC = Presence(client_id,pipe=0)
RPC.connect()

COLORS = {\
"magenta":"\u001b[35m",
}

def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

while True: 
    r = """ [[magenta]] █    ██  ██████  ▄▄▄        ▄████ ▓█████  ██▓███   ██▀███  ▓█████   ██████ ▓█████ ███▄    █  ▄████▄ ▓█████ 
 ██  ▓██▒██    ▒ ▒████▄     ██▒ ▀█▒▓█   ▀ ▓██░  ██▒▓██ ▒ ██▒▓█   ▀ ▒██    ▒ ▓█   ▀ ██ ▀█   █ ▒██▀ ▀█ ▓█   ▀ 
▓██  ▒██░ ▓██▄   ▒██  ▀█▄  ▒██░▄▄▄░▒███   ▓██░ ██▓▒▓██ ░▄█ ▒▒███   ░ ▓██▄   ▒███  ▓██  ▀█ ██▒▒▓█    ▄▒███   
▓▓█  ░██░ ▒   ██▒░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄ ▒██▄█▓▒ ▒▒██▀▀█▄  ▒▓█  ▄   ▒   ██▒▒▓█  ▄▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▓█  ▄ 
▒▒█████▓▒██████▒▒ ▓█   ▓██▒░▒▓███▀▒░▒████▒▒██▒ ░  ░░██▓ ▒██▒░▒████▒▒██████▒▒░▒████▒██░   ▓██░▒ ▓███▀ ░▒████▒
░▒▓▒ ▒ ▒▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░▒▓▒░ ░  ░░ ▒▓ ░▒▓░░░ ▒░ ░▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░ ▒░ ░
░░▒░ ░ ░░ ░▒  ░ ░  ▒   ▒▒ ░  ░   ░  ░ ░  ░░▒ ░       ░▒ ░ ▒░ ░ ░  ░░ ░▒  ░ ░ ░ ░  ░ ░░   ░ ▒░  ░  ▒   ░ ░  ░
 ░░░ ░ ░░  ░  ░    ░   ▒   ░ ░   ░    ░   ░░         ░░   ░    ░   ░  ░  ░     ░     ░   ░ ░ ░          ░   
   ░          ░        ░  ░      ░    ░  ░            ░        ░  ░      ░     ░  ░        ░ ░ ░        ░  ░
                                                                                             ░              y"""

    print(colorText(r))
    t0 = '[[magenta]]Starting... y/n\n'
    query = input(colorText(t0)) 
    Fl = query[0].lower() 
    if query == '' or not Fl in ['y','n']: 
       t1 = "[[magenta]]Please answer with yes or no!"
       print(colorText(t1))
    else: 
       break 

if Fl == 'y': 
    clear = lambda: os.system('cls')
    clear()
    t2 = f"[[magenta]]Started successfully.\nPress CNTRL + C to stop."
    print(colorText(t2))
    FILE_NAME = './sound.wav'  
    wave_length = 4 
    sample_rate = 16_000  
    while True:
        print(RPC.update(
                details=f"CPU: {str(psutil.cpu_percent())}% | RAM: {str(psutil.virtual_memory().percent)}% | OS: Windows 10",
                large_image="https://i.imgur.com/CVje3Zw.gif", large_text="gif",
                buttons=[{
                    "label": "cool video",
                    "url": "https://www.youtube.com/watch?v=iik25wqIuFo"}
                    ]
            )) 
        time.sleep(1)

if Fl == 'n': 
    quit()
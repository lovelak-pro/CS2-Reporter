import pyautogui as py
from colorama import Fore,Style
from time import sleep
import os

# Text Colors
_Y = Fore.YELLOW
_C = Fore.CYAN
_R = Fore.RED

# All Buttons X,Y Pos
reportX = 1377
CTreportY = [405,432,456,483,508]
TreportY = [665,690,715,742,769]
BWalls = 1180,505
BAim = 1180,560
Bsubmit = 1161,696

# Click Delay
delay = 0.3

while True:
    os.system('cls')
    os.system('title Reporter Them Bitches!')
    logo = f'''
\t{_R} ██████╗███████╗██████╗     {_C}██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗███████╗██████╗ 
\t{_R}██╔════╝██╔════╝╚════██╗    {_C}██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
\t{_R}██║     ███████╗ █████╔╝    {_C}██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   █████╗  ██████╔╝
\t{_R}██║     ╚════██║██╔═══╝     {_C}██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   ██╔══╝  ██╔══██╗
\t{_R}╚██████╗███████║███████╗    {_C}██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║
\t{_R} ╚═════╝╚══════╝╚══════╝    {_C}╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                                                                                            
'''
    print(logo)
    print(f'''{Fore.RED}{Style.BRIGHT}\n\tNOTE :{_Y} THIS ONLY WORK ON 1920x1080 FULLSCREEN WINDOWED
             {_R}!{_Y} ONLY WORK IN {_R}({_Y}COMPETITIVE{_R}){_Y} GAMEMODE FOR NOW
             {_R}!{_Y} ONLY WORK ON ENEMY TEAM{_R}/{_Y}PLAYERS FOR NOW...
             {_R}!{_Y} Made by Lovelak''')
                        
    print(f'{_Y}\n\tWhich Team : {_C}CT{_Y} or {_C}T{_Y}')
    print(f'\tJust type : {_C}1{_Y} for {_C}CT{_Y} or {_C}2{_Y} for {_C}T{_Y}')
    team = input(f'\t{Fore.RED}Which Team to report ? : ')
    print(f'\n\t{_C}[1]{_Y} 1st player  {_C}[2]{_Y} 2nd player {_C}[3]{_Y} 3rd player {_C}[4]{_Y} 4th player {_C}[5]{_Y} 5th player ')
    print(f'\n\tJust type : {_C}1, 2, 3, 4{_Y} or {_C}5{_Y}')
    player = int(input(f'\t{Fore.RED}Which Player to report ? : '))
    print(f'\n\t{_C}[1]{_Y} For WallHacks {_C}[2]{_Y} For AimHacks')
    print(f'\n\tJust type : {_C}1{_Y} or {_C}2{_Y}')
    whatkind = input(f'\t{Fore.RED}What type of cheat ? : ')
    print(f'\n\t{_Y}Just enter a number from {_C}1{_Y} to {_C}9,999,999,999,999{_Y}')
    amount = int(input(f'\t{Fore.RED}How many reports ? : '))
    
    sleep(3)
    if team == '1':
        if  whatkind == '1':
            for x in range(amount):
                py.click(reportX,CTreportY[player-1])
                sleep(delay)
                py.click(BWalls)
                sleep(delay)
                py.click(Bsubmit)
                sleep(delay)

        elif whatkind == '2' and team == '1':
            for x in range(amount):
                py.click(reportX,CTreportY[player-1])
                sleep(delay)
                py.click(BAim)
                sleep(delay)
                py.click(Bsubmit)
                sleep(delay)
        else:
            print('Something went wrong!')
    elif team == '2':
        if  whatkind == '1'  and team == '2':
            for x in range(amount):
                py.click(reportX,TreportY[player-1])
                sleep(delay)
                py.click(BWalls)
                sleep(delay)
                py.click(Bsubmit)
                sleep(delay)

        elif whatkind == '2'  and team == '2':
            for x in range(amount):
                py.click(reportX,TreportY[player-1])
                sleep(delay)
                py.click(BAim)
                sleep(delay)
                py.click(Bsubmit)
                sleep(delay)
        else:
            print('Something went wrong!')
    else:
        print('Something went wrong!')
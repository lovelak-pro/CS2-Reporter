import webview
from time import sleep
import os
from pyautogui import click,moveTo
from pymsgbox import confirm
from keyboard import is_pressed

# All Buttons X,Y Pos
reportX = 1377
CTreportY = [405,432,456,483,508]
TreportY = [665,690,715,742,769]

# Buttons for WallHacks
BWallsX,BWallsY = 1180,505

# Buttons for  AimHacks
BAimX,BAimY  = 1180,560

# Submit Button
BsubmitX,BsubmitY = 1161, 696

if not os.path.exists("C:\\Windows\\Temp\\dontshowagain.gay"):
    asd = confirm("This Tool Only Works On 1920x1080\nAndOnly 16:9 Aspect Ratio","CS2 Report Spammer",["OK","Don't Show Again"])
    if asd == "Don't Show Again":
        with open("C:\\Windows\\Temp\\dontshowagain.gay","w") as f:
            f.write("Delete this file if you're GAY!")

class APP():
    is_running = False
    def start(self,Team,Player,Whatkind,Speed,Amount):
        self.is_running = True
        Speed = int(Speed)/10
        if Team == "CT" and Whatkind == "aim":
            sleep(5)
            for x in range(int(Amount)):
                if self.is_running == False or is_pressed('f3'):
                    break
                else:
                    moveTo(reportX,CTreportY[int(Player)-1],duration=0.25)
                    click(reportX,CTreportY[int(Player)-1])
                    sleep(Speed)
                    moveTo(BAimX,BAimY,duration=0.25)
                    click(BAimX,BAimY)
                    sleep(Speed)
                    moveTo(BsubmitX,BsubmitY,duration=0.25)
                    click(BsubmitX,BsubmitY)
                    sleep(Speed)

        elif Team == "T" and Whatkind == "aim":
            sleep(5)
            for x in range(int(Amount)):
                if self.is_running == False or is_pressed('f3'):
                    break
                else:
                    moveTo(reportX,TreportY[int(Player)-1],duration=0.25)
                    click(reportX,TreportY[int(Player)-1])
                    sleep(Speed)
                    moveTo(BAimX,BAimY,duration=0.25)
                    click(BAimX,BAimY)
                    sleep(Speed)
                    moveTo(BsubmitX,BsubmitY,duration=0.25)
                    click(BsubmitX,BsubmitY)
                    sleep(Speed)

        elif Team == "CT" and Whatkind == "wall":
            sleep(5)
            for x in range(int(Amount)):
                if self.is_running == False or is_pressed('f3'):
                    break
                else:
                    moveTo(reportX,CTreportY[int(Player)-1],duration=0.25)
                    click(reportX,CTreportY[int(Player)-1])
                    sleep(Speed)
                    moveTo(BWallsX,BWallsY,duration=0.25)
                    click(BWallsX,BWallsY)
                    sleep(Speed)
                    moveTo(BsubmitX,BsubmitY,duration=0.25)
                    click(BsubmitX,BsubmitY)
                    sleep(Speed)

        elif Team == "T" and Whatkind == "wall":
            sleep(5)
            for x in range(int(Amount)):
                if self.is_running == False or is_pressed('f3'):
                    break
                else:
                    moveTo(reportX,TreportY[int(Player)-1],duration=0.25)
                    click(reportX,TreportY[int(Player)-1])
                    sleep(Speed)
                    moveTo(BWallsX,BWallsY,duration=0.25)
                    click(BWallsX,BWallsY)
                    sleep(Speed)
                    moveTo(BsubmitX,BsubmitY,duration=0.25)
                    click(BsubmitX,BsubmitY)
                    sleep(Speed)

        else:
            pass

    def stop(self):
        if self.is_running == True:
            self.is_running = False
        
if __name__ == "__main__":
    app = APP()
    webview.create_window('Cheaters Are GAY!',url='src/index.html',js_api=app,width=300,height=350,resizable=False)
    webview.start()
import webview
from time import sleep
import os
from pymsgbox import confirm
from keyboard import is_pressed
from pyautogui import click,moveTo


HTML = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>CS2 Reporter</title>
    <style>
      * {
        padding: 0%;
        margin: 0%;
      }
      body {
      background-color: white;
        text-align: center;
        font-family:
          "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
      }
      h2 span {
        color: red;
      }
      h2 {
        margin-top: 15px;
        font-weight: bolder;
        text-transform: uppercase;
      }
      select,
      input,
      button {
        box-shadow: 2px 2px rgb(255, 0, 0);
        width: 220px;
        background-color: transparent;
        outline: none;
        border: 1px black solid;
        border-radius: 0;
        padding: 0 5px;
        margin-top: 5px;
        height: 30px;
        transition: 0.5s;
        text-align: center;
      }
      select:hover,
      input:hover,
      button:hover {
        box-shadow: 3px 3px rgb(0, 0, 0);
      }
      #delaytime{
        margin: 5px 0 -3px 0;
      }
      #speed {
        -webkit-appearance: none;
        width: 210px;
        height: 15px;
        background: transparent;
        outline: none;
        opacity: 0.7;
        -webkit-transition: 0.2s;
        transition: opacity 0.2s;
      }

      #speed:hover {
        opacity: 1;
      }

      #speed::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 25px;
        height: 15px;
        background: #ff0c0c;
        cursor: pointer;
      }

      #speed::-moz-range-thumb {
        width: 25px;
        height: 25px;
        background: #04aa6d;
        cursor: pointer;
      }
      #amount {
        width: 210px;
      }
      #alert {
        margin-top: 10px;
        font-size: 16px;
      }
      #alert a {
        color: red;
      }
    </style>
  </head>
  <body>
    <h2><span>CS2</span> Report Spammer</h2>
    <select name="" id="team">
      <option value="none">Select Enemy Team</option>
      <option value="CT">CT - Counter Terrorist</option>
      <option value="T">T - Terrorist</option>
    </select>
    <br />
    <select id="player">
      <option value="none">Select Player Number</option>
      <option value="1">Player 1</option>
      <option value="2">Player 2</option>
      <option value="3">Player 3</option>
      <option value="4">Player 4</option>
      <option value="5">Player 5</option>
    </select>
    <br />
    <select id="whatkind">
      <option value="none">What Type Of Cheat?</option>
      <option value="wall">Wall Hacks</option>
      <option value="aim">Aim Hacks</option>
    </select>
    <br />
    <p id="delaytime"></p>
    <input type="range" onchange="update()" min="3" value="4" max="15" id="speed" />
    <br />
    <input type="number" placeholder="Enter Spam Amount..." id="amount" />
    <br />
    <button id="start" onclick="start()">Start</button>
    <p id="alert">
      Developed By <a href="https://lovelak.rf.gd" target="_blank">Lovelak</a>
    </p>

    <script>
      const Team = document.getElementById("team");
      const Player = document.getElementById("player");
      const Whatkind = document.getElementById("whatkind");
      const DelayTime = document.getElementById('delaytime');
      const Speed = document.getElementById("speed");
      const Amount = document.getElementById("amount");
      const Alert = document.getElementById("alert");
      const Start = document.getElementById("start");
      
      DelayTime.innerHTML = 'Delay Between Clicks is 0.'+Speed.value+'s';        
      function update() {
      DelayTime.innerHTML = 'Delay Between Clicks is 0.'+Speed.value+'s';        
      }

      function start() {
        if (Start.innerHTML === "Start") {
          if (
            Team.value === "none" ||
            Player.value === "none" ||
            Whatkind.value === "none" ||
            Amount.value === "" ||
            Amount.value < "0"
          ) {
            Alert.innerHTML = "Please Make Sure All Fields Are Set.";
            setTimeout(() => {
              Alert.innerHTML =
                'Developed By <a href="https://lovelak.rf.gd" target="_blank">Lovelak</a>';
            }, 3000);
          } else {
            window.pywebview.api.start(
              Team.value,
              Player.value,
              Whatkind.value,
              Speed.value,
              Amount.value,
            );
            Start.innerHTML = "Stop";
            Alert.innerHTML =
              Amount.value + " Reports For Player " + Player.value + " Start";
            setTimeout(() => {
              Alert.innerHTML =
                'Click ( STOP ) Or Hold F3 To Stop';
            }, 3000);
          }
        } else {
          window.pywebview.api.stop();
          Start.innerHTML = "Start";
          Alert.innerHTML = "Report Spam Stopped...";
          setTimeout(() => {
            Alert.innerHTML =
              'Developed By <a href="https://lovelak.rf.gd" target="_blank">Lovelak</a>';
          }, 3000);
        }
      }
    </script>
  </body>
</html>

'''

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
                    moveTo(reportX,CTreportY[int(Player)-1],duration=0.2)
                    click(reportX,CTreportY[int(Player)-1])
                    sleep(Speed)
                    moveTo(BAimX,BAimY,duration=0.2)
                    click(BAimX,BAimY)
                    sleep(Speed)
                    moveTo(BsubmitX,BsubmitY,duration=0.2)
                    click(BsubmitX,BsubmitY)
                    sleep(Speed)

        elif Team == "T" and Whatkind == "aim":
            sleep(5)
            for x in range(int(Amount)):
                if self.is_running == False or is_pressed('f3'):
                    break
                else:
                    moveTo(reportX,TreportY[int(Player)-1],duration=0.2)
                    click(reportX,TreportY[int(Player)-1])
                    sleep(Speed)
                    moveTo(BAimX,BAimY,duration=0.2)
                    click(BAimX,BAimY)
                    sleep(Speed)
                    moveTo(BsubmitX,BsubmitY,duration=0.2)
                    click(BsubmitX,BsubmitY)
                    sleep(Speed)

        elif Team == "CT" and Whatkind == "wall":
            sleep(5)
            for x in range(int(Amount)):
                if self.is_running == False or is_pressed('f3'):
                    break
                else:
                    moveTo(reportX,CTreportY[int(Player)-1],duration=0.2)
                    click(reportX,CTreportY[int(Player)-1])
                    sleep(Speed)
                    moveTo(BWallsX,BWallsY,duration=0.2)
                    click(BWallsX,BWallsY)
                    sleep(Speed)
                    moveTo(BsubmitX,BsubmitY,duration=0.2)
                    click(BsubmitX,BsubmitY)
                    sleep(Speed)

        elif Team == "T" and Whatkind == "wall":
            sleep(5)
            for x in range(int(Amount)):
                if self.is_running == False or is_pressed('f3'):
                    break
                else:
                    moveTo(reportX,TreportY[int(Player)-1],duration=0.2)
                    click(reportX,TreportY[int(Player)-1])
                    sleep(Speed)
                    moveTo(BWallsX,BWallsY,duration=0.2)
                    click(BWallsX,BWallsY)
                    sleep(Speed)
                    moveTo(BsubmitX,BsubmitY,duration=0.2)
                    click(BsubmitX,BsubmitY)
                    sleep(Speed)

        else:
            pass

    def stop(self):
        if self.is_running == True:
            self.is_running = False
        
if __name__ == "__main__":
    app = APP()
    webview.create_window('Cheaters Are GAY!',html=HTML,js_api=app,width=300,height=350,resizable=False)
    webview.start()
import webview
import time
import os

class APP():
    is_running = False
    def start(self,Team,Player,Whatkind,Speed,Amount):
        self.is_running = True
        if self.is_running == True:
            print(Team,type(Team))
            print(Player,type(Player))
            print(Whatkind,type(Whatkind))
            print(Speed,type(Speed))
            print(Amount,type(Amount))

            for x in range(int(Amount)):
                if self.is_running == False:
                    break
                else:
                    print(x)
                    time.sleep(0.5)
        else:
            pass

    def stop(self):
        if self.is_running == True:
            self.is_running = False
        


if __name__ == "__main__":
    app = APP()
    webview.create_window('Cheaters Are GAY!',url='src/index.html',js_api=app,width=300,height=350,resizable=False)
    webview.start()
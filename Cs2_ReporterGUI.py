import pyautogui as py



CTreportY = [405,432,456,483,508]
CTColor = (138, 161, 180)

TreportY = [665,690,715,742,769]
TColor = (179, 162, 116)

reportX = 1379

_AIM = 'assets\\img\\aim.png'
_WALL = 'assets\\img\\wall.png'
_SUBMIT = 'assets\\img\\submit.png'



py.sleep(2)
for x in range(10):
    py.sleep(0.1)
    if py.pixelMatchesColor(reportX,CTreportY[0],expectedRGBColor=CTColor,tolerance=10):
        py.click(reportX,CTreportY[0])
        if py.locateOnScreen(_AIM,minSearchTime=1000,confidence=0.8,grayscale=True) != None:
            py.moveTo(_AIM)
            py.click(None,None)
            py.sleep(0.1)

        if py.locateOnScreen(_SUBMIT,minSearchTime=1000,confidence=0.8,grayscale=True) != None:
            py.click(_SUBMIT)
            py.sleep(0.1)
    else:
        print('cant see it')









# if py.locateOnScreen('assets\\img\\wall.png',minSearchTime=1000,confidence=0.8) != None:
#     py.click('assets\\img\\wall.png')
        









# Players X ( CT/T )
# X: 1379 


# CT Color 
# RGB: (138, 161, 180)



# T Color
# RGB: (179, 162, 116)
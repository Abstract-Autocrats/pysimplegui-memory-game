import PySimpleGUI as gui
from random import randint
import threading as th
from time import sleep
import random

"""def getDifficulty():
    layout = [
        [gui.Text("Speed:")],
        [gui.Radio("Easy","DiffRadio"),gui.Radio("Medium","DiffRadio",default=True),gui.Radio("Hard","DiffRadio"),gui.Radio("Extreme","DiffRadio")],
        [gui.Text("Initial Size:")],
        [gui.Slider(range=(1,100),default_value=5,orientation='h',size=(50,10))],
        [gui.OK()]
    ]

    window = gui.Window("Difficulty", layout, keep_on_top=True, font=(None, 15))
    event , values = window.read()
    window.close()

    if values[0]: return (2.00, values[4])
    if values[1]: return (1.00, values[4])
    if values[2]: return (0.50, values[4])
    if values[3]: return (0.25, values[4])
"""
random_list=['mango','banana','apple','milk','cake','orange','chips','vinegar','wheat','rice','sugar','salt','biscuits','oil','dal','chilli']
def showWord():
    global pos, nums, window
    window[pos]('')
    pos = 'box'+randNum()
    newWord = randWord()
    nums.append(newWord)
    window[pos](newWord)

def showTime(window,sec,limit):
    
    if limit == 0:
        return
    
    showWord()
    window.finalize()
    sleep(sec)
    showTime(window,sec,limit-1)


def randNum():
    return str(randint(0,99))

def randWord():
    return str(random.choice(random_list))

def disableControls(window):
    window["Quit"].Update(disabled=True)
    window["OK"].Update(disabled=True)
    window["input"].Update(disabled=True)

def enableControls(window):
    window["Quit"].Update(disabled=False)
    window["OK"].Update(disabled=False)
    window["input"].Update(disabled=False)


gui.ChangeLookAndFeel('Black')

layout = [[gui.Text('SHOPPING LIST!!!')],
          [gui.Text(' ', key='box0', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box10', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box20', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box30', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box40', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box50', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box60', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box70', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box80', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box90', size=(7, 1), pad=(1, 10))],
          [gui.Text(' ', key='box1', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box11', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box21', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box31', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box41', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box51', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box61', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box71', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box81', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box91', size=(7, 1), pad=(1, 10))],
          [gui.Text(' ', key='box2', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box12', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box22', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box32', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box42', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box52', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box62', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box72', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box82', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box92', size=(7, 1), pad=(1, 10))],
          [gui.Text(' ', key='box3', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box13', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box23', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box33', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box43', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box53', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box63', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box73', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box83', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box93', size=(7, 1), pad=(1, 10))],
          [gui.Text(' ', key='box4', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box14', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box24', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box34', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box44', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box54', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box64', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box74', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box84', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box94', size=(7, 1), pad=(1, 10))],
          [gui.Text(' ', key='box5', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box15', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box25', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box35', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box45', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box55', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box65', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box75', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box85', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box95', size=(7, 1), pad=(1, 10))],
          [gui.Text(' ', key='box6', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box16', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box26', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box36', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box46', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box56', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box66', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box76', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box86', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box96', size=(7, 1), pad=(1, 10))],
          [gui.Text(' ', key='box7', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box17', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box27', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box37', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box47', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box57', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box67', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box77', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box87', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box97', size=(7, 1), pad=(1, 10))],
          [gui.Text(' ', key='box8', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box18', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box28', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box38', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box48', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box58', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box68', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box78', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box88', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box98', size=(7, 1), pad=(1, 10))],
          [gui.Text(' ', key='box9', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box19', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box29', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box39', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box49', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box59', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box69', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box79', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box89', size=(7, 1), pad=(1, 10)),gui.Text(' ', key='box99', size=(7, 1), pad=(1, 10))],
          [gui.Text('Press START to begin',pad=(1,10),key="info",size=(50,1))],
          [gui.In(size=(40,1),disabled=True,background_color='white',key="input",text_color='black'), gui.Submit('START',button_color=('purple','white'),key="OK",size=(6,1)),gui.CloseButton('QUIT',button_color=('purple','white'),key="Quit",size=(5,1))]
          ]

window = gui.Window('Memory Game', layout, keep_on_top=True, font=(None, 15))


nums = []
pos = 'box0'

isStart = 1
isWaiting = 0

sec=2.5
level=5

"""temp = getDifficulty()


if temp == None:
    sec = 1
    level = 5
else:
    sec , level = temp

print(level)
print(sec)"""

while True:
    
    event, values = window.read()
    print('Event:',event, values)
    if event in (None, 'Quit'):
        break
    
    if not isStart:
        if values["input"].split() == nums:
            gui.PopupAutoClose("CORRECT",title='',keep_on_top=True,background_color='Dark Green',text_color='White',auto_close_duration=1,button_type=5)
        else:
            gui.Popup("WRONG\n\nCorrect Answer:\n" +" ".join(nums),title='',keep_on_top=True,background_color='Dark Red',text_color='White',font=("Helvetica",15))
            break
        nums.clear()
        window["input"]('')
        isWaiting = 1
        window["info"](">> Press START for next round")
        window["OK"].Update('START')
        window.finalize()
        "level += 1"
        isWaiting = 1
        isStart = 1

    if not isWaiting:
        window["info"](" >> Memorise Them!")
        window.finalize()
        disableControls(window)
        showTime(window,sec,level)
        enableControls(window)
        window[pos]('')
        window["info"](" >> Write Down the items!")
        window["OK"].Update('OK')
        window.finalize()
        isStart = 0
    else:
        isWaiting = 0

    print('nums',nums)

window.close()

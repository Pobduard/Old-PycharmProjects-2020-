import pyautogui as py
import keyboard

py.FAILSAFE = True

def click_fun():
    py.PAUSE = 0
    posx, posy = py.position()
    py.leftClick(x=posx, y=posy, interval=0.02)

def click_fun2():
    py.PAUSE = 0
    posx, posy = py.position()
    py.leftClick(x=posx, y=posy, interval=0.01)

Cliker = False

while 1:
    while keyboard.is_pressed('|'):
        click_fun()
    while keyboard.is_pressed('+'):
        click_fun2()
    if keyboard.is_pressed('q'):
        break
    if keyboard.is_pressed('u'):
        Cliker = True
    while Cliker is True:
            if keyboard.is_pressed('i'):
                Cliker = False
            if keyboard.is_pressed('q'):
                break
            click_fun()

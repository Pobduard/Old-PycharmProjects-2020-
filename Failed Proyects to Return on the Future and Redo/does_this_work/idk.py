import pyautogui
import threading

pyautogui.FAILSAFE = True

images = ["C:/Users/ARELLANO IBARRA/Desktop/Pob/PycharmProjects/does_this_work/prueba1", 
         "C:/Users/ARELLANO IBARRA/Desktop/Pob/PycharmProjects/does_this_work/prueba2", 
         "C:/Users/ARELLANO IBARRA/Desktop/Pob/PycharmProjects/does_this_work/prueba3", 
         "C:/Users/ARELLANO IBARRA/Desktop/Pob/PycharmProjects/does_this_work/prueba4"
         ]



def wait_start(some_number):
    cords = pyautogui.locateOnScreen(images[some_number] + ".jpg")
    pyautogui.click(cords)
    print("no found")

def wait_drag(some_location):
    pyautogui.PAUSE = 0
    pyautogui.mouseDown()
    pyautogui.moveRel(0, 10, duration=1)
    pyautogui.mouseUp()

def main_start(image_num):
    thread = threading.Thread(target=wait_start(image_num))
    thread.start()
    # wait here for the result to be available before continuing
    thread.join()

def main_drag(location_num):
    thread = threading.Thread(target=wait_drag(location_num))
    thread.start()
    # wait here for the result to be available before continuing
    thread.join()


wait_start(1)
print(pyautogui.locateOnScreen("C:/Users/ARELLANO IBARRA/Desktop/Pob/PycharmProjects/does_this_work/prueba1.jpg"))

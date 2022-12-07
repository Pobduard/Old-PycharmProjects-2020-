import pyautogui
import time
import datetime


def restart_time():
    date_time = str(datetime.datetime.now())
    date_time = date_time.split(" ")
    date_time[0] = date_time[0].replace("-", "/")
    time_now = str(date_time[1]).split(".")
    time_time = time_now[0]
    return str("Try at date: " + date_time[0] + " and time: " + time_time)


def click_restart():
    cords = (pyautogui.locateOnScreen("C:/Users/JANETH/PycharmProjects/Restar_Download/screen.png"))
    pyautogui.click(cords)
    print("Found")


time.sleep(2)
while True:
    print("Search" + "\N{RIGHTWARDS BLACK ARROW}" * 10)
    if pyautogui.locateOnScreen("C:/Users/JANETH/PycharmProjects/Restar_Download/screen.png"):
        click_restart()
        print(restart_time())
        pyautogui.moveTo(747, 739)
    else:
        print("Not Found")
    print("Done" + "\N{RIGHTWARDS BLACK ARROW}" * 12)
    time.sleep(20)

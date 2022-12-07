import pyautogui
import keyboard
import time
import os



########################################## SCREENSHOTS
dirreccion_path = os.path.dirname(os.path.realpath(__file__))

print("preparing")
time.sleep(1.2)
print("ready")


def screenie():
    nol_list = open(str(dirreccion_path) + '/archives.txt', "r").read().split(",")
    pyautogui.screenshot(str(dirreccion_path) + "/screenchots/Screen" + nol_list[-1] + ".png")
    print("Screenshot Taken")


########################################## ADD TO TXT FILE

def add_list():
    nol_write = open(str(dirreccion_path) + '/archives.txt', 'a')
    nol_list = open(str(dirreccion_path) + '/archives.txt', "r").read().split(",")
    nol_write.write("," + (str(int(nol_list[-1]) + 1)))
    nol_write.close()


########################################## KEY PRESS LOOP
# while True:
#     if keyboard.is_pressed('0'):
#         screenie()
#         add_list()
#         time.sleep(0.2)
#     elif keyboard.is_pressed('|'):
#         print("closed")
#         time.sleep(1)
#         break

while True:
    keyboard.wait('0')
    screenie()
    add_list()
    time.sleep(0.2)
    if keyboard.is_pressed('|'):
        print("closed")
        time.sleep(1)
        break

########################################## ANOTHER WAY
# while True:
#     if keyboard.is_pressed('0') and not keyboard.is_pressed('|'):
#         screenie()
#         add_list()
#         time.sleep(0.2)
#     time.sleep(0.2)
#     if keyboard.is_pressed('|'):
#         print("closed")
#         time.sleep(1)
#         break

########################################## END OF COMMENTS
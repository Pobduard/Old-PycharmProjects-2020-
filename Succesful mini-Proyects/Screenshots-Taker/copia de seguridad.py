# import pyautogui
# import keyboard
# import time


########################################## SCREENSHOTS

# time.sleep(2)
# num_of_sh = 0
#
#
# def screenie():
#     pyautogui.screenshot("screenchots\screenshot" + str(num_of_sh) + ".png")
#     time.sleep(0.5)
#
#
# for i in range(0, 10):
#    screenie()
#    num_of_sh += 1
# image = pyautogui.screenshot("none.png")
# print(image.getpixel((200, 600)))

########################################## KEY PRESS LOOP

# while True:
#     if keyboard.is_pressed('l+o'):
#         print("l+o pressed")
#         time.sleep(0.2)
#     elif keyboard.is_pressed('q'):
#         break
#

########################################## FAILURE

# print("out of whileloop")
# num = 7
# num_of_screenie = open("archives.txt", "a")
# num_of_screenie.write(str(num) + ",")
# nol = open("nol.txt", "a")
# num_of_screenie.close()
#

########################################## ADD TO TXT FILE

# def add_list():
#     nol_list = open('archives.txt', "r").read().split(",")
#     list_plus = nol_list[-1]
#     nol_write = open('archives.txt', 'a')
#     nol_write.write("," + (str(int(list_plus) + 1)))
#     nol_write.close()
#
#
# for i in range(0, 2):
#     add_list()

########################################## END OF COMMENTS

# Imports time, pyautogui, ctypes and turtle libraries
import pyautogui
import time
import ctypes
import turtle

# Buttons
MB_OK = 0x0
MB_OKCXL = 0x01
MB_YESNOCXL = 0x03
MB_YESNO = 0x04
MB_HELP = 0x4000

# Icons
ICON_EXCLAIM = 0x30
ICON_INFO = 0x40
ICON_STOP = 0x10

# Actual code
result = int(ctypes.windll.user32.MessageBoxW(0, "Do you want to continue?", "Proceed?", MB_YESNO | ICON_EXCLAIM))
if result == 6:
    times = turtle.textinput("Enter here", "How many times do you want to repeat?")
    if times != int:
        ctypes.windll.user32.MessageBoxW(0, "Error", "Value not a number", MB_OK | ICON_STOP)
        exit()
    else:
        time_rep = 0
        games = 0
        while  times > time_rep:
            time.sleep(5)
            time_rep += 1
            games += 1
            pyautogui.FAILSAFE = False
            pyautogui.moveTo(150, 50)
            pyautogui.leftClick()
            pyautogui.moveTo(155, 120)
            pyautogui.leftClick()
            if games == 4:
                time.sleep(10)
                pyautogui.moveTo(840, 870)
                pyautogui.leftClick()
                games -= 4
            
            

else:
    ctypes.windll.user32.MessageBoxW(0, "Abort Initiated", "Aborted", MB_OK | ICON_EXCLAIM)
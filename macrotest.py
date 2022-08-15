from pyautogui import *
import pyautogui
import time, os
import keyboard
import random
import win32api, win32con

file = open("readkey.txt", "a+")
while True:
    time.sleep(0.2)
    file.write(f"[{keyboard.read_key()}]")  
    print(keyboard.read_key())
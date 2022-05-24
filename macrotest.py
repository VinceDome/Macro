from pyautogui import *
import pyautogui
import time, os
import keyboard
import random
import win32api, win32con

for i in range(100000):
    print(str(win32api.GetCursorPos()[0])+" "+str(win32api.GetCursorPos()[1]))

for i in range(20):
    button6location = pyautogui.locateOnScreen('button6.png')
    try:
        button6point = pyautogui.center(button6location)
        win32api.SetCursorPos(button6point)
    except:
        pass


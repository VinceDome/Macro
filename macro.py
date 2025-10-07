import pyautogui
import time, os
import keyboard
import win32api, win32con
import cv2
import numpy as np

def createIfNot(path, pathType, extraAction="pass"):
    if not os.path.exists(path):
        if pathType == "folder":
            os.mkdir(path)
            exec(extraAction)
        elif pathType == "file":
            file = open(path, "a+")
            exec(extraAction)
            file.close()

"""
NOTE

"""

def switch(_bool):
    exec(f"""global {_bool}
if {_bool} == True:
    {_bool} = False
elif {_bool} == False:
    {_bool} = True
else:
    {_bool} = None""")




createIfNot(os.getcwd()+f"/macro_files", "folder")

createIfNot(os.getcwd()+f"/macro_files/data.txt", "file")

createIfNot(os.getcwd()+f"/macro_files/images", "folder")



try:
    data = open(os.getcwd()+f"/macro_files/data.txt", "r")
    profile = data.read()
    data.close()
except FileNotFoundError:
    profile = None


if win32api.GetKeyState(win32con.VK_CAPITAL) == 1:
    pyautogui.press("capslock")

while True:
    os.system("cls")
    print("----------------------------------------------\nrecord (r), delete (d), playback (p) or quit (q)?\n----------------------------------------------")
    if profile != None: 
        while True:
            if keyboard.is_pressed("r"):
                time.sleep(0.01)
                keyboard.press_and_release("backspace")
                mode = "r"
                break
            elif keyboard.is_pressed("p"):
                time.sleep(0.01)
                keyboard.press_and_release("backspace")
                mode = "p"
                break
            elif keyboard.is_pressed("d"):
                time.sleep(0.01)
                keyboard.press_and_release("backspace")
                mode = "d"
                break
            elif keyboard.is_pressed("q"):
                time.sleep(0.01)
                keyboard.press_and_release("backspace")
                exit()
    else:
        mode = "r"


    if mode == "r":
        leftdown = False
        rightdown = False
        actioncounter = 0
        print("epik macroboi\n-----------------------\nv = setcursor\nc = click\nx = setcursor and click\nb = move cursor by\nl = left[down&up]\nr = right[down&up]\nt = type\nw = wait\nq = save\n-----------------------")
        
        print("Which profile do you want to record to?")
        while True:
            time.sleep(0.2)
            recordingProfile = keyboard.read_key()
            if recordingProfile in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                break
        
        print(recordingProfile)
        if profile == None:
            profile = recordingProfile

        """
        while True:
            recordingProfile = input("Which profile do you want to record to? ")
            if recordingProfile in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                break
        
        """


        
        keyboard.press_and_release("backspace")
        filename = input("What should be the name of the new bind? ")

        createIfNot(os.getcwd()+f"/macro_files/profile_{recordingProfile}", "folder")
        createIfNot(os.getcwd()+f"/macro_files/profile_{recordingProfile}/created_macros", "folder")
        createIfNot(os.getcwd()+f"/macro_files/profile_{recordingProfile}/binds.txt", "file")

        bindpath = os.getcwd()+f"/macro_files/profile_{recordingProfile}/created_macros/{filename}.txt"
        if os.path.exists(bindpath):
            os.remove(bindpath)
        pos = open(bindpath, "a+", encoding="utf-8")

        nodelete = input("Delete when activated? (y/n) ")
        if nodelete == "n":
            pos.write("nodelete")
            actioncounter += 1

        while True:
            if keyboard.is_pressed("v"):
                time.sleep(0.1)
                keyboard.press_and_release("backspace")
                if actioncounter != 0:
                    pos.write("\n")
                pos.write("cursor "+str(win32api.GetCursorPos()[0])+" "+str(win32api.GetCursorPos()[1]))
                actioncounter += 1

                print(str(win32api.GetCursorPos()))
                time.sleep(0.2)

            elif keyboard.is_pressed("b"):
                time.sleep(0.1)
                keyboard.press_and_release("backspace")
                x1, y1 = win32api.GetCursorPos()[0], win32api.GetCursorPos()[1]
                if actioncounter != 0:
                    pos.write("\n")

                print("""Move your cursor relative from your current position, then press "b"!""")
                while True:
                    if keyboard.is_pressed("b"):
                        break

                x2, y2 = win32api.GetCursorPos()[0], win32api.GetCursorPos()[1]
                pos.write("cursor rel "+str(x2-x1)+" "+str(y2-y1))
                actioncounter += 1
                #pos.write("\n"+str(win32api.GetCursorPos()))

                print("cursor rel "+str(x2-x1)+" "+str(y2-y1))
                time.sleep(0.2)

            elif keyboard.is_pressed("c"):
                time.sleep(0.1)
                keyboard.press_and_release("backspace")
                if actioncounter != 0:
                    pos.write("\n")

                pos.write("click")
                print("click")
                actioncounter += 1
                time.sleep(0.2)
            
            elif keyboard.is_pressed("r"):
                time.sleep(0.1)
                keyboard.press_and_release("backspace")
                if actioncounter != 0:
                    pos.write("\n")
                
                if rightdown == False:
                    pos.write("down right")
                    print("down right")
                elif rightdown == True:
                    pos.write("up right")
                    print("up right")

                switch("rightdown")
                actioncounter += 1
                time.sleep(0.2)

            elif keyboard.is_pressed("l"):
                time.sleep(0.1)
                keyboard.press_and_release("backspace")
                if actioncounter != 0:
                    pos.write("\n")
                actioncounter += 1

                if leftdown == False:
                    pos.write("down left")
                    print("down left")
                elif leftdown == True:
                    pos.write("up left")
                    print("up left")

                switch("leftdown")
                time.sleep(0.2)

            elif keyboard.is_pressed("x"):
                time.sleep(0.1)
                keyboard.press_and_release("backspace")
                if actioncounter != 0:
                    pos.write("\n")
                pos.write("cursor "+str(win32api.GetCursorPos()[0])+" "+str(win32api.GetCursorPos()[1]))
                pos.write("\nclick")
                actioncounter += 2
                #pos.write("\n"+str(win32api.GetCursorPos()))

                print(str(win32api.GetCursorPos()))
                print("click")
                time.sleep(0.2)
            
            elif keyboard.is_pressed("t"):
                time.sleep(0.1)
                keyboard.press_and_release("backspace")
                
                string = input("What should I type? ")
                if actioncounter != 0:
                    pos.write("\n")
                actioncounter += 1
                pos.write(f"type {string}")
                print(f"type {string}")
                time.sleep(0.2)

            elif keyboard.is_pressed("w"):
                time.sleep(0.1)
                keyboard.press_and_release("backspace")
                while True:
                    try:
                        wait = input("[until/while] image, or [seconds]? ")
                        wait = float(wait)
                        if actioncounter != 0:
                            pos.write("\n")
                        pos.write(f"wait {wait}")
                        break
                    except ValueError:
                        if wait in ["until", "while"]:
                            while True:
                                screenshot = ("Does the image already exist? (y/n) ")
                                if "n" in screenshot:
                                    name = input("What do you want to name the image? ")

                                    print("Move your cursor to the top left corner of the screenshot you want to take, then press enter!")
                                    time.sleep(0.3)
                                    while True:
                                        if keyboard.is_pressed("enter"):
                                            break
                                    sTopleftx, sToplefty = win32api.GetCursorPos()[0], win32api.GetCursorPos()[1]

                                    print("Move your cursor to the top left corner of the screenshot you want to take, then press enter!")
                                    time.sleep(0.3)
                                    while True:
                                        if keyboard.is_pressed("enter"):
                                            break
                                        
                                    sBottomrightx, sBottomrighty = win32api.GetCursorPos()[0], win32api.GetCursorPos()[1]

                                    sBottomrightx -= sTopleftx
                                    sBottomrighty -= sToplefty
                                    
                                    im = pyautogui.screenshot(r"{}".format(os.getcwd()+"\\macro_files\\images\\" + name + ".png"), region=(sTopleftx, sToplefty, sBottomrightx, sBottomrighty))
                                    break

                                elif "y" in screenshot:
                                    name = input("What is the name of the image? ")
                                    if os.path.exists(os.getcwd()+f"/macro_files/images/{name}.png"):
                                        break
                                    print("This image doesn't exist!")

                            print("Move your cursor to the top left corner of the detection region, then press enter!")
                            time.sleep(0.3)
                            while True:
                                if keyboard.is_pressed("enter"):
                                    break

                            topleftx, toplefty = win32api.GetCursorPos()[0], win32api.GetCursorPos()[1]
                            
                            print("Move your cursor to the bottom right corner of the detection region, then press enter!")
                            time.sleep(0.3)
                            while True:
                                if keyboard.is_pressed("enter"):
                                    break

                            bottomrightx, bottomrighty = win32api.GetCursorPos()[0], win32api.GetCursorPos()[1]

                            if actioncounter != 0:
                                pos.write("\n")
                            pos.write(f"wait {wait} {name} {topleftx} {toplefty} {bottomrightx} {bottomrighty}")
                            break

                        print("bruh")
                actioncounter += 1
                time.sleep(0.2)

            elif keyboard.is_pressed("i"):
                time.sleep(0.1)
                keyboard.press_and_release("backspace")
                
                while True:
                    screenshot = input("Does the image already exist? (y/n) ")
                    
                    if "n" in screenshot:
                        name = input("What do you want to name the image? ")

                        print("Move your cursor to the top left corner of the screenshot you want to take, then press enter!")
                        time.sleep(0.3)
                        while True:
                            if keyboard.is_pressed("enter"):
                                break
                        sTopleftx, sToplefty = win32api.GetCursorPos()[0], win32api.GetCursorPos()[1]

                        print("Move your cursor to the bottom right corner of the screenshot you want to take, then press enter!")
                        time.sleep(0.3)
                        while True:
                            if keyboard.is_pressed("enter"):
                                break
                        sBottomrightx, sBottomrighty = win32api.GetCursorPos()[0], win32api.GetCursorPos()[1]

                        sBottomrightx -= sTopleftx
                        sBottomrighty -= sToplefty
                        
                        im = pyautogui.screenshot(r"{}".format(os.getcwd()+"\\macro_files\\images\\" + name + ".png"), region=(sTopleftx, sToplefty, sBottomrightx, sBottomrighty))
                        break
                    elif "y" in screenshot:
                        name = input("What is the name of the image? ")
                        if os.path.exists(os.getcwd()+f"/macro_files/images/{name}.png"):
                            break
                        print("This image doesn't exist!")

                print("Move your cursor to the top left corner of the detection region, then press enter!")
                time.sleep(0.3)
                while True:
                    if keyboard.is_pressed("enter"):
                        break

                topleftx, toplefty = win32api.GetCursorPos()[0], win32api.GetCursorPos()[1]
                
                print("Move your cursor to the bottom right corner of the detecition region, then press enter!")
                time.sleep(0.3)
                while True:
                    if keyboard.is_pressed("enter"):
                        break

                bottomrightx, bottomrighty = win32api.GetCursorPos()[0], win32api.GetCursorPos()[1]


                if actioncounter != 0:
                    pos.write("\n")

                actioncounter += 1
                pos.write(f"cursor {name}.png {topleftx} {toplefty} {bottomrightx} {bottomrighty}")
                print(f"cursor {name}.png {topleftx} {toplefty} {bottomrightx} {bottomrighty}")
                time.sleep(0.2)

            elif keyboard.is_pressed("q"):
                #region checking if empty
                bindsF = open(os.getcwd()+f"/macro_files/profile_{recordingProfile}/binds.txt", "r", encoding="utf-8")
                bindsR = bindsF.read()
                if bindsR == "" or bindsR == " ":
                    empty = True
                else:
                    empty = False
                bindsF.close()
                #endregion

                bindsF = open(os.getcwd()+f"/macro_files/profile_{recordingProfile}/binds.txt", "a+", encoding="utf-8")

                print("What do you want to bind this to?")
                while True:
                    time.sleep(0.2)
                    bindButton = keyboard.read_key()
                    """
                    if bindButton != keyboard.read_key():
                        break
                    """
                    print(bindButton)
                    break
                        

                """
                while True:
                    time.sleep(0.2)
                    keyboard.press_and_release("backspace")
                    bindButton = input("What do you want to bind this to? ")
                    if len(bindButton) == 1:
                        break
                    print("lol only one button")
                """
                if not empty:
                    bindsF.write("\n")
                bindsF.write(f"{bindButton} {filename}")
                time.sleep(0.1)
                keyboard.press_and_release("backspace")
                if actioncounter == 0:
                    print("bruh do something before you exit\n-----------------------")
                    time.sleep(0.3)
                    continue
                bindsF.close()
                pos.close()
                break

    elif mode == "p":
        profilesL = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        bindsF = open(os.getcwd()+f"/macro_files/profile_{profile}/binds.txt", "r", encoding="utf-8")
        bindsL = bindsF.read().split("\n")
        bindsF.close()
        binds = {}

        for i in bindsL:
            individualBind = i.split(" ")
            binds[individualBind[0]] = individualBind[1]

        os.system("cls")
        print(f"Profile [{profile}]\nBinds:\n", binds)
        time.sleep(1)

        activated = True

        while True: 
            time.sleep(0.02)
            if win32api.GetKeyState(win32con.VK_CAPITAL) == 1:
                if keyboard.is_pressed("escape"):
                    break

                elif keyboard.is_pressed("ctrl"):
                    

                    if activated:
                        os.system("cls")
                        print("Profile: [Disabled]")
                        activated = False

                    elif not activated:
                        os.system("cls")
                        print(f"Profile [{profile}]\nBinds:\n", binds)
                        activated = True
                        for i in range(2):
                            pyautogui.press("capslock")


                    for i in range(2):
                        pyautogui.press("capslock")

                    time.sleep(0.3)

                if not activated:
                    continue


                for i in profilesL:
                    if keyboard.is_pressed(i):
                        time.sleep(0.01)
                        keyboard.press_and_release("backspace")

                        if not os.path.exists(os.getcwd()+f"/macro_files/profile_{i}"):
                            continue
                        for a in range(2):
                            pyautogui.press("capslock")

                        os.remove(os.getcwd()+f"/macro_files/data.txt")
                        data = open(os.getcwd()+f"/macro_files/data.txt", "a+")
                        data.write(i)
                        data.close()
                        profile = i
                        #region updatebinds
                        bindsF = open(os.getcwd()+f"/macro_files/profile_{profile}/binds.txt", "r", encoding="utf-8")
                        bindsL = bindsF.read().split("\n")
                        bindsF.close()
                        binds = {}
                        for i in bindsL:
                            individualBind = i.split(" ")
                            binds[individualBind[0]] = individualBind[1]
                        #endregion
                        
                        os.system("cls")    
                        print(f"Profile [{profile}]\nBinds:\n", binds)
                        
                        time.sleep(0.2)

                for i in binds:
                    if keyboard.is_pressed(i):
                        time.sleep(0.01)
                        pos = open(os.getcwd()+f"/macro_files/profile_{profile}/created_macros/{binds[i]}.txt", "r", encoding="utf-8")
                        posRL = pos.read().split("\n")
                        pos.close()
                        if posRL[0] != "nodelete":
                            keyboard.press_and_release("backspace")
                        #region performing the keybind
                        for i in posRL:
                            poslistNUMS = []
                            if i == "" or i == " ":
                                print("extra whitespace")
                                break

                            while keyboard.is_pressed("q"):
                                print("manually paused for 5secs")
                                time.sleep(5)
                                print("continuing")
                            if keyboard.is_pressed("escape"):
                                print("force quitting")
                                time.sleep(2)
                                break
                        
                            if i == "click":
                                pyautogui.mouseDown()
                                time.sleep(0.01)
                                pyautogui.mouseUp()
                                time.sleep(0.01)
                                continue

                            
                            poslist = i.split(" ")
                            if poslist[0] == "type":
                                if win32api.GetKeyState(win32con.VK_CAPITAL) == 1:
                                    pyautogui.press("capslock")
                                time.sleep(0.01)

                                for a in poslist:
                                    if a != poslist[0]:
                                        if a == "enter":
                                            time.sleep(0.01)
                                            keyboard.press_and_release("enter")
                                            continue
                                        elif a == "left":
                                            time.sleep(0.01)
                                            keyboard.press_and_release("left_arrow")
                                            continue
                                        elif a == "right":
                                            time.sleep(0.01)
                                            keyboard.press_and_release("right_arrow")
                                            continue

                                        keyboard.write(a)
                                        if not a == poslist[len(poslist)-1]:
                                            theresmore = False
                                            for i in range(poslist.index(a), len(poslist)):
                                                if i != "enter":
                                                    theresmore = True
                                                    break
                                            if theresmore:
                                                keyboard.press_and_release(" ")
                                                
                                if win32api.GetKeyState(win32con.VK_CAPITAL) == 0:
                                    pyautogui.press("capslock")
                                time.sleep(0.05)
                                continue
                            
                            elif poslist[0] == "cursor":
                                if len(poslist) == 3:
                                    for i in range(3):
                                        if i != 0:
                                            poslistNUMS.append(int(poslist[i]))
                                    pyautogui.moveTo(poslistNUMS[0], poslistNUMS[1])

                                elif len(poslist) == 4:
                                    if poslist[1] == "rel":
                                        for i in range(4):
                                            if i != 0 and i != 1:
                                                poslistNUMS.append(int(poslist[i]))

                                        x, y = win32api.GetCursorPos()[0], win32api.GetCursorPos()[1]
                                        poslistNUMS[0] += x
                                        poslistNUMS[1] += y      
                                        win32api.SetCursorPos(poslistNUMS)

                                elif len(poslist) == 6:
                                    path = os.path.join(os.getcwd(), "macro_files", "images", poslist[1])
                                 
                                    # fr"""{os.getcwd()}\\macro_files\\images\\{poslist[1]}"""
                                    img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), 0)

                                    location = pyautogui.locateOnScreen(img, region=(int(poslist[2]),int(poslist[3]), int(poslist[4]), int(poslist[5])), confidence = 0.85)
                                    if location == None:
                                        continue
                                    locationC = pyautogui.center(location)
                                    win32api.SetCursorPos(locationC)
                                                    
                            elif poslist[0] == "wait":
                                if len(poslist) <= 2:
                                    time.sleep(float(poslist[1]))
                                else:
                                    sleeptime = 0.3
                                    if poslist[1] == "slow":
                                        sleeptime = 5
                                    if poslist[len(poslist)-6] == "until":
                                        while True:
                                            time.sleep(sleeptime)
                                            if keyboard.is_pressed("escape"):
                                                print("force quitting")
                                                time.sleep(2)
                                                os.system("cls")
                                                break

                                            path = os.path.join(os.getcwd(), "macro_files", "images", poslist[len(poslist)-5])
                                 
                                            
                                            img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), 0)
                                            location = pyautogui.locateOnScreen(img, region=(int(poslist[len(poslist)-4]),int(poslist[len(poslist)-3]), int(poslist[len(poslist)-2]), int(poslist[len(poslist)-1])), confidence = 0.85)

                                            if location != None:    
                                                break

                                

                                    elif poslist[len(poslist)-6] == "while":
                                        while True:
                                            time.sleep(sleeptime)
                                            if keyboard.is_pressed("escape"):
                                                print("force quitting")
                                                time.sleep(2)
                                                os.system("cls")
                                                break
                                            
                                            path = os.path.join(os.getcwd(), "macro_files", "images", poslist[len(poslist)-5])
                                            
                                            img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), 0)
                                            location = pyautogui.locateOnScreen(img, region=(int(poslist[len(poslist)-4]),int(poslist[len(poslist)-3]), int(poslist[len(poslist)-2]), int(poslist[len(poslist)-1])), confidence = 0.85)
                                            if location == None:    
                                                break
                                            
                            elif poslist[0] == "down": 
                                time.sleep(0.15)
                                if poslist[1] == "left":
                                    pyautogui.mouseDown()
                                elif poslist[1] == "right":
                                    pyautogui.mouseDown(button="right")
                                time.sleep(0.15)
                                
                            elif poslist[0] == "up":
                                time.sleep(0.15)
                                if poslist[1] == "left":
                                    pyautogui.mouseUp()
                                elif poslist[1] == "right":
                                    pyautogui.mouseUp(button="right")

                        if "capsoff" in posRL[0]:
                            pyautogui.press("capslock")
                        time.sleep(0.2)
                        #endregion

    elif mode == "d":
        print("Which profile do you want to delete from?")
        while True:
            time.sleep(0.2)
            deleteProfile = keyboard.read_key()
            if deleteProfile in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                break
        print(deleteProfile)

        print("Which letter is the macro binded to?")
        while True:
            time.sleep(0.2)
            bindButton = keyboard.read_key().lower()
            print(bindButton)
            break

        
        
        profilepath = os.getcwd()+f"/macro_files/profile_{deleteProfile}"

        binds = open(profilepath+"/binds.txt", "r")
        bindsR = binds.read()
        binds.close()

        bindsL = bindsR.split("\n")

        for i in bindsL:
            iS = i.split(" ")
            if iS[0] == bindButton:
                bindname = iS[1]
                bindsL.remove(i)
                break

        os.remove(profilepath+"/binds.txt")
        binds = open(profilepath+"/binds.txt", "a+")
        binds.write("\n".join(bindsL))
        binds.close()

        os.remove(profilepath+f"/created_macros/{bindname}.txt")





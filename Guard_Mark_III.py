import cv2
import pyautogui
import pydirectinput
import time
import win32gui
import win32ui
import win32con
from python_imagesearch.imagesearch import imagesearch

a = 0
b = 0

def Screenshot():
    w = 1920
    h = 1080
    bmpfilenamename = "Screenshot.bmp"

    hwnd = None
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
    dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)

    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())


def playerLocation():
    global xPlayer, yPlayer

    screenshot = cv2.imread('./Screenshot.bmp')
    img_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    player = cv2.imread('./Data/leader.png', cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(screenshot, player, cv2.TM_CCORR)
    
    loc  = cv2.minMaxLoc(result)
    playerCoordinates = loc[3]

    xPlayer = playerCoordinates[0]
    yPlayer = playerCoordinates[1]


def move(x, y):
    global a, b
    
    if (x == a) and (y == b):
        pass
    else:
        pyautogui.moveTo(x - 180, y + 180)
        pyautogui.rightClick()
        a = x
        b = y

   
def hourse():
    pydirectinput.keyDown('a')
    pydirectinput.keyUp('a')
    time.sleep(3)


def pve():
    global pve_pos
    
    if (pve_pos[0] != -1):
        pydirectinput.keyDown('a')
        pydirectinput.keyUp('a')
        time.sleep(0.4)
        pyautogui.moveTo(pve_pos[0] + 5, pve_pos[1] + 10)
        pyautogui.click()
        pydirectinput.keyDown('q')
        pydirectinput.keyUp('q')
        time.sleep(2)
        pydirectinput.keyDown('q')
        pydirectinput.keyUp('q')
        pve_pos = imagesearch('./Data/pve.png')
        if (pve_pos[0] != -1):
            pydirectinput.keyDown('w')
            pydirectinput.keyUp('w')
            time.sleep(1)
            pydirectinput.keyDown('w')
            pydirectinput.keyUp('w')
            time.sleep(1.2)
            pydirectinput.keyDown('e')
            pydirectinput.keyUp('e')
            pyautogui.click()
            time.sleep(3)
            pydirectinput.keyDown('e')
            pydirectinput.keyUp('e')
        else:
            pass
    else:
        pass


def pvp():
    global pvp_pos
    
    if (pvp_pos[0] != -1):
        pydirectinput.keyDown('a')
        pydirectinput.keyUp('a')
        time.sleep(0.4)
        pyautogui.moveTo(pvp_pos[0] + 5, pvp_pos[1] + 150)
        pyautogui.click()
        pydirectinput.keyDown('d')
        pydirectinput.keyUp('d')
        time.sleep(0.4)
        pydirectinput.keyDown('q')
        pydirectinput.keyUp('q')
        time.sleep(2)
        pydirectinput.keyDown('q')
        pydirectinput.keyUp('q')
        pvp_pos = imagesearch('./Data/pvp.png')
        if (pvp_pos[0] != -1):
            pyautogui.moveTo(pvp_pos[0] + 5, pvp_pos[1] + 150)
            pydirectinput.keyDown('w')
            pydirectinput.keyUp('w')
            pyautogui.click()
            time.sleep(1)
            pydirectinput.keyDown('w')
            pydirectinput.keyUp('w')
            time.sleep(1.2)
            pydirectinput.keyDown('e')
            pydirectinput.keyUp('e')
            pyautogui.click()
            time.sleep(3)
            pydirectinput.keyDown('e')
            pydirectinput.keyUp('e')
        else:
            pass
    else:
        pass

print('|===============================================|')
print('|===============  Guard Mark III  ==============|')
print('|===============================================|')
print('|                                               |')
print('|  ATTENTION! THIS PRODUCT IS PROHIBITED FOR    |')
print('|  DISTRIBUTION. ANYONE WHO WILL BE INVOLVED IN |')
print('|  ITS DISTRIBUTION TAKES FULLY RESPONSIBILITY. |')
print('|  RESPONSIBILITY STARTS FROM THE MOMENT OF     |')
print('|  RECEIPT OF THIS PROGRAM!                     |')
print('|                                               |')
print('|                                               |')
print('|===============================================|')
print('|            Copyright by Lucky38©              |')
print('|===============================================|')

while True:
    pve_pos = imagesearch('./Data/pve.png')
    pvp_pos = imagesearch('./Data/pvp.png')
    hourse_pos = imagesearch('./Data/hourse.png')
    
    Screenshot()
    if pve_pos[0] != -1 or pvp_pos[0] != -1:
        pve()
        pvp()
    elif hourse_pos[0] != -1:
        hourse()
    else:
        playerLocation()
        print(xPlayer, yPlayer)
        move(xPlayer, yPlayer)

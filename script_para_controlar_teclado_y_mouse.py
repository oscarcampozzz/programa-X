import keyboard
import pyautogui as pi
import random
import time 

while True:
    pi.moveTo(x=random.randint(10,1910),y=random.randint(10,1070))
    time.sleep(3)
    if keyboard.is_pressed("a"):
        break
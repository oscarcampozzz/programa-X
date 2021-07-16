import keyboard
import pyautogui as pa
import random

print(pa.position())

for i in range(10):
    pa.moveTo(x=random.randint(10,1910), y=random.randint(10,1070))
    print(pa.position())
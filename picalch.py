import pyautogui as pg
from extUtils import sleepy

sleepy(5, 2)
alch = pg.locateOnScreen('high_alch.png', confidence='0.9')
pg.moveTo(alch)

while True:
    if (pg.locateOnScreen('high_alch.png', confidence='0.9') is not None):
        sleepy(1, 0.5)
        pg.click()
        sleepy(0.2, 0.02)
        pg.click()
        sleepy(0.15, 0.05)
    else:
        sleepy(1, 1)

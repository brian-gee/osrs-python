from extUtils import sleepy
import pyautogui as pg
from time import sleep

def click_overload():
    current_pos = pg.position()
    overload = pg.locateOnScreen('cyan-overload.png', confidence=0.9)
    pg.click(overload)
    pg.moveTo(current_pos)
    sleep(300)
    print('Overload')
    sleepy(3, 0.5)

if __name__ == "__main__":
    sleepy(5, 0.5)
    while (pg.locateOnScreen('nmz.png', confidence=0.9) is not None):
        click_overload()

from extUtils import sleepy, sleeper
from time import sleep
import pyautogui as pg

def guzzle_cake():
    cake = pg.locateOnScreen('prayer.png', confidence=0.9)
    current_pos = pg.position()
    pg.moveTo(cake)
    pg.click()
    print('wait for flick')
    sleepy(0.4, 0.03)
    pg.moveTo(cake)
    pg.click()
    pg.moveTo(current_pos)

if __name__ == "__main__":
    sleepy(15, 0.5)
    while (pg.locateOnScreen('nmz.png', confidence=0.9) is not None):
        guzzle_cake()
        print("Guzzle")
        sleeper(25, 54)

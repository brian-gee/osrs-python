from random import randint, uniform
from time import sleep
import pyautogui as pg


def shorter_sleep():
    sleep(uniform(0.25, 0.52))

def short_sleep():
    sleep(randint(2, 4))

def long_sleep():
    sleep(randint(23, 47))

def click_prayer():
    current_pos = pg.position()
    # pg.click(812, 321)
    pg.click(1709, 670)
    shorter_sleep()
    # pg.click(812, 321)
    pg.click(1709, 670)
    pg.moveTo(current_pos)


if __name__ == "__main__":
    while True:
        click_prayer()
        long_sleep()


from extUtils import sleepy
import pyautogui as pg
from time import sleep
import random

def click_overload():
    current_pos = pg.position()
    overload = pg.locateOnScreen('overload.png', confidence=0.9)
    pg.click(overload)
    pg.moveTo(current_pos)
    sleep(300)
    print('Overload')
    sleepy(3, 0.5)

if __name__ == "__main__":
    while (pg.locateOnScreen('nmz.png', confidence=0.9) is not None):
        click_overload()

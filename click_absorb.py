from extUtils import sleepy, sleeper
import pyautogui as pg
from time import sleep
import random

def click_absorb():
    absorb = pg.locateOnScreen('absorb.png', confidence=0.9)
    pg.click(absorb)

# def click_absorb_start(): #     current_pos = pg.position() #     for i in range(21): #         absorb = pg.locateOnScreen('absorb.png', confidence=0.9)
#         pg.click(absorb)
#         pg.moveTo(current_pos)
#         sleepy(2, 0.5)

# def click_cake():
#     current_pos = pg.position()
#     cake = pg.locateOnScreen('rock_cake.png', confidence=1.9)
#
#     for i in range(6):
#         pg.click(cake)
#         pg.moveTo(current_pos)

if __name__ == "__main__":
    while True:
        if (pg.locateOnScreen('nmz.png', confidence=0.8) is not None):
            sleeper(8, 15)
            for i in range(random.randint(6, 12)):
                click_absorb()
                sleepy(0.7, 0.05)
            print('Absorb')
            sleepy(2400, 0.5)
        else:
            break

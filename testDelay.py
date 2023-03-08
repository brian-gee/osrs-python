from extUtils import sleepy
import pyautogui as pg
from time import sleep
import random

def click_overload():
    current_pos = pg.position()
    overload = pg.locateOnScreen('delayClick.png')
    pg.click(overload)
    pg.moveTo(current_pos)
    print('Clicked')

if __name__ == "__main__":
  while True: 
    click_overload()

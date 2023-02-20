from bezier_mouse import move_mouse
from pyautogui import click
from random import uniform, gauss
from time import sleep

def rand_cord(x, y, mu=4):
    return int(abs(gauss(x, mu))), int(abs(gauss(y, mu)))

def sleepy(delay, mu):
    rand = abs(gauss(delay, mu))
    print(rand)
    sleep(rand)

def sleeper(delay_min, delay_max):
    rand = uniform(delay_min, delay_max)
    print(rand)
    sleep(rand)

def click_move(x, y):
    # rand = abs(gauss(0.2, 0.01))
    # pg.moveTo(x, y, rand)
    move_mouse(x, y)
    click()

def bezier_move(x, y):
    move_mouse(x, y)

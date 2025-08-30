import pyautogui
import random
import numpy as np
import time
from scipy import interpolate
import math

# Setting a low PAUSE is better than a manual sleep in the loop
pyautogui.PAUSE = 0.0

def point_dist(x1,y1,x2,y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def move_mouse(x2, y2):
    cp = random.randint(2, 4)
    x1, y1 = pyautogui.position()

    x = np.linspace(x1, x2, num=cp, dtype='int')
    y = np.linspace(y1, y2, num=cp, dtype='int')

    RND_X = 10 # Controls left-and-right deviation
    RND_Y = 2  # Controls up-and-down deviation

    xr = [random.randint(-RND_X, RND_X) for _ in range(cp)]
    yr = [random.randint(-RND_Y, RND_Y) for _ in range(cp)]
    
    xr[0] = yr[0] = xr[-1] = yr[-1] = 0
    x += xr
    y += yr

    degree = 3 if cp > 3 else cp - 1
    tck, u = interpolate.splprep([x, y], k=degree)

    # --- CHANGE #1: FEWER STEPS FOR HIGHER SPEED ---
    # Increasing the divisor from 4.0 to 15.0 generates fewer points.
    # Fewer points = faster movement. Try adjusting this number to your liking.
    num_points = max(20, int(point_dist(x1, y1, x2, y2) / 15.0)) # Previously / 4.0
    u = np.linspace(0, 1, num=num_points)
    points = interpolate.splev(u, tck)

    # --- CHANGE #2: DURATION SET TO ZERO ---
    # Since the goal is maximum speed, we set the duration between each point to 0.
    step_duration = 0.0
    
    point_list = zip(*(i.astype(int) for i in points))
    for point in point_list:
        pyautogui.moveTo(*point, duration=step_duration)

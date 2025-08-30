# Note: Ensure your utility file is named "extUtils.py" in the same folder
from extUtils import click_move, rand_cord
from time import sleep
from pynput import keyboard # Switched from 'keyboard' to 'pynput.keyboard'

# --- CONFIGURATION ---
# 1. Replace these coordinates with the ones you found
POINT_A = (2003, 383)
POINT_B = (2100, 381) 

# 2. Set the keybinds you want to use for each point
#    These are now single characters.
KEY_A = '1'
KEY_B = '2'
QUIT_KEY = 'q'

# --- MAIN LOGIC ---

def click_at_point(coords):
    """
    Takes a coordinate tuple, randomizes it using your utility, and clicks.
    """
    rand_coords = rand_cord(*coords)
    click_move(rand_coords[0], rand_coords[1])
    print(f"Clicked near {coords}")

def on_press(key):
    """
    This function is called every time a key is pressed.
    """
    try:
        # Check if the pressed key matches one of our keybinds
        if key.char == KEY_A:
            click_at_point(POINT_A)
        elif key.char == KEY_B:
            click_at_point(POINT_B)
        elif key.char == QUIT_KEY:
            print("Quit key pressed. Exiting...")
            # Returning False stops the listener
            return False
    except AttributeError:
        # This handles special keys (like Ctrl, Shift) that don't have a 'char' attribute
        pass

if __name__ == "__main__":
    print(f"Script loaded and listening...")
    print(f"Press '{KEY_A}' to click Point A {POINT_A}")
    print(f"Press '{KEY_B}' to click Point B {POINT_B}")
    print(f"Press '{QUIT_KEY}' to exit the script.")

    # Set up the listener and join it to the main thread to keep running
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

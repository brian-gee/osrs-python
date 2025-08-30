from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    """
    This function is called every time a mouse event occurs.
    We only care about the 'press' event.
    """
    if pressed:
        print(f"Mouse clicked at: (X={x}, Y={y})")

print("Listening for mouse clicks...")
print("Press Ctrl-C in this terminal to quit.")

# Set up the listener that calls 'on_click' for each mouse event
with Listener(on_click=on_click) as listener:
    listener.join()

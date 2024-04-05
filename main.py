import pyautogui
import time
import keyboard
import threading
import sys
import pyscreeze
from PIL import Image

def shutdown_on_t():
    def check_for_t():
        while True:

            if keyboard.is_pressed('t'):
                print("Key 't' pressed. Shutting down the program.")
                global function_running
                function_running = 0
                sys.exit()  # Exit the program if 't' is pressed
s
    # Create a thread for the check_for_t function
    t_thread = threading.Thread(target=check_for_t, daemon=True)

    # Start the thread
    t_thread.start()


# Test the function
shutdown_on_t()


function_running = False

def is_mouse_on_black_pixel():
    # Get the current position of the mouse
    mouse_x, mouse_y = pyautogui.position()

    # Get the color of the pixel at the mouse position
    pixel_color = pyautogui.pixel(mouse_x, mouse_y)

    global function_running
    # Check if the pixel color is black (0, 0, 0) in RGB
    if pixel_color == (0, 0, 0):
        if not function_running:
            function_running = True
            GotCopper()
        return True
    else:
        if not function_running:
            function_running = True
            ShouldFindCopper()
        return False
# when we have no copper u call this

def ShouldFindCopper():
    noCopper = True
    #screen_width, screen_height = pyautogui.size()

    #print("Screen width:", screen_width, "pixels")
    #print("Screen height:", screen_height, "pixels")
    while noCopper:
        time.sleep(2)
        onCopper = not is_mouse_on_black_pixel()
        pyautogui.move(20, 0)
    global function_running
    function_running = False
    is_mouse_on_black_pixel()


def GotCopper():
    haveCopper = True
    pyautogui.mouseDown(button='left')

    while haveCopper:
        time.sleep(2)
        haveCopper = is_mouse_on_black_pixel()
    pyautogui.mouseUp(button='left')

    global function_running
    function_running = False
    is_mouse_on_black_pixel()

is_mouse_on_black_pixel()
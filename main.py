import pyautogui
import time
import keyboard
import threading
import sys

end = False
def shutdown_on_t():
    def check_for_t():
        while True:

            if keyboard.is_pressed('t'):
                print("Key 't' pressed. Shutting down the program.")
                global end
                end = True
                sys.exit()  # Exit the program if 't' is pressed

    # Create a thread for the check_for_t function
    t_thread = threading.Thread(target=check_for_t, daemon=True)

    # Start the thread
    t_thread.start()


# Test the function
shutdown_on_t()

function_running = False
import detection as dec

get, close = dec.load_mss()
def is_mouse_on_black_pixel():
    global end
    if end:
        sys.exit()

    global function_running
    foundcopper = dec.heuristic_is_copper(get())


    if foundcopper:
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
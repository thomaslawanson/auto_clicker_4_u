import pyautogui
from pynput.keyboard import *

#  ======== settings ========
delay = 0.0001  # in seconds

resume_key = Key.f6
pause_key = Key.f2
exit_key = Key.esc
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// AutoClicker by sadthomas")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t F6 = Resume")
    print("\t F2 = Pause")
    print("\t F3 = Exit")
    print("-----------------------------------------------------")
    print('Press F6 to start ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()
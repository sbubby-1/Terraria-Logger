import keyboard
import LoggingLogic
import sys


def startKeyboardListener():
    keyboard.add_hotkey("ctrl+shift+m", LoggingLogic.resetTriggered)
    keyboard.wait("ctrl+shift+w")
    shutdown()


def shutdown():
    keyboard.unhook_all_hotkeys()
    sys.exit(0)


startKeyboardListener()

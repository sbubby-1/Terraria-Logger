import keyboard
from LoggingLogic import resetTriggered, saveSeed
import sys


def startKeyboardListener():
    keyboard.add_hotkey("ctrl+shift+m", resetTriggered)
    keyboard.add_hotkey("ctrl+shift+s", saveSeed)
    keyboard.wait("ctrl+shift+w")
    shutdown()


def shutdown():
    keyboard.unhook_all_hotkeys()
    sys.exit(0)

from LoggingLogic import resetTriggered, saveSeed
from Display import toggleVisibility
import keyboard


def startKeyboardListener():
    keyboard.add_hotkey("ctrl+shift+m", resetTriggered)
    keyboard.add_hotkey("ctrl+shift+h", toggleVisibility)
    keyboard.add_hotkey("ctrl+shift+p", saveSeed)
    keyboard.wait()

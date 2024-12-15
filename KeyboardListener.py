from LoggingLogic import resetTriggered, saveSeed
import keyboard


def startKeyboardListener():
    keyboard.add_hotkey("ctrl+shift+m", resetTriggered)
    keyboard.add_hotkey("ctrl+shift+s", saveSeed)
    keyboard.wait()

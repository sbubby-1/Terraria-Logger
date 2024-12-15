from Display import toggleVisibility
from LoggingLogic import resetTriggered, saveSeed
import keyboard


def startKeyboardListener():
    """
    Assigns key combinations to actions and begins keyboard listening.
    """

    # Analyzes and deletes the first .wld found in the Worlds folder.
    keyboard.add_hotkey("ctrl+shift+m", resetTriggered)

    # Hides or unhides the display window.
    keyboard.add_hotkey("ctrl+shift+h", toggleVisibility)

    # Saves the current seed alongside its relevant info in JSON format.
    keyboard.add_hotkey("ctrl+shift+p", saveSeed)

    keyboard.wait()

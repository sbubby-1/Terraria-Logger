from KeyboardListener import startKeyboardListener
from Display import startDisplay
import threading

listenerThread = threading.Thread(target=startKeyboardListener, daemon=True)
listenerThread.start()
startDisplay()

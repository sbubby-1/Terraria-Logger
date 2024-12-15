from Display import startDisplay
from KeyboardListener import startKeyboardListener
import threading

# The keyboard listener is started on a separate thread to prevent
# keyboard.wait() from blocking execution of startDisplay().
listenerThread = threading.Thread(target=startKeyboardListener, daemon=True)
listenerThread.start()

startDisplay()

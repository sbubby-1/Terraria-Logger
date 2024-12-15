from PIL import Image, ImageTk
import WorldInfo
import keyboard
import os
import sys
import tkinter as tk

ASSETS_FOLDER = os.path.join(os.getcwd(), "Assets")
BG_COLOR = "#161618"
CANVAS_HEIGHT = 80
CANVAS_WIDTH = 300
ICON_Y = 50
LINE_Y = 60
PADDING = 30

# The display window.
root = tk.Tk()

# The canvas on which widgets are drawn.
canvas = tk.Canvas(
    root,
    width=CANVAS_WIDTH,
    height=CANVAS_HEIGHT,
    bg=BG_COLOR,
    highlightthickness=0,
)

# All widgets that are currently drawn on the canvas.
drawnWidgets = []

# A list that holds references to ``PhotoImages`` so they're not removed by
# garbage collection.
preventImageGarbageCollection = []


def startDisplay():
    """
    Initializes the display and begins the loop.
    """

    setRootProperties()
    createCanvas()

    root.mainloop()


def toggleVisibility():
    """
    Toggles the visibility of the display window.
    """

    if root.state() == "withdrawn":
        root.deiconify()
    else:
        root.withdraw()


def setRootProperties():
    """
    Configures the window's properties.
    """

    root.configure(bg=BG_COLOR)
    root.title("Terraria Reset Feedback")
    root.iconbitmap(os.path.join(ASSETS_FOLDER, "King_Slime.ico"))
    root.geometry(f"{CANVAS_WIDTH}x{CANVAS_HEIGHT}")
    root.attributes("-topmost", True)
    root.protocol("WM_DELETE_WINDOW", shutdown)


def drawWidgets():
    """
    Draws the Spawn, Dungeon, and Pyramid Items on the canvas.
    """

    removeWidgets()

    try:
        spawnXPosition = WorldInfo.relevantInfo["Spawn X"]
        drawIcon(spawnXPosition, os.path.join(ASSETS_FOLDER, "MapSpawn.png"))

        dungeonXPosition = WorldInfo.relevantInfo["Dungeon X"]
        drawIcon(dungeonXPosition, "./Assets/Dungeon_Spirit.png")

        for item in WorldInfo.pyramidItems:
            iconPath = ""

            match item.itemName:
                case "Sandstorm in a Bottle":
                    iconPath = "./Assets/Sandstorm_in_a_Bottle.png"
                case "Flying Carpet":
                    iconPath = "./Assets/Flying_Carpet.png"
                case "Pharaoh's Mask":
                    iconPath = "./Assets/Pharaoh's_Mask.png"

            pyramidItemXPosition = item.chestX
            drawIcon(pyramidItemXPosition, iconPath)

    except Exception as e:
        print(e)


def drawIcon(position, iconPath):
    """
    Draws a single icon on the canvas.

    Parameters:
    ----------
    position: Int
        The position of the structure in the World. This is to be converted to
        its position on the canvas.

    iconPath: String
        The path to the image for the icon.
    ----------
    """

    lineWidth = CANVAS_WIDTH - PADDING * 2
    worldWidth = WorldInfo.relevantInfo["World Width"]
    canvasPosition = (position * lineWidth) / worldWidth + PADDING

    # The images are garbage collected and won't be displayed if I don't retain
    # a reference to them.
    iconImage = ImageTk.PhotoImage(Image.open(iconPath))
    preventImageGarbageCollection.append(iconImage)

    icon = canvas.create_image(canvasPosition, ICON_Y, image=iconImage)
    drawnWidgets.append(icon)


def removeWidgets():
    """
    Reverts the canvas to a blank state.
    """

    for widget in drawnWidgets:
        canvas.delete(widget)

    drawnWidgets.clear()
    preventImageGarbageCollection.clear()


def createCanvas():
    """
    Adds the canvas to the window along with a line representing the world
    width.
    """

    canvas.pack()

    canvas.create_line(
        PADDING,
        LINE_Y,
        CANVAS_WIDTH - PADDING,
        LINE_Y,
        width=4,
        fill="#06402B",
        capstyle="round",
    )


def shutdown():
    """
    Cleanly exits the program.
    """

    keyboard.unhook_all()
    root.destroy()
    sys.exit(0)

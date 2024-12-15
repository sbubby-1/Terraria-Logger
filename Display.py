import os
import tkinter as tk
import keyboard
import sys
import WorldInfo
from PIL import Image, ImageTk

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 80
LINE_Y = 60
ICON_Y = 50
PADDING = 30
BG_COLOR = "#161618"
ASSETS_FOLDER = os.path.join(os.getcwd(), "Assets")

root = tk.Tk()
canvas = tk.Canvas(
    root,
    width=CANVAS_WIDTH,
    height=CANVAS_HEIGHT,
    bg=BG_COLOR,
    highlightthickness=0,
)

drawnWidgets = []
preventImageGarbageCollection = []


def startDisplay():
    setRootProperties()
    createCanvas()

    root.mainloop()


def toggleVisibility():
    if root.state() == "withdrawn":
        root.deiconify()
    else:
        root.withdraw()


def setRootProperties():
    root.configure(bg=BG_COLOR)
    root.title("Terraria Reset Feedback")
    root.iconbitmap(os.path.join(ASSETS_FOLDER, "King_Slime.ico"))
    root.geometry(f"{CANVAS_WIDTH}x{CANVAS_HEIGHT}")
    root.attributes("-topmost", True)
    root.protocol("WM_DELETE_WINDOW", shutdown)


def drawWidgets():
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
        pass


def drawIcon(position, iconPath):
    lineWidth = CANVAS_WIDTH - PADDING * 2
    worldWidth = WorldInfo.relevantInfo["World Width"]
    canvasPosition = (position * lineWidth) / worldWidth + PADDING

    # The images are garbage collected and won't be displayed if I don't retain a reference to them.
    iconImage = ImageTk.PhotoImage(Image.open(iconPath))
    preventImageGarbageCollection.append(iconImage)

    icon = canvas.create_image(canvasPosition, ICON_Y, image=iconImage)
    drawnWidgets.append(icon)


def removeWidgets():
    for widget in drawnWidgets:
        canvas.delete(widget)

    drawnWidgets.clear()
    preventImageGarbageCollection.clear()


def createCanvas():
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
    keyboard.unhook_all()
    root.destroy()
    sys.exit(0)

from CustomExceptions.InvalidWorldsFolder import InvalidWorldsFolder
import os
from ParseWorldFile import analyzeWorld
import WorldInfo

WORLDS_FOLDER_FILEPATH = "C:/Documents/My Games/Terraria/Worlds"


def resetTriggered():
    if not WORLDS_FOLDER_FILEPATH.endswith(r"/Documents/My Games/Terraria/Worlds"):
        raise InvalidWorldsFolder()

    worldsFolderFiles = os.listdir(WORLDS_FOLDER_FILEPATH)

    foundFile = False
    for fileName in worldsFolderFiles:
        if not fileName.endswith("wld"):
            continue

        worldFilepath = os.path.join(WORLDS_FOLDER_FILEPATH, fileName)
        if os.path.isdir(worldFilepath):
            continue

        foundFile = True
        analyzeWorld(worldFilepath)
        os.remove(worldFilepath)
        break

    if not foundFile:
        return

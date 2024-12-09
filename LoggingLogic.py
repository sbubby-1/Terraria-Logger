import os
import json

from CustomExceptions.InvalidWorldsFolder import InvalidWorldsFolder
from ParseWorldFile import analyzeWorld
from WorldInfo import getSeedInfo

WORLDS_FOLDER_FILEPATH = "C:/Documents/My Games/Terraria/Worlds"
SAVED_SEEDS_FILEPATH = "C:/Documents/My Games/Terraria/Saved Seeds"


def resetTriggered():
    if not WORLDS_FOLDER_FILEPATH.endswith(r"/Terraria/Worlds"):
        raise InvalidWorldsFolder()

    worldsFolderFiles = os.listdir(WORLDS_FOLDER_FILEPATH)

    foundFile = False
    for fileName in worldsFolderFiles:
        if not fileName.endswith(".wld"):
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

    seedInfo = getSeedInfo()


def saveSeed():
    writeSeed(getSeedInfo())


def writeSeed(seedInfo):
    if not os.path.exists(SAVED_SEEDS_FILEPATH):
        os.makedirs(SAVED_SEEDS_FILEPATH)

    outputFilepath = os.path.join(SAVED_SEEDS_FILEPATH, f"{seedInfo["Seed"]}.json")
    with open(outputFilepath, "w") as outputFile:
        json.dump(seedInfo, outputFile, indent=4)

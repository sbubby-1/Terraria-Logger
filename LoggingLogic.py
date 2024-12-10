import json
import os

from CustomExceptions.InvalidFolder import InvalidFolder
from ParseWorldFile import analyzeWorld
from WorldInfo import getSeedInfo

WORLDS_FOLDER_FILEPATH = "C:/Documents/My Games/Terraria/Worlds"
SAVED_SEEDS_FILEPATH = "C:/Documents/My Games/Terraria/Saved Seeds"
AUTOSAVE_FILEPATH = "Autosave.json"


def resetTriggered():
    if not (
        WORLDS_FOLDER_FILEPATH.endswith(r"/Terraria/Worlds")
        and os.path.exists(WORLDS_FOLDER_FILEPATH)
    ):
        raise InvalidFolder("Worlds")

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

    attemptAutosave()


def attemptAutosave():
    with open(AUTOSAVE_FILEPATH, "r") as file:
        autosaveRequirements = json.load(file, object_pairs_hook=dict)
        if not autosaveRequirements["Autosave Enabled"]:
            return

        seedInfo = getSeedInfo()

        for key, value in autosaveRequirements.items():
            match key:
                case "Autosave Enabled":
                    continue
                case "Minimum Pyramid Items":
                    if len(seedInfo["Pyramid Items"]) < value:
                        return
                case _:
                    if value and not seedInfo[key]:
                        return

        writeSeed(seedInfo)


def saveSeed():
    writeSeed(getSeedInfo())


def writeSeed(seedInfo):
    if not os.path.exists(SAVED_SEEDS_FILEPATH):
        os.makedirs(SAVED_SEEDS_FILEPATH)

    outputFilepath = os.path.join(SAVED_SEEDS_FILEPATH, f"{seedInfo["Seed"]}.json")
    with open(outputFilepath, "w") as outputFile:
        json.dump(seedInfo, outputFile, indent=4)

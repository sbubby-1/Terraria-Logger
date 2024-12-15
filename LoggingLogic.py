"""
Contains all logic pertaining to logging relevant info for a world.
"""

from CustomExceptions.InvalidFolder import InvalidFolder
from Display import drawWidgets
from ParseWorldFile import analyzeWorld
from WorldInfo import getSeedInfo
import json
import os

AUTOSAVE_FILEPATH = "Autosave.json"
SAVED_SEEDS_FILEPATH = "C:/Documents/My Games/Terraria/Saved Seeds"
WORLDS_FOLDER_FILEPATH = "C:/Documents/My Games/Terraria/Worlds"


def resetTriggered():
    """
    Looks through the world folder for .wld files. If one is found, it is
    analyzed and deleted. If the world file meets criteria toggled in
    ``Autosave.json``, its relevant info will be saved as a JSON in the Saved
    Seeds folder.
    """

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

    drawWidgets()

    attemptAutosave()


def attemptAutosave():
    """
    Checks to see if the most recently opened world meets autosave criteria. If
    so, it writes the relevant info to the saved seeds folder as a JSON.
    """

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
    """
    A function that exists to be passed in as an action for a keyboard shortcut
    without requiring a parameter.
    """

    writeSeed(getSeedInfo())


def writeSeed(seedInfo):
    """
    Writes a JSON file to the saved seeds folder.

    Parameters:
    ----------
    seedInfo: Dict
        A dictionary holding relevant info about the most recently analyzed seed.
    ----------
    """

    if not os.path.exists(SAVED_SEEDS_FILEPATH):
        os.makedirs(SAVED_SEEDS_FILEPATH)

    outputFilepath = os.path.join(SAVED_SEEDS_FILEPATH, f"{seedInfo["Seed"]}.json")
    with open(outputFilepath, "w") as outputFile:
        json.dump(seedInfo, outputFile, indent=4)

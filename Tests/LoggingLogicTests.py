import os
import shutil
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from CustomExceptions.InvalidFolder import InvalidFolder
from LoggingLogic import SAVED_SEEDS_FILEPATH, WORLDS_FOLDER_FILEPATH
from ParseWorldFile import analyzeWorld
from WorldFiles.Filepaths import WorldFilepaths
from WorldInfo import clearWorldInfo
import LoggingLogic
import WorldInfo


def runTests():
    numberOfTestsPassed = 0
    numberOfTests = 0

    if not resetTriggeredTest():
        print("resetTriggeredTest failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    if not attemptAutosaveQualificationsUnmetTest():
        print("attemptAutosaveQualificationsUnmetTest failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    if not attemptAutosaveQualificationsMetTest():
        print("attemptAutosaveQualificationsMetTest failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    if not saveSeedTest():
        print("saveSeedTest failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    return (numberOfTestsPassed, numberOfTests)


def saveSeedTest():
    try:
        clearSavedSeedsFolder()
    except InvalidFolder:
        print("saveSeedTest was not run because the Worlds folder filepath is invalid.")
        return False

    analyzeWorld(WorldFilepaths.SKELETRON.value.filepath)
    LoggingLogic.saveSeed()

    outputFilepath = os.path.join(
        SAVED_SEEDS_FILEPATH, f"{WorldInfo.relevantInfo["World Seed"]}.json"
    )

    if not os.path.exists(outputFilepath):
        return False

    return True


# Works under the current Autosave.json but may not work if you change qualifications
def attemptAutosaveQualificationsUnmetTest():
    try:
        clearSavedSeedsFolder()
    except InvalidFolder:
        print(
            "attemptAutosaveQualificationsUnmetTest was not run because the Worlds folder filepath is invalid."
        )
        return False

    analyzeWorld(WorldFilepaths.SKELETRON.value.filepath)

    LoggingLogic.attemptAutosave()

    outputFilepath = os.path.join(
        SAVED_SEEDS_FILEPATH, f"{WorldInfo.relevantInfo["World Seed"]}.json"
    )
    if os.path.exists(outputFilepath):
        return False

    return True


# Works under the current Autosave.json but may not work if you change qualifications
def attemptAutosaveQualificationsMetTest():
    try:
        clearSavedSeedsFolder()
    except InvalidFolder:
        print(
            "attemptAutosaveQualificationsMetTest was not run because the Worlds folder filepath is invalid."
        )
        return False

    analyzeWorld(WorldFilepaths.PLANTERA.value.filepath)

    LoggingLogic.attemptAutosave()

    outputFilepath = os.path.join(
        SAVED_SEEDS_FILEPATH, f"{WorldInfo.relevantInfo["World Seed"]}.json"
    )
    if not os.path.exists(outputFilepath):
        return False

    return True


def resetTriggeredTest():
    try:
        clearWorldsFolder()
    except InvalidFolder:
        print(
            "resetTriggeredTest was not run because the Worlds folder filepath is invalid."
        )
        return False

    shutil.copy(WorldFilepaths.DUKE_FISHRON.value.filepath, WORLDS_FOLDER_FILEPATH)

    clearWorldInfo()

    if WorldInfo.bossesSlain["Duke Fishron"]:
        return False

    LoggingLogic.resetTriggered()

    if not WorldInfo.bossesSlain["Duke Fishron"]:
        return False

    return True


def clearSavedSeedsFolder():
    if not os.path.exists(SAVED_SEEDS_FILEPATH):
        raise InvalidFolder("Saved Seeds Folder")

    savedSeedsFolder = os.listdir(SAVED_SEEDS_FILEPATH)

    for fileName in savedSeedsFolder:
        if fileName.endswith(".json"):
            worldFilepath = os.path.join(SAVED_SEEDS_FILEPATH, fileName)

            if os.path.isdir(worldFilepath):
                continue

            os.remove(worldFilepath)


def clearWorldsFolder():
    if not os.path.exists(WORLDS_FOLDER_FILEPATH):
        raise InvalidFolder("Worlds Folder")

    worldsFolder = os.listdir(WORLDS_FOLDER_FILEPATH)

    for fileName in worldsFolder:
        if fileName.endswith(".wld"):
            worldFilepath = os.path.join(WORLDS_FOLDER_FILEPATH, fileName)

            if os.path.isdir(worldFilepath):
                continue

            os.remove(worldFilepath)

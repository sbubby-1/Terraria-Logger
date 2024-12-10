import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import LoggingLogic
from LoggingLogic import WORLDS_FOLDER_FILEPATH


def runTests():
    numberOfTestsPassed = 0
    numberOfTests = 0

    if not resetTriggeredTest():
        print("resetTriggeredTest failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    return (numberOfTestsPassed, numberOfTests)


def resetTriggeredTest():
    success = True

    if not (
        WORLDS_FOLDER_FILEPATH.endswith(r"/Terraria/Worlds")
        and os.path.exists(WORLDS_FOLDER_FILEPATH)
    ):
        print(
            "resetTriggeredTest was not run because the Worlds folder filepath is invalid."
        )
        return False

    worldsFolderFiles = os.listdir(WORLDS_FOLDER_FILEPATH)

    for fileName in worldsFolderFiles:
        if fileName.endswith(".wld"):
            worldFilepath = os.path.join(WORLDS_FOLDER_FILEPATH, fileName)

            if os.path.isdir(worldFilepath):
                continue

            os.remove(worldFilepath)

    return success

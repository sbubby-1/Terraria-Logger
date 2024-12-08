import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import ParseWorldFile
from CustomExceptions.InvalidWorldFile import InvalidWorldFile
from WorldFiles.Filepaths import WorldFilepaths


def runTests():
    numberOfTestsPassed = 0
    numberOfTests = 0

    if not initializeOffsetsWithFreshWorld():
        print("initializeOffsetsWithFreshWorld failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    if not initializeOffsetsWithRevisedWorld():
        print("initializeOffsetsWithRevisedWorld failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    if not initializeOffsetsWithPlayerFile():
        print("initializeOffsetsWithPlayerFile failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    return (numberOfTestsPassed, numberOfTests)


def initializeOffsetsWithFreshWorld():
    success = True
    with open(WorldFilepaths.FRESH_WORLD.value.filepath, "rb") as file:
        try:
            ParseWorldFile.initializeOffsets(file)
            success = False
        except InvalidWorldFile as e:
            if e.message != "This is a fresh world.":
                success = False
    return success


def initializeOffsetsWithRevisedWorld():
    success = True
    with open(WorldFilepaths.PYRAMID.value.filepath, "rb") as file:
        try:
            ParseWorldFile.initializeOffsets(file)
        except InvalidWorldFile:
            success = False
    return success


def initializeOffsetsWithPlayerFile():
    success = True
    with open(WorldFilepaths.PLAYER.value.filepath, "rb") as file:
        try:
            ParseWorldFile.initializeOffsets(file)
            success = False
        except InvalidWorldFile:
            pass
    return success

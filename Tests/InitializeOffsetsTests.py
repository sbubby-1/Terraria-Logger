import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import ParseWorldFile
from CustomExceptions.InvalidWorldFile import InvalidWorldFile
from WorldFiles.Filepaths import WorldFilepaths


def initializeOffsetsWithFreshWorld():
    success = True
    with open(WorldFilepaths.FRESH_WORLD.value, "rb") as file:
        try:
            ParseWorldFile.initializeOffsets(file)
            success = False
        except InvalidWorldFile as e:
            if e.message != "This is a fresh world.":
                success = False
    return success


def initializeOffsetsWithRevisedWorld():
    success = True
    with open(WorldFilepaths.PYRAMID.value, "rb") as file:
        try:
            ParseWorldFile.initializeOffsets(file)
        except InvalidWorldFile:
            success = False
    return success

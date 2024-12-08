import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import Metadata
import ParseWorldFile
import WorldInfo
from WorldFiles.Filepaths import WorldFilepaths


def runTests():
    numberOfTestsPassed = 0
    numberOfTests = 0
    if not pyramidLootTests():
        print("pyramidLootTests failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    return (numberOfTestsPassed, numberOfTests)


def pyramidLootTests():
    success = True
    # Contains Sandstorm, Carpet, Pharaoh's
    containsPyramidItem = [False, False, False]

    with open(WorldFilepaths.PYRAMID.value.filepath, "rb") as file:
        offsets = ParseWorldFile.initializeOffsets(file)

        ParseWorldFile.processChests(file, offsets[Metadata.OffsetIndices.CHESTS.value])

        for item in WorldInfo.pyramidItems:
            match item.itemName:
                case "Sandstorm in a Bottle":
                    if item.chestX != 1528 or item.chestY != 298:
                        success = False
                    containsPyramidItem[0] = True
                case "Flying Carpet":
                    if item.chestX != 281 or item.chestY != 205:
                        success = False
                    containsPyramidItem[1] = True
                case "Pharoah's Mask":
                    if item.chestX != 2390 or item.chestY != 209:
                        success = False
                    containsPyramidItem[2] = True

    if not all(containsPyramidItem):
        success = False

    return success

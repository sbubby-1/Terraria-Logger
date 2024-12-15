import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from WorldFiles.Filepaths import WorldFilepaths
import Metadata
import ParseWorldFile
import WorldInfo


def runTests():
    numberOfTestsPassed = 0
    numberOfTests = 0

    if not haveNotTalkedToDemoTest():
        print("haveNotTalkedToDemoTest failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    if not talkedToDemoTest():
        print("talkedToDemoTest failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    return (numberOfTestsPassed, numberOfTests)


def haveNotTalkedToDemoTest():
    success = True

    with open(WorldFilepaths.PYRAMID.value.filepath, "rb") as file:
        offsets = ParseWorldFile.initializeOffsets(file)

        ParseWorldFile.processBestiary(
            file, offsets[Metadata.OffsetIndices.BESTIARY.value]
        )

        if WorldInfo.talkedToDemo == True:
            success = False

    return success


def talkedToDemoTest():
    success = True

    with open(WorldFilepaths.TALKED_TO_DEMOLITIONIST.value.filepath, "rb") as file:
        offsets = ParseWorldFile.initializeOffsets(file)

        ParseWorldFile.processBestiary(
            file, offsets[Metadata.OffsetIndices.BESTIARY.value]
        )

        if WorldInfo.talkedToDemo == False:
            success = False

    return success

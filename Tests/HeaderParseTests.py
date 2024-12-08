import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import Metadata
import ParseWorldFile
import WorldInfo
from WorldFiles.Filepaths import WorldFilepaths

HEADER_FIELD_COUNT = 152
RELEVANT_HEADER_FIELDS = 19


def runTests():
    numberOfTestsPassed = 0
    numberOfTests = 0
    if not initializeHeaderFieldsTests():
        print("initializeHeaderFieldsTests failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    if not processHeaderTests():
        print("processHeaderTests failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    return (numberOfTestsPassed, numberOfTests)


def initializeHeaderFieldsTests():
    success = True

    Metadata.initializeHeaderFields()

    if len(Metadata.headerFields.items()) != HEADER_FIELD_COUNT:
        success = False

    for key, value in Metadata.headerFields.items():
        if (
            type(key) != str
            or "type" not in value
            or "isRelevant" not in value
            or type(value["type"]) != str
            or type(value["isRelevant"]) != bool
        ):
            success = False
    return success


def processHeaderTests():
    success = True
    filesUsed = 0

    for worldFileEnum in WorldFilepaths:
        worldFile = worldFileEnum.value
        if worldFile.location != Metadata.OffsetIndices.HEADER.value:
            continue

        filesUsed += 1
        file = open(worldFile.filepath, "rb")
        offsets = ParseWorldFile.initializeOffsets(file)

        ParseWorldFile.processHeader(file, offsets[Metadata.OffsetIndices.HEADER.value])

        if WorldInfo.relevantInfo[worldFile.headerField] == False:
            success = False
        if worldFile.headerField in WorldInfo.bossesSlain:
            if WorldInfo.bossesSlain[worldFile.headerField] == False:
                success = False

        for boss in WorldInfo.bossesSlain.keys():
            WorldInfo.bossesSlain[boss] = False
        WorldInfo.relevantInfo.clear()

        file.close()

    if filesUsed != RELEVANT_HEADER_FIELDS:
        success = False

    return success

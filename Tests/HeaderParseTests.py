import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import Metadata
import ParseWorldFile
import WorldInfo
from WorldFiles.Filepaths import WorldFilepaths

# expectedHeaderFieldCount = 153


def initializeHeaderFieldsTests():
    success = True

    Metadata.initializeHeaderFields()

    # if expectedHeaderFieldCount != 153:
    #     success = False

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

    if filesUsed != 19:
        success = False

    return success

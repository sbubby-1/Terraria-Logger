import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import Metadata
import ParseWorldFile
import WorldInfo

expectedHeaderFieldCount = 153


def initializeHeaderFieldsTests():
    success = True

    Metadata.initializeHeaderFields()

    if expectedHeaderFieldCount != 153:
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

    file = open("./WorldFiles/PostShimmerWorld.wld", "rb")
    offsets = ParseWorldFile.initializeOffsets(file)

    ParseWorldFile.processHeader(file, offsets[Metadata.OffsetIndices.HEADER.value])

    for key, value in WorldInfo.bossesSlain.items():
        print(f"{key} : {value}")

    for key, value in WorldInfo.relevantInfo.items():
        print(f"{key} : {value}")

    print()

    file.close()

    return success

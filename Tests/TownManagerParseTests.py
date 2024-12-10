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

    if not noHousingBuiltTests():
        print("noHousingBuiltTests failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    if not housingBuiltTests():
        print("housingBuiltTests failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    if not guideInHellTests():
        print("guideInHellTests failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    if not npcAtShimmerTests():
        print("npcAtShimmerTests failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    return (numberOfTestsPassed, numberOfTests)


def noHousingBuiltTests():
    success = True

    with open(WorldFilepaths.SKELETRON.value.filepath, "rb") as file:
        offsets = ParseWorldFile.initializeOffsets(file)
        ParseWorldFile.processHeader(file, offsets[Metadata.OffsetIndices.HEADER.value])

        ParseWorldFile.processTownManager(
            file, offsets[Metadata.OffsetIndices.TOWN_MANAGER.value]
        )

        if WorldInfo.housingBuilt == True or WorldInfo.guideInHell == True:
            success = False

    return success


def housingBuiltTests():
    success = True

    with open(WorldFilepaths.HOUSING_BUILT.value.filepath, "rb") as file:
        offsets = ParseWorldFile.initializeOffsets(file)
        ParseWorldFile.processHeader(file, offsets[Metadata.OffsetIndices.HEADER.value])

        ParseWorldFile.processTownManager(
            file, offsets[Metadata.OffsetIndices.TOWN_MANAGER.value]
        )

        if WorldInfo.housingBuilt == False or WorldInfo.guideInHell == True:
            success = False

    return success


def guideInHellTests():
    success = True

    with open(WorldFilepaths.HELL_BED_BUILT.value.filepath, "rb") as file:
        offsets = ParseWorldFile.initializeOffsets(file)
        ParseWorldFile.processHeader(file, offsets[Metadata.OffsetIndices.HEADER.value])

        ParseWorldFile.processTownManager(
            file, offsets[Metadata.OffsetIndices.TOWN_MANAGER.value]
        )

        if WorldInfo.guideInHell == False:
            success = False

    return success


def npcAtShimmerTests():
    success = True

    with open(WorldFilepaths.NPC_AT_SHIMMER.value.filepath, "rb") as file:
        offsets = ParseWorldFile.initializeOffsets(file)
        ParseWorldFile.processHeader(file, offsets[Metadata.OffsetIndices.HEADER.value])

        ParseWorldFile.processTownManager(
            file, offsets[Metadata.OffsetIndices.TOWN_MANAGER.value]
        )

        if WorldInfo.npcAtShimmer == False:
            success = False

    return success

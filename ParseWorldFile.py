import Metadata
import ReadDataTypes
import WorldInfo
from CustomExceptions.CorruptedChestData import CorruptedChestData
from CustomExceptions.InvalidDataType import InvalidDataType
from CustomExceptions.InvalidWorldFile import InvalidWorldFile


def analyzeWorld(filepath):
    file = open(filepath, "rb")
    offsets = initializeOffsets(file)

    processHeader(file, offsets[Metadata.OffsetIndices.HEADER.value])
    processChests(file, offsets[Metadata.OffsetIndices.CHESTS.value])

    file.close()


def processChests(file, chestsOffset):
    file.seek(chestsOffset, 0)

    numberOfChests = ReadDataTypes.readInt16(file)
    slotsPerChest = ReadDataTypes.readInt16(file)

    # I don't think storage items that store more or less than 40 items exist?
    # This is probably for older versions of the game, but I'll leave it in for safety.
    leftoverSlots = max(0, slotsPerChest - 40)
    slotsPerChest = min(40, slotsPerChest)

    for _ in range(numberOfChests):
        chestX = ReadDataTypes.readInt32(file)
        chestY = ReadDataTypes.readInt32(file)
        # The name of the chest.
        _ = ReadDataTypes.readString(file)

        for slotNumber in range(slotsPerChest):
            stackSize = ReadDataTypes.readInt16(file)
            if stackSize < 0:
                raise CorruptedChestData()

            if stackSize > 0:
                # Pyramid loot is primary loot.
                # It will be in slot 0 of a chest, unless manually stored by a player.
                if slotNumber == 0:
                    itemID = ReadDataTypes.readInt32(file)
                    # Item prefix
                    _ = ReadDataTypes.readByte(file)

                    checkIfItemIsPyramidLoot(itemID, chestX, chestY)
                else:
                    file.seek(5, 1)

        for _ in range(leftoverSlots):
            stackSize = ReadDataTypes.readInt16(file)
            if stackSize < 0:
                raise CorruptedChestData()

            if stackSize > 0:
                file.seek(5, 1)


def checkIfItemIsPyramidLoot(itemID, chestX, chestY):
    pyramidItem = None
    match itemID:
        case 848:
            pyramidItem = Metadata.PyramidItem("Pharoah's Mask", chestX, chestY)
        case 857:
            pyramidItem = Metadata.PyramidItem("Sandstorm in a Bottle", chestX, chestY)
        case 934:
            pyramidItem = Metadata.PyramidItem("Flying Carpet", chestX, chestY)

    if pyramidItem != None:
        WorldInfo.pyramidItems.append(pyramidItem)


def processHeader(file, headerOffset):
    file.seek(headerOffset, 0)
    Metadata.initializeHeaderFields()

    multiplier = 1
    for field, value in Metadata.headerFields.items():
        dataType = value["type"]
        isRelevant = value["isRelevant"]

        if field in Metadata.MULTIPLIER_FIELDS:
            multiplier = process(file, dataType)
            continue

        for _ in range(multiplier):
            if isRelevant:
                processedValue = process(file, dataType)

                WorldInfo.relevantInfo[field] = processedValue

                if field in WorldInfo.bossesSlain:
                    WorldInfo.bossesSlain[field] = processedValue
            else:
                skipPast(file, dataType)
        multiplier = 1


def process(file, dataType):
    match dataType:
        case "Byte":
            return ReadDataTypes.readByte(file)
        case "Bool":
            return ReadDataTypes.readBoolean(file)
        case "Int16":
            return ReadDataTypes.readInt16(file)
        case "Int32":
            return ReadDataTypes.readInt32(file)
        case "Int64":
            return ReadDataTypes.readInt64(file)
        case "Single":
            return ReadDataTypes.readSingle(file)
        case "Double":
            return ReadDataTypes.readDouble(file)
        case "String":
            return ReadDataTypes.readString(file)
        case _:
            raise InvalidDataType(dataType)


def skipPast(file, dataType):
    match dataType:
        case "String":
            _ = ReadDataTypes.readString(file)
        case _:
            file.seek(Metadata.sizeOf(dataType), 1)


def initializeOffsets(file):
    version = ReadDataTypes.readInt32(file)
    # 1.4.4.9 = 279
    if version < 267:
        raise InvalidWorldFile(
            "This file version is outdated. This tool is built for 1.4.4.9."
        )

    num = ReadDataTypes.readInt64(file)

    # 7 byte Re-Logic stamp
    if (num & 0xFFFFFFFFFFFFFF) != 27981915666277746:
        raise InvalidWorldFile("Expected Re-Logic file format.")

    fileType = (num >> 56) & 0xFF
    if fileType != 2:
        fileTypeString = "unidentified"
        match fileType:
            case 0:
                fileTypeString = "None"
            case 1:
                fileTypeString = "Map"
            case 3:
                fileTypeString = "Player"

        raise InvalidWorldFile("The filetype is " + fileTypeString)

    # Number of times the file has been edited
    revision = ReadDataTypes.readInt32(file)
    if revision <= 1:
        raise InvalidWorldFile("This is a fresh world.")

    # Whether this world has been favorited.
    # It uses 8 bytes, but only the last byte is relevant.
    file.seek(8, 1)

    # Number of sections in the file
    numberOfSections = ReadDataTypes.readInt16(file)

    # Offset to each section
    offsets = []
    for _ in range(numberOfSections):
        curr_offset = ReadDataTypes.readInt32(file)
        offsets.append(curr_offset)

    return offsets

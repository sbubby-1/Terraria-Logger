import Metadata
import ReadDataTypes
import WorldInfo
from CustomExceptions.InvalidDataType import InvalidDataType
from CustomExceptions.InvalidWorldFile import InvalidWorldFile


def analyzeWorld(filepath):
    file = open(filepath, "rb")
    offsets = initializeOffsets(file)

    processHeader(file, offsets[Metadata.OffsetIndices.HEADER.value])

    file.close()


def processHeader(file, headerOffset):
    file.seek(headerOffset, 0)
    Metadata.initializeHeaderFields()

    multiplier = 1
    for field, value in Metadata.headerFields.items():
        dataType = value["type"]
        isRelevant = value["isRelevant"]

        if field in Metadata.multiplierFields:
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

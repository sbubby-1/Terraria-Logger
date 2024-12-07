import ReadDataTypes
from CustomExceptions.InvalidWorldFile import InvalidWorldFile


def initializeOffsets(file):
    version = ReadDataTypes.readInt(file)
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
    revision = ReadDataTypes.readInt(file)
    if revision <= 1:
        raise InvalidWorldFile("This is a fresh world.")

    # Whether this world has been favorited.
    # It uses 8 bytes, but only the last byte is relevant.
    file.seek(8, 1)

    # Number of sections in the file
    numberOfSections = ReadDataTypes.readShort(file)

    # Offset to each section
    # 0. Header
    # 1. Tile Data
    # 2. Chests
    # 3. Signs
    # 4. NPCs
    # 5. Entities
    # 6. Pressure Plates
    # 7. Town Manager
    # 8. Bestiary
    # 9. Journey Powers
    offsets = []
    for _ in range(numberOfSections):
        curr_offset = ReadDataTypes.readInt(file)
        offsets.append(curr_offset)

    return offsets

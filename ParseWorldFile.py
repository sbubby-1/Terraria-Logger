from CustomExceptions.CorruptedChestData import CorruptedChestData
from CustomExceptions.InitializationFailed import InitializationFailed
from CustomExceptions.InvalidDataType import InvalidDataType
from CustomExceptions.InvalidWorldFile import InvalidWorldFile
import Metadata
import ReadDataTypes
import WorldInfo


def analyzeWorld(filepath):
    """
    Analyzes the world and stores relevant info in ``WorldInfo`` fields.

    Parameters:
    ---------
    filepath: String
        The filepath to the world file to be analyzed.
    ---------
    """

    WorldInfo.clearWorldInfo()
    file = open(filepath, "rb")

    try:
        # Contains the byte offset from the start of the file to each section.
        offsets = initializeOffsets(file)

        processHeader(file, offsets[Metadata.OffsetIndices.HEADER.value])
        processChests(file, offsets[Metadata.OffsetIndices.CHESTS.value])
        processTownManager(file, offsets[Metadata.OffsetIndices.TOWN_MANAGER.value])
        processBestiary(file, offsets[Metadata.OffsetIndices.BESTIARY.value])
    except (
        CorruptedChestData,
        InitializationFailed,
        InvalidDataType,
        InvalidWorldFile,
    ) as e:
        print(e.message)

    file.close()


def processBestiary(file, offset):
    """
    Processes the Bestiary section of the world file.

    Parameters:
    ----------
    file: File
        The file to be analyzed.
    offset: Int
        The byte offset to this section of the world file.
    ----------
    """

    file.seek(offset, 0)

    numberOfKills = ReadDataTypes.readInt32(file)
    for _ in range(numberOfKills):
        # NPC Name
        _ = ReadDataTypes.readString(file)
        # Number of times killed
        file.seek(4, 1)

    numberSeen = ReadDataTypes.readInt32(file)
    for _ in range(numberSeen):
        # NPC Name
        _ = ReadDataTypes.readString(file)

    numberOfNPCsTalkedTo = ReadDataTypes.readInt32(file)
    for _ in range(numberOfNPCsTalkedTo):
        npcName = ReadDataTypes.readString(file)

        if npcName == "Demolitionist":
            WorldInfo.talkedToDemo = True


def processTownManager(file, offset):
    """
    Processes the Town Manager section of the world file.

    Parameters:
    ----------
    file: File
        The file to be analyzed.
    offset: Int
        The byte offset to this section of the world file.
    ----------
    """

    file.seek(offset, 0)

    if WorldInfo.bossesSlain["Wall of Flesh"]:
        WorldInfo.housingBuilt = True
        WorldInfo.guideInHell = True

    numberOfRooms = ReadDataTypes.readInt32(file)
    worldWidth = WorldInfo.relevantInfo["World Width"]

    for _ in range(numberOfRooms):
        npcID = ReadDataTypes.readInt32(file)
        npcX = ReadDataTypes.readInt32(file)
        npcY = ReadDataTypes.readInt32(file)

        try:
            if (
                npcX < worldWidth * 0.2 + 100 or npcX > worldWidth * 0.8 - 100
            ) and npcY > WorldInfo.relevantInfo["World Surface Y"]:
                WorldInfo.npcAtShimmer = True

            # Guide ID
            if npcID == 22:
                WorldInfo.housingBuilt = True

                worldHeight = WorldInfo.relevantInfo["World Height"]

                if npcY > worldHeight * 0.75:
                    WorldInfo.guideInHell = True

        except Exception:
            raise InitializationFailed()


def processChests(file, offset):
    """
    Processes the Chests section of the world file.

    Parameters:
    ----------
    file: File
        The file to be analyzed.
    offset: Int
        The byte offset to this section of the world file.
    ----------
    """

    file.seek(offset, 0)

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
    """
    Checks if the items is a Pyramid item, and if so, adds it to
    ``WorldInfo.pyramidItems``.
    """

    pyramidItem = None
    match itemID:
        case 848:
            pyramidItem = Metadata.PyramidItem("Pharaoh's Mask", chestX, chestY)
        case 857:
            pyramidItem = Metadata.PyramidItem("Sandstorm in a Bottle", chestX, chestY)
        case 934:
            pyramidItem = Metadata.PyramidItem("Flying Carpet", chestX, chestY)

    if pyramidItem != None:
        WorldInfo.pyramidItems.append(pyramidItem)


def processHeader(file, offset):
    """
    Processes the Header section of the world file.

    Parameters:
    ----------
    file: File
        The file to be analyzed.
    offset: Int
        The byte offset to this section of the world file.
    ----------
    """

    file.seek(offset, 0)
    Metadata.initializeHeaderFields()

    multiplier = 1
    for field, value in Metadata.headerFields.items():
        dataType = value["type"]
        isRelevant = value["isRelevant"]

        # Some fields, such as ``Number of Partiers``, are stored in two parts.
        # The second is a non-fixed-size array, and the first is the number of
        # elements in the array.
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
    """
    Processes and returns the next value in the file.

    Parameters:
    ----------
    file: File
        The file to be analyzed.
    dataType: String
        The dataType of the next value in String form.
    ----------
    Returns: Variable data type
        The value read in.
    """

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
    """
    Skips past the next value in the file.

    Parameters:
    ----------
    file: File
        The file to be analyzed.
    dataType: String
        The dataType of the next value in String form.
    ----------
    """

    match dataType:
        case "String":
            _ = ReadDataTypes.readString(file)
        case _:
            file.seek(Metadata.sizeOf(dataType), 1)


def initializeOffsets(file):
    """
    Reads the initial section of the world file and initializes ``offsets``,
    which contains the byte offsets to each section of the file.

    Parameters:
    ----------
    file: File
        The file to be analyzed.
    ----------
    Returns: [Int]
        An array holding the byte offset to each section of the file.
    """

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

"""
Contains logic for various metadata pertaining to world file reading.
"""

from collections import OrderedDict
from enum import Enum
import json

headerFields = OrderedDict()

HEADER_VALUES_FILEPATH = "HeaderValues.json"
MULTIPLIER_FIELDS = {
    "Number of Players",
    "Kill Count Length",
    "Number of Partiers",
    "Number of Tree Tops",
}
PYRAMID_ITEM_IDS = {848, 857, 866, 934}


def initializeHeaderFields():
    """
    Reads in HeaderValues.json, which lists the field name, relevance and data
    type for each field in the header section of a world file.
    """

    with open(HEADER_VALUES_FILEPATH, "r") as file:
        global headerFields
        headerFields = json.load(file, object_pairs_hook=OrderedDict)


def sizeOf(dataType):
    """
    Returns the byte size of the provided data type.

    Parameters:
    ----------
    dataType: String
        The data type in String format. A space-separated multiplier can follow
        the data type.
    ----------
    """

    match dataType:
        case "Byte":
            return 1
        case "Bool":
            return 1
        case "Int16":
            return 2
        case "Int32":
            return 4
        case "Int64":
            return 8
        case "Single":
            return 4
        case "Double":
            return 8
        case "Rect":
            return 16
        # This case is for "dataType multiplier".
        case _:
            dataType, multiplier = dataType.split(" ")
            return int(multiplier) * sizeOf(dataType)


class PyramidItem:
    """
    A class that holds relevant info for a pyramid item.
    """

    def __init__(self, itemName, chestX, chestY):
        self.itemName = itemName
        self.chestX = chestX
        self.chestY = chestY


class OffsetIndices(Enum):
    """
    An Enumerable that holds the corresponding index for each section of the
    world file in the ``offsets`` array.
    """

    INITIALIZATION = -1
    HEADER = 0
    TILE_DATA = 1
    CHESTS = 2
    SIGNS = 3
    NPCS = 4
    ENTITIES = 5
    PRESSURE_PLATES = 6
    TOWN_MANAGER = 7
    BESTIARY = 8
    JOURNEY_POWERS = 9

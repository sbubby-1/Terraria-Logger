import json
from collections import OrderedDict
from enum import Enum

headerValuesFilepath = "HeaderValues.json"

headerFields = OrderedDict()

multiplierFields = {
    "Number of Players",
    "Kill Count Length",
    "Number of Partiers",
    "Number of Tree Tops",
}


def initializeHeaderFields():
    with open(headerValuesFilepath, "r") as file:
        global headerFields
        headerFields = json.load(file, object_pairs_hook=OrderedDict)


def sizeOf(dataType):
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
        case _:
            dataType, multiplier = dataType.split(" ")
            return int(multiplier) * sizeOf(dataType)


class OffsetIndices(Enum):
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

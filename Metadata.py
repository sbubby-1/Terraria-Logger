import json
from collections import OrderedDict
from enum import Enum

import ReadDataTypes
from CustomExceptions.InvalidDataType import InvalidDataType

headerValuesFilepath = "HeaderValues.json"

headerFields = OrderedDict()


def initializeHeaderFields():
    with open(headerValuesFilepath, "r") as file:
        global headerFields
        headerFields = json.load(file, object_pairs_hook=OrderedDict)


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


def sizeOf(dataType):
    match dataType:
        case "Byte":
            return 1
        case "Bool":
            return 2
        case "Int16":
            return 4
        case "Int32":
            return 4
        case "Int64":
            return 8
        case "Single":
            return 4
        case "Double":
            return 8
        case _:
            dataType, multiplier = dataType.split(" ")
            return multiplier * sizeOf(dataType)


class OffsetIndices(Enum):
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

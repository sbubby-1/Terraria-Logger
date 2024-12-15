"""
Contains functions for parsing and returning the values of various data types.
"""

import struct


def readString(file):
    # Length of the decoded String
    length = 0

    # Position of the current bit (in multiples of 7)
    shift = 0
    while True:
        # Read the first byte, extracts the lower 7 bits and shifts them into
        # position, combines them with length.
        byte = file.read(1)[0]
        length |= (byte & 0x7F) << shift

        # If this is the 8th bit of the byte, it is the last bit of the length.
        if (byte & 0x80) == 0:
            break

        shift += 7

    data = file.read(length)
    return data.decode("utf-8")


def readBoolean(file):
    byte = readByte(file)
    return byte != 0


def readInt16(file):
    data = file.read(2)
    return struct.unpack("<H", data)[0]


def readInt32(file):
    data = file.read(4)
    return struct.unpack("<I", data)[0]


def readInt64(file):
    data = file.read(8)
    return struct.unpack("<Q", data)[0]


def readSingle(file):
    data = file.read(4)
    return struct.unpack("<f", data)[0]


def readDouble(file):
    data = file.read(8)
    return struct.unpack("<d", data)[0]


def readByte(file):
    data = file.read(1)
    return struct.unpack("<B", data)[0]

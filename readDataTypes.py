import struct


def readString(file):
    length = 0
    shift = 0
    while True:
        byte = file.read(1)[0]
        length |= (byte & 0x7F) << shift
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

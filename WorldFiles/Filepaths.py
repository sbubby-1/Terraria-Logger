import os
import sys
from enum import Enum

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import Metadata


class WorldFile:
    def __init__(self, filepath, headerField, location):
        self.filepath = filepath
        self.headerField = headerField
        self.location = location


class WorldFilepaths(Enum):
    DEERCLOPS = WorldFile(
        "./WorldFiles/Deerclops.wld", "Deerclops", Metadata.OffsetIndices.HEADER.value
    )
    DUKE_FISHRON = WorldFile(
        "./WorldFiles/DukeFishron.wld",
        "Duke Fishron",
        Metadata.OffsetIndices.HEADER.value,
    )
    EMPRESS_OF_LIGHT = WorldFile(
        "./WorldFiles/EmpressOfLight.wld",
        "Empress of Light",
        Metadata.OffsetIndices.HEADER.value,
    )
    EVIL_BOSS = WorldFile(
        "./WorldFiles/EvilBoss.wld", "Evil Boss", Metadata.OffsetIndices.HEADER.value
    )
    EYE_OF_CTHULHU = WorldFile(
        "./WorldFiles/EvilBoss.wld",
        "Eye of Cthulhu",
        Metadata.OffsetIndices.HEADER.value,
    )
    FRESH_WORLD = WorldFile(
        "./WorldFiles/Fresh.wld", None, Metadata.OffsetIndices.INITIALIZATION.value
    )
    GOLEM = WorldFile(
        "./WorldFiles/Golem.wld",
        "Golem",
        Metadata.OffsetIndices.HEADER.value,
    )
    HELL_BED_BUILT = WorldFile(
        "./WorldFiles/HellBetBuilt.wld",
        None,
        Metadata.OffsetIndices.TOWN_MANAGER.value,
    )
    HOUSING_BUILT = WorldFile(
        "./WorldFiles/HousingBuilt.wld",
        None,
        Metadata.OffsetIndices.TOWN_MANAGER.value,
    )
    KING_SLIME = WorldFile(
        "./WorldFiles/KingSlime.wld",
        "King Slime",
        Metadata.OffsetIndices.HEADER.value,
    )
    LUNATIC_CULTIST = WorldFile(
        "./WorldFiles/LunaticCultist.wld",
        "Lunatic Cultist",
        Metadata.OffsetIndices.HEADER.value,
    )
    MOON_LORD = WorldFile(
        "./WorldFiles/MoonLord.wld",
        "Moon Lord",
        Metadata.OffsetIndices.HEADER.value,
    )
    PLANTERA = WorldFile(
        "./WorldFiles/Plantera.wld",
        "Plantera",
        Metadata.OffsetIndices.HEADER.value,
    )
    PLAYER = WorldFile(
        "./WorldFiles/Player.wld",
        None,
        Metadata.OffsetIndices.INITIALIZATION.value,
    )
    PYRAMID = WorldFile(
        "./WorldFiles/Pyramid.wld", None, Metadata.OffsetIndices.CHESTS.value
    )
    QUEEN_BEE = WorldFile(
        "./WorldFiles/QueenBee.wld",
        "Queen Bee",
        Metadata.OffsetIndices.HEADER.value,
    )
    QUEEN_SLIME = WorldFile(
        "./WorldFiles/QueenSlime.wld",
        "Queen Slime",
        Metadata.OffsetIndices.HEADER.value,
    )
    SAVED_MECHANIC = WorldFile(
        "./WorldFiles/SavedMechanic.wld",
        "Saved Mechanic",
        Metadata.OffsetIndices.HEADER.value,
    )
    SAVED_WIZARD = WorldFile(
        "./WorldFiles/SavedWizard.wld",
        "Saved Wizard",
        Metadata.OffsetIndices.HEADER.value,
    )
    SKELETRON = WorldFile(
        "./WorldFiles/Skeletron.wld",
        "Skeletron",
        Metadata.OffsetIndices.HEADER.value,
    )
    SKELETRON_PRIME = WorldFile(
        "./WorldFiles/SkeletronPrime.wld",
        "Skeletron Prime",
        Metadata.OffsetIndices.HEADER.value,
    )
    TALKED_TO_DEMOLITIONIST = WorldFile(
        "./WorldFiles/TalkedToDemo.wld",
        None,
        Metadata.OffsetIndices.BESTIARY.value,
    )
    THE_DESTROYER = WorldFile(
        "./WorldFiles/TheDestroyer.wld",
        "The Destroyer",
        Metadata.OffsetIndices.HEADER.value,
    )
    THE_TWINS = WorldFile(
        "./WorldFiles/TheTwins.wld",
        "The Twins",
        Metadata.OffsetIndices.HEADER.value,
    )
    WALL_OF_FLESH = WorldFile(
        "./WorldFiles/WallOfFlesh.wld",
        "Wall of Flesh",
        Metadata.OffsetIndices.HEADER.value,
    )

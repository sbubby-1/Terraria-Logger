"""
Contains relevant info regarding an analyzed seed.
"""

from CustomExceptions.InitializationFailed import InitializationFailed

# Relevant info from the ``Header`` section of the world file. Fields are
# tagged as relevant in ``HeaderValues.json``.
relevantInfo = {}

# An array of ``PyramidItem``s.
pyramidItems = []

# Whether housing has been built in this world at all.
housingBuilt = False

# Whether the player has talked to the Demolitionist.
talkedToDemo = False

# Whether the Guide has been housed in the Underworld.
guideInHell = False

# Whether there is an NPC housed at shimmer.
npcAtShimmer = False

# Tracks which bosses have been killed.
bossesSlain = {
    "Deerclops": False,
    "Duke Fishron": False,
    "Empress of Light": False,
    "Evil Boss": False,
    "Eye of Cthulhu": False,
    "Golem": False,
    "King Slime": False,
    "Lunatic Cultist": False,
    "Moon Lord": False,
    "Plantera": False,
    "Queen Bee": False,
    "Queen Slime": False,
    "Skeletron Prime": False,
    "Skeletron": False,
    "The Destroyer": False,
    "The Twins": False,
    "Wall of Flesh": False,
}


def clearWorldInfo():
    """
    Resets WorldInfo to its original state.
    """

    for key in bossesSlain:
        bossesSlain[key] = False

    relevantInfo.clear()
    pyramidItems.clear()

    global housingBuilt
    housingBuilt = False

    global talkedToDemo
    talkedToDemo = False

    global guideInHell
    guideInHell = False

    global npcAtShimmer
    npcAtShimmer = False


def getSeedInfo():
    """
    Returns info that will be saved to a JSON.

    Returns: Dict
        A Dictionary holding relevant info with values formatted in the style
        they'll appear in the saved JSON.
    """

    seedInfo = {}

    try:
        seedInfo["Seed"] = relevantInfo["World Seed"]
        seedInfo["Dungeon Side"] = (
            "Right" if relevantInfo["Dungeon X"] > relevantInfo["Spawn X"] else "Left"
        )
        seedInfo["Pyramid Items"] = []
        for item in pyramidItems:
            distanceFromSpawn = item.chestX - relevantInfo["Spawn X"]
            directionFromSpawn = "right" if distanceFromSpawn > 0 else "left"
            seedInfo["Pyramid Items"].append(
                f"{item.itemName} {abs(distanceFromSpawn)} blocks {directionFromSpawn} of spawn."
            )

        seedInfo["Built Housing"] = housingBuilt
        seedInfo["Talked to Demo"] = talkedToDemo
        seedInfo["Guide In Hell"] = guideInHell
        seedInfo["Skeletron Killed"] = bossesSlain["Skeletron"]
        seedInfo["Saved Mechanic/Wizard"] = (
            relevantInfo["Saved Wizard"] or relevantInfo["Saved Mechanic"]
        )
        seedInfo["Hardmode Reached"] = bossesSlain["Wall of Flesh"]
        seedInfo["NPC at Shimmer"] = npcAtShimmer
        seedInfo["Destroyer Killed"] = bossesSlain["The Destroyer"]
        seedInfo["Mechs Killed"] = (
            bossesSlain["The Destroyer"]
            and bossesSlain["The Twins"]
            and bossesSlain["Skeletron Prime"]
        )
        seedInfo["Plantera Killed"] = bossesSlain["Plantera"]
        seedInfo["Golem Killed"] = bossesSlain["Golem"]
        seedInfo["Lunatic Cultist Killed"] = bossesSlain["Lunatic Cultist"]
        seedInfo["Moon Lord Killed"] = bossesSlain["Moon Lord"]

    except KeyError:
        raise InitializationFailed()

    return seedInfo

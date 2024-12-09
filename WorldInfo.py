from CustomExceptions.InitializationFailed import InitializationFailed

relevantInfo = {}
pyramidItems = []
housingBuilt = False
guideInHell = False
npcAtShimmer = False
talkedToDemo = False

bossesSlain = {
    "Eye of Cthulhu": False,
    "Evil Boss": False,
    "Skeletron": False,
    "Queen Bee": False,
    "The Destroyer": False,
    "The Twins": False,
    "Skeletron Prime": False,
    "Plantera": False,
    "Golem": False,
    "King Slime": False,
    "Wall of Flesh": False,
    "Lunatic Cultist": False,
    "Moon Lord": False,
    "Empress of Light": False,
    "Queen Slime": False,
    "Deerclops": False,
}


def getSeedInfo():
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

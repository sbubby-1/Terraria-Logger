import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ParseWorldFile import analyzeWorld
from WorldFiles.Filepaths import WorldFilepaths
import WorldInfo


def runTests():
    numberOfTestsPassed = 0
    numberOfTests = 0

    if not getSeedInfoTests():
        print("getSeedInfoTests failed. \n")
    else:
        numberOfTestsPassed += 1
    numberOfTests += 1

    return (numberOfTestsPassed, numberOfTests)


def getSeedInfoTests():
    analyzeWorld(WorldFilepaths.PLANTERA.value.filepath)

    seedInfo = WorldInfo.getSeedInfo()

    for key, value in seedInfo.items():
        match key:
            case "Seed":
                if value != "1334898976":
                    return False
            case "Dungeon Side":
                if value != "Right":
                    return False
            case "Pyramid Items":
                if len(value) != 3:
                    return False
            case "Built Housing":
                if value != True:
                    return False
            case "Talked to Demo":
                if value != False:
                    return False
            case "Guide In Hell":
                if value != True:
                    return False
            case "Skeletron Killed":
                if value != True:
                    return False
            case "Saved Mechanic/Wizard":
                if value != True:
                    return False
            case "Hardmode Reached":
                if value != True:
                    return False
            case "NPC at Shimmer":
                if value != False:
                    return False
            case "Destroyer Killed":
                if value != True:
                    return False
            case "Mechs Killed":
                if value != True:
                    return False
            case "Plantera Killed":
                if value != True:
                    return False
            case "Golem Killed":
                if value != False:
                    return False
            case "Lunatic Cultist Killed":
                if value != False:
                    return False
            case "Moon Lord Killed":
                if value != False:
                    return False
    return True

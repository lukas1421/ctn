import re
import unicodedata

from regex import getEstateFull, getBuildingEstate

dict1 = {'10': '十', '11': '十一', '1': '一', '2': '二', '3': '三', '4': '四',
         '5': '五', '6': '六', '7': '七', '8': '八', '9': '九'}


def normalize(s):
    # for i in dict1.keys():
    #     s = s.replace(i, dict1[i])
    return unicodedata.normalize('NFKC', s)


def getConfirmedDict(fileName):
    with open(fileName, "r") as file:
        lines = file.read().rstrip().splitlines()

    regionEstates = {}

    for line in lines:
        if '地區' in line:
            continue

        line = line.replace("(", "").replace(")", "")

        [region, estateFull] = getEstateFull(line)
        [estate, building, resType] = getBuildingEstate(estateFull)

        if region not in regionEstates:
            regionEstates[region] = {}

        building = estate if building == "" else building

        if estate not in regionEstates[region]:
            regionEstates[region][estate] = []
        if building not in regionEstates[region][estate]:
            regionEstates[region][estate].append(building)

    return regionEstates


def getQuarantineDict(fileName):
    with open(fileName, "r") as file:
        lines = file.read().rstrip().splitlines()

    regionEstates = {}

    for line in lines:

        line = line.replace("(", "").replace(")", "")

        [region, estateFull] = getEstateFull(line)
        [estate, building, resType] = getBuildingEstate(estateFull)

        if region not in regionEstates:
            regionEstates[region] = {}

        building = estate if building == "" else building

        if estate not in regionEstates[region]:
            regionEstates[region][estate] = []
        if building not in regionEstates[region][estate]:
            regionEstates[region][estate].append(building)

    return regionEstates

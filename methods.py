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



        # patternRegionBuilding = re.compile(r'^(.*?)\s+(.*?)$')
        # resRegionBuilding = patternRegionBuilding.match(line)
        #
        # patternEstates = re.compile(r"([\u4E00-\u9FA5]+[苑|邨|花園])([\u4E00-\u9FA5]+[樓|閣|苑].*?)$")
        # # patternEstates = re.compile(r"([\u4E00-\u9FA5]+苑|[\u4E00-\u9FA5]+邨)(.*?)$")
        # patternSingleBuilding = re.compile(r"^(\S+)$")
        # patternPhase = re.compile(r"^(.*?期)\s*(.*?)$")
        # patternEnglish = re.compile(r"([^第]+)\s*(第*\S+\s*座)+$")
        # patternNonestates = re.compile(r"^(.+)$")
        #
        # # patternEnglish = re.compile(r"([^\d第]+)\s+(\S+\s*座)$")
        # # patternEnglish = re.compile(r"([^\d第]+)\s*(第*.*座)*$")
        # # patternNonestates = re.compile(r"([^\s]+)\s*(.*?)$")
        # # patternEnglish = re.compile(r"([^\d第]+)\s*(第*\S+\s*座)+$")
        # # patternEnglish = re.compile(r'^(.*?)\s\d+')
        # # patternEnglish = re.compile(r'^(.*?)\s[第|\d]')
        # # patternEnglish = re.compile(r'^([\w|\s]+)\s(第?([\u4E00-\u9FA5]|\d)+(.+))$')
        #
        # if resRegionBuilding:
        #     region = resRegionBuilding.group(1).upper().strip()
        #     # estateFull = normalize(resRegionBuilding.group(2).upper().strip().replace(" ", ""))
        #     estateFull = resRegionBuilding.group(2).upper().strip()
        #
        #     if region not in regionEstates:
        #         regionEstates[region] = {}
        #
        #     # print("estatefull", estateFull)
        #     resEstate = patternEstates.match(estateFull)
        #     resSingle = patternSingleBuilding.match(estateFull)
        #     resPhase = patternPhase.match(estateFull)
        #     resEnglish = patternEnglish.match(estateFull)
        #     resultNonestate = patternNonestates.match(estateFull)
        #
        #     if resEstate:
        #         estate = normalize(resEstate.group(1).upper().strip().replace(" ", "_"))
        #         building = normalize(resEstate.group(2).upper().strip().replace(" ", ""))
        #
        #     elif resSingle:
        #         estate = normalize(resSingle.group(1).upper().strip().replace(" ", "_"))
        #         building = estate
        #
        #     elif resPhase:
        #         estate = normalize(resPhase.group(1).upper().strip().replace(" ", "_"))
        #         building = normalize(resPhase.group(2).upper().strip().replace(" ", ""))
        #
        #     elif resEnglish:
        #         estate = resEnglish.group(1).upper().strip().replace("  ", " ").replace(" ", "_")
        #         # print(estate, resEnglish.group(2))
        #         building = resEnglish.group(2).upper().strip().replace(" ", "") \
        #             if resEnglish.group(2) != None else estate
        #
        #     elif resultNonestate:
        #         estate = normalize(resultNonestate.group(1).upper().strip().replace(" ", "_"))
        #         # print("result non estate ", estateFull)
        #         building = estate
        #         #building = normalize(resultNonestate.group(2).upper().strip().replace(" ", ""))
        #     else:
        #         raise Exception("not found", line)

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

        # patternRegionBuilding = re.compile(r'^(.*?)\s+(.*?)$')
        #
        # # patternEstates = re.compile(r"([\u4E00-\u9FA5]+苑|[\u4E00-\u9FA5]+邨)([\u4E00-\u9FA5]+)$")
        # patternEstates = re.compile(r"([\u4E00-\u9FA5]+[苑|邨|花園])([\u4E00-\u9FA5]+[樓|閣|苑].*?)$")
        # patternSingleBuilding = re.compile(r"^(\S+)$")
        #
        #
        # # patternEnglish = re.compile(r'^([\w|\s]+)\s(第?([\u4E00-\u9FA5]|\d)+(.+))$')
        # # patternEnglish = re.compile("([^\d第]+)\s(.+)$")
        # # patternEnglish = re.compile(r"([^\d第]+)\s+(\S+\s+座?)$")
        # #patternEnglish = re.compile(r"([^\d第]+)\s*(\S+\s*座)$")
        # # patternEnglish = re.compile(r"([^\d第]+)\s*(第*.*座)*$")
        # patternEnglish = re.compile(r"([^第]+)\s*(第*\S+\s*座)+$")
        # patternNonestates = re.compile(r"^(.+)$")
        #
        # patternCommon = re.compile(r"^(.*?)(第.{1,3}座)$")
        #
        # #patternNonestates = re.compile(r"(\S+)\s+(.*?)$")
        #
        # resRegionBuilding = patternRegionBuilding.match(line)
        #
        # if resRegionBuilding:
        #     region = normalize(resRegionBuilding.group(1).upper().strip())
        #     estateFull = resRegionBuilding.group(2).upper().strip()
        #

        #
        #     resSingleBuilding = patternSingleBuilding.match(estateFull)
        #     resEstates = patternEstates.match(estateFull)
        #     resEnglish = patternEnglish.match(estateFull)
        #     # resCommon = patternCommon.match(estateFull)
        #     resNonestates = patternNonestates.match(estateFull)
        #
        #     if resEstates:
        #         estate = normalize(resEstates.group(1).upper().strip().replace(" ", "_"))
        #         building = normalize(resEstates.group(2).upper().strip().replace(" ", ""))
        #
        #     elif resSingleBuilding:
        #         estate = resSingleBuilding.group(1).upper()
        #         building = estate
        #
        #     elif resEnglish:
        #         estate = resEnglish.group(1).upper().strip().replace("  ", " ").replace(" ", "_")
        #
        #         building = resEnglish.group(2).upper().strip().replace(" ", "") \
        #             if resEnglish.group(2) != None else estate
        #
        #     elif resNonestates:
        #         estate = normalize(resNonestates.group(1).upper().strip().replace(" ", "_"))
        #         building = estate
        #         # building = normalize(resNonestates.group(2).upper().strip().replace(" ", ""))
        #
        #     else:
        #         raise Exception("not found", estateFull)

        building = estate if building == "" else building

        if estate not in regionEstates[region]:
            regionEstates[region][estate] = []
        if building not in regionEstates[region][estate]:
            regionEstates[region][estate].append(building)

    return regionEstates

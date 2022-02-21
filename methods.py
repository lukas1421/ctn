import re
import unicodedata

dict1 = {'10': '十', '11': '十一', '1': '一', '2': '二', '3': '三', '4': '四',
         '5': '五', '6': '六', '7': '七', '8': '八', '9': '九'}


def normalize(s):
    for i in dict1.keys():
        s = s.replace(i, dict1[i])
    return unicodedata.normalize('NFKC', s)


def getConfirmedDict(fileName):
    with open(fileName, "r") as file:
        lines = file.read().rstrip().splitlines()

    regionEstates = {}

    for line in lines:
        if '地區' in line:
            continue

        patternRegionBuilding = re.compile(r'^(.*?)\s+(.*?)$')
        resRegionBuilding = patternRegionBuilding.match(line)
        patternEstates = re.compile(r"([\u4E00-\u9FA5]{2}苑|[\u4E00-\u9FA5]{2}邨)(.*?)$")
        patternPhase = re.compile(r"^(.*?期)\s*(.*?)$")
        patternNonestates = re.compile(r"([^\s]+)\s*(.*?)$")

        if resRegionBuilding:
            region = normalize(resRegionBuilding.group(1).upper().strip())
            estateFull = normalize(resRegionBuilding.group(2).upper().strip().replace(" ", ""))

            if region not in regionEstates:
                regionEstates[region] = {}

            resEstate = patternEstates.match(estateFull)
            resPhase = patternPhase.match(estateFull)
            resultNonestate = patternNonestates.match(estateFull)

            if resEstate:
                estate = normalize(resEstate.group(1).upper().strip().replace(" ", ""))
                building = normalize(resEstate.group(2).upper().strip().replace(" ", ""))

                if estate not in regionEstates[region]:
                    regionEstates[region][estate] = []
                if building not in regionEstates[region][estate]:
                    regionEstates[region][estate].append(building)

            elif resPhase:
                estate = normalize(resPhase.group(1).upper().strip().replace(" ", ""))
                building = normalize(resPhase.group(2).upper().strip().replace(" ", ""))
                if estate not in regionEstates[region]:
                    regionEstates[region][estate] = []
                if building not in regionEstates[region][estate]:
                    regionEstates[region][estate].append(building)

            elif resultNonestate:
                estate = normalize(resultNonestate.group(1).upper().strip().replace(" ", ""))
                building = normalize(resultNonestate.group(2).upper().strip().replace(" ", ""))

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
        patternRegionBuilding = re.compile(r'^(.*?)\s+(.*?)$')

        patternEstates = re.compile(r"([\u4E00-\u9FA5]{2}苑|[\u4E00-\u9FA5]{2}邨)(.*?)$")
        patternCommon = re.compile(r"^(.*?)(第.{1,3}座)$")

        patternNonestates = re.compile(r"([^\s]+)\s+(.*?)$")

        resRegionBuilding = patternRegionBuilding.match(line)

        if resRegionBuilding:
            region = normalize(resRegionBuilding.group(1).upper().strip().replace(" ", ""))
            estateFull = normalize(resRegionBuilding.group(2).upper().strip().replace(" ", ""))

            if region not in regionEstates:
                regionEstates[region] = {}

            resEstates = patternEstates.match(estateFull)
            resCommon = patternCommon.match(estateFull)
            resNonestates = patternNonestates.match(estateFull)

            if resEstates:
                estate = normalize(resEstates.group(1).upper().strip().replace(" ", ""))
                building = normalize(resEstates.group(2).upper().strip().replace(" ", ""))

                if estate not in regionEstates[region]:
                    regionEstates[region][estate] = []
                if building not in regionEstates[region][estate]:
                    regionEstates[region][estate].append(building)

            elif resCommon:
                estate = normalize(resCommon.group(1).upper().strip().replace(" ", ""))
                building = normalize(resCommon.group(2).upper().strip().replace(" ", ""))

                if estate not in regionEstates[region]:
                    regionEstates[region][estate] = []
                if building not in regionEstates[region][estate]:
                    regionEstates[region][estate].append(building)

            elif resNonestates:
                estate = normalize(resNonestates.group(1).upper().strip().replace(" ", ""))
                building = normalize(resNonestates.group(2).upper().strip().replace(" ", ""))

                if estate not in regionEstates[region]:
                    regionEstates[region][estate] = []
                if building not in regionEstates[region][estate]:
                    regionEstates[region][estate].append(building)
    return regionEstates

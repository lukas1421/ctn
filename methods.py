import re


def getConfirmedDict(fileName):
    with open(fileName, "r") as file:
        lines = file.read().rstrip().splitlines()

    regionEstates = {}

    for line in lines:
        # print(region)
        patternRegionBuilding = re.compile(r'^(.*?)\s+(.*?)$')
        # pattern = re.compile(r'' + region)
        # print(pattern)
        # patternRegion = re.compile(region + r'\s+(.*?)$')
        # print(patternRegion)
        # pattern = re.compile(r'西貢')
        # pattern1 = re.compile(r'西貢\s+(.*?)$')
        resRegionBuilding = patternRegionBuilding.match(line)
        patternEstates = re.compile(r"([\u4E00-\u9FA5]{2}苑|[\u4E00-\u9FA5]{2}邨)(.*?)$")
        patternPhase = re.compile(r"^(.*?期)\s*(.*?)$")
        patternNonestates = re.compile(r"([^\s]+)\s*(.*?)$")

        if resRegionBuilding:
            region = resRegionBuilding.group(1).upper()
            estateFull = resRegionBuilding.group(2).upper()

            if region == '地區':
                # print("diqu useless line", region, line)
                continue

            if region not in regionEstates:
                regionEstates[region] = {}

            # print("group1",region, "group2", estateFull)
            resEstate = patternEstates.match(estateFull)
            resPhase = patternPhase.match(estateFull)
            resultNonestate = patternNonestates.match(estateFull)

            if resEstate:
                estate = resEstate.group(1).upper()
                building = resEstate.group(2).upper()

                if estate not in regionEstates[region]:
                    regionEstates[region][estate] = []
                regionEstates[region][estate].append(building)

            elif resPhase:
                estate = resPhase.group(1).upper()
                building = resPhase.group(2).upper()
                if estate not in regionEstates[region]:
                    regionEstates[region][estate] = []
                regionEstates[region][estate].append(building)

            elif resultNonestate:
                estate = resultNonestate.group(1).upper()
                building = resultNonestate.group(2).upper()

                if estate not in regionEstates[region]:
                    regionEstates[region][estate] = []
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
            region = resRegionBuilding.group(1).upper()
            estateFull = resRegionBuilding.group(2).upper()

            if region not in regionEstates:
                regionEstates[region] = {}

            resEstates = patternEstates.match(estateFull)
            resCommon = patternCommon.match(estateFull)
            resNonestates = patternNonestates.match(estateFull)

            if resEstates:
                estate = resEstates.group(1).upper()
                building = resEstates.group(2).upper()

                if estate not in regionEstates[region]:
                    regionEstates[region][estate] = []
                regionEstates[region][estate].append(building)

            elif resCommon:
                estate = resCommon.group(1).upper()
                building = resCommon.group(2).upper()

                if estate not in regionEstates[region]:
                    regionEstates[region][estate] = []
                regionEstates[region][estate].append(building)

            elif resNonestates:
                estate = resNonestates.group(1).upper()
                building = resNonestates.group(2).upper()

                if estate not in regionEstates[region]:
                    regionEstates[region][estate] = []
                regionEstates[region][estate].append(building)
    return regionEstates

import re

def getEstateFull(line):
    try:
        region = re.compile(r'^(\S+)\s+(.+)$').match(line).group(1)
        res = re.compile(r'^(\S+)\s+(.+)$').match(line).group(2)

        # return res if res != None else res
        return region, res
    except Exception as e:
        print(line, "error")


def getBuildingEstate(estateFull):
    patternGovEstates = re.compile(r"([\u4E00-\u9FA5]+[苑|邨|花園])([\u4E00-\u9FA5]+[樓|閣|苑].*?)$")
    patternSingleBuilding = re.compile(r"^(\S+)$")
    patternPhase = re.compile(r"^(.*?期)\s*(.*?)$")
    patternSeat = re.compile(r"(^.+)\s*(第\s*\S+\s*座)$")
    patternEnglish = re.compile(r"(^.+)\s+(\S+\s*座)$")
    # patternEnglish = re.compile(r"([^第]+)\s*(第*\S+\s*座)+$")
    patternStreet = re.compile(r"^(.+)\s+(\S+\s*號)$")

    patternNonestates = re.compile(r"^(.+)$")

    resEstate = patternGovEstates.match(estateFull)
    resSingle = patternSingleBuilding.match(estateFull)
    resPhase = patternPhase.match(estateFull)
    resSeat = patternSeat.match(estateFull)
    resEnglish = patternEnglish.match(estateFull)
    resStreet = patternStreet.match(estateFull)
    resultNonestate = patternNonestates.match(estateFull)
    resType = "default"

    if resSeat:
        estate = resSeat.group(1).upper().strip().replace(" ", "_")
        building = resSeat.group(2).upper().strip().replace(" ", "")
        resType = 'resSeat'
    elif resEstate:
        estate = resEstate.group(1).upper().strip().replace(" ", "_")
        building = resEstate.group(2).upper().strip().replace(" ", "")
        resType = 'resEstate'
    elif resSingle:
        estate = resSingle.group(1).upper().strip().replace(" ", "_")
        building = estate
        resType = 'resSingle'
    elif resPhase:
        estate = resPhase.group(1).upper().strip().replace(" ", "_")
        building = resPhase.group(2).upper().strip().replace(" ", "")
        resType = 'resPhase'
    elif resEnglish:
        estate = resEnglish.group(1).upper().strip().replace("  ", " ").replace(" ", "_")
        building = resEnglish.group(2).upper().strip().replace(" ", "") \
            if resEnglish.group(2) != None else estate
        resType = 'resEnglish'

    elif resStreet:
        estate = resStreet.group(1).upper().strip().replace(" ", "_")
        building = resStreet.group(2).upper().strip().replace(" ", "")
        resType = 'resStreet'

    elif resultNonestate:
        estate = resultNonestate.group(1).upper().strip().replace(" ", "_")
        building = estate
        resType = 'resNonestate'
    else:
        resType = 'notFound'
        raise Exception("not found")

    return estate, building, resType


###RUN####

# with open('file_confirmedBuildings_T', "r") as file:
#     lines = file.read().rstrip().splitlines()
#
# for line in lines:
#     try:
#         #print(getEstateFull(line))
#         resTuple = getBuildingEstate(getEstateFull(line)[1])
#         #print(resTuple[0], resTuple[1])
#         print("tuple", resTuple)
#         #print("line only", line)
#     except Exception as e:
#         print(line, " ", e)
#     # print(getBuildingEstate())

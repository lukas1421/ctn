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
    patternGovEstates = re.compile(r"([\u4E00-\u9FA5]+花*[苑邨村園心島廈都])([\u4E00-\u9FA5]+[樓閣楼苑軒居廈].*?)$")
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
        estate = prettifyEstate(resSeat.group(1))
        building = resSeat.group(2).upper().strip().replace(" ", "")
        resType = 'resSeat'
    elif resEstate:
        estate = prettifyEstate(resEstate.group(1))
        building = resEstate.group(2).upper().strip().replace(" ", "")
        resType = 'resEstate'
    elif resSingle:
        estate = prettifyEstate(resSingle.group(1))
        building = estate
        resType = 'resSingle'
    elif resPhase:
        estate = prettifyEstate(resPhase.group(1))
        building = resPhase.group(2).upper().strip().replace(" ", "")
        resType = 'resPhase'
    elif resEnglish:
        estate = prettifyEstate(resEnglish.group(1))
        building = resEnglish.group(2).upper().strip().replace(" ", "") \
            if resEnglish.group(2) != None else estate
        resType = 'resEnglish'
    elif resStreet:
        estate = prettifyEstate(resStreet.group(1))
        building = resStreet.group(2).upper().strip().replace(" ", "")
        resType = 'resStreet'

    elif resultNonestate:
        estate = prettifyEstate(resultNonestate.group(1))
        building = estate
        resType = 'resNonestate'
    else:
        resType = 'notFound'
        raise Exception("not found")

    return estate, building, resType

# 青山公路 - 荃灣段
def prettifyEstate(estate):
    return '_'.join(estate.strip().upper().replace("-"," ").split())
    # return '_'.join(re.split(r',+|_+|\s+', estate)).replace(" ", "_")
    # return estate.upper().strip().replace(" ", "_")


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

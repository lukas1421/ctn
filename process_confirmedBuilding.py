import re

with open("file_confirmedBuildings_T", "r") as file:
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
        region = resRegionBuilding.group(1)
        estateFull = resRegionBuilding.group(2)

        if region == '地區':
            #print("diqu useless line", region, line)
            continue

        if region not in regionEstates:
            regionEstates[region] = {}

        # print("group1",region, "group2", estateFull)
        resEstate = patternEstates.match(estateFull)
        resPhase = patternPhase.match(estateFull)
        resultNonestate = patternNonestates.match(estateFull)

        if resEstate:
            estate = resEstate.group(1)
            building = resEstate.group(2)

            if estate not in regionEstates[region]:
                regionEstates[region][estate] = []
            regionEstates[region][estate].append(building)

        elif resPhase:
            estate = resPhase.group(1)
            building = resPhase.group(2)
            if estate not in regionEstates[region]:
                regionEstates[region][estate] = []
            regionEstates[region][estate].append(building)

        elif resultNonestate:
            estate = resultNonestate.group(1)
            building = resultNonestate.group(2)

            if estate not in regionEstates[region]:
                regionEstates[region][estate] = []
            regionEstates[region][estate].append(building)
#
print("*******************************确诊小区*****************************")
totalEstatesInHK = sum(len(regionEstates[r]) for r in regionEstates.keys())
totalBuildingsInHK = sum(sum(len(regionEstates[r][e]) for e in regionEstates[r].keys()) for r in regionEstates.keys())
totalPublicEstatesInHK = sum(sum(1 for e in regionEstates[r].keys() if '邨' in e or '苑' in e)
                             for r in regionEstates.keys())
totalPublicBuildingsInHK = sum(sum(len(regionEstates[r][e]) for e in regionEstates[r].keys() if '邨' in e or '苑' in e)
                               for r in regionEstates.keys())

print(" total estate in HK ", totalEstatesInHK)
print(" total Buildings in HK ", totalBuildingsInHK)
print(" total public estates ", totalPublicEstatesInHK)
print(" total public buildings ", totalPublicBuildingsInHK)

for r in sorted(regionEstates,
                key=lambda r: sum(len(regionEstates[r][v]) for v in regionEstates[r].keys()), reverse=True):
    print("***************", r, "****************")
    print("# of estates/HK estates", len(regionEstates[r]), round(len(regionEstates[r]) / totalEstatesInHK * 100), "%")
    print("# of public estates/region estates", sum(1 for e in regionEstates[r].keys() if '邨' in e or '苑' in e),
          round(sum(1 for e in regionEstates[r].keys() if '邨' in e or '苑' in e) / len(regionEstates[r]) * 100), "%")

    print("# total Buildings/total HK buildings", sum(len(regionEstates[r][e]) for e in regionEstates[r].keys()),
          round(sum(len(regionEstates[r][e]) for e in regionEstates[r].keys()) / totalBuildingsInHK * 100), "%")

    print("# of public buildings/region buildings",
          sum(len(regionEstates[r][e]) for e in regionEstates[r].keys() if '邨' in e or '苑' in e),
          round(sum(len(regionEstates[r][e]) for e in regionEstates[r].keys() if '邨' in e or '苑' in e)
                / sum(len(regionEstates[r][e]) for e in regionEstates[r].keys()) * 100), "%")

    for k in sorted(regionEstates[r], key=lambda k: len(regionEstates[r][k]), reverse=True):
        print(r, k, regionEstates[r][k], len(regionEstates[r][k]))

# print(region)
# # print(dictEstates)
# for k in sorted(dictEstates, key=lambda k: len(dictEstates[k]), reverse=True):
#     print(k, dictEstates[k])

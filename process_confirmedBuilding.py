import re

from methods import getConfirmedDict

regionEstates = getConfirmedDict('file_confirmedBuildings_T-1')

# print(regionEstates['南區'])

print("*******************************确诊小区*****************************")
totalEstatesInHK = sum(len(regionEstates[r]) for r in regionEstates.keys())
totalBuildingsInHK = sum(sum(len(regionEstates[r][e]) for e in regionEstates[r].keys()) for r in regionEstates.keys())
totalPublicEstatesInHK = sum(sum(1 for e in regionEstates[r].keys()
                                 if ('邨' in e or '苑' in e) and len(regionEstates[r][e]) > 1)
                             for r in regionEstates.keys())
totalPublicBuildingsInHK = sum(sum(len(regionEstates[r][e]) for e in regionEstates[r].keys()
                                   if ('邨' in e or '苑' in e) and len(regionEstates[r][e]) > 1)
                               for r in regionEstates.keys())

print(" total estate in HK ", totalEstatesInHK)

# print(sorted(((v, k) for k, v in estateChg.items()), reverse=True))

estatesRanks = {k: len(v) for k, v in regionEstates.items()}
print(sorted(((v, r) for r, v in estatesRanks.items()), reverse=True))

print(" total Buildings in HK ", totalBuildingsInHK)
buildingRank = {r: sum(len(regionEstates[r][e]) for e in regionEstates[r].keys()) for r in regionEstates.keys()}
print(sorted(((v, r) for r, v in buildingRank.items()), reverse=True))

print(" total public estates ", totalPublicEstatesInHK)
print(" total public buildings ", totalPublicBuildingsInHK)

for r in sorted(regionEstates,
                key=lambda r: sum(len(regionEstates[r][v]) for v in regionEstates[r].keys()), reverse=True):
    print(' ')
    print("***************", r, "****************")
    print("# of estates/HK estates", len(regionEstates[r]), totalEstatesInHK,
          round(len(regionEstates[r]) / totalEstatesInHK * 100), "%")

    # print("# of public estates/region estates", sum(1 for e in regionEstates[r].keys() if '邨' in e or '苑' in e),
    #       round(sum(1 for e in regionEstates[r].keys() if '邨' in e or '苑' in e and len(regionEstates[r][e]) > 1)
    #             / len(regionEstates[r]) * 100), "%")

    singleBuilding = sum(1 for e in regionEstates[r].keys() for b in regionEstates[r][e] if '號' in b)
    totalBuildings = sum(1 for e in regionEstates[r].keys() for b in regionEstates[r][e])
    print('单楼#', singleBuilding,
          '非单楼', sum(1 for e in regionEstates[r].keys() for b in regionEstates[r][e] if '號' not in b),
          '总楼', totalBuildings, "单楼%", round(singleBuilding / totalBuildings * 100), "%")

    print("# total Buildings", sum(len(regionEstates[r][e]) for e in regionEstates[r].keys()))

    print("# total Buildings/total HK buildings", sum(len(regionEstates[r][e]) for e in regionEstates[r].keys()),
          totalBuildingsInHK,
          round(sum(len(regionEstates[r][e]) for e in regionEstates[r].keys()) / totalBuildingsInHK * 100), "%")

    # print("# of public buildings/region buildings",
    #       sum(len(regionEstates[r][e]) for e in regionEstates[r].keys() if
    #           '邨' in e or '苑' in e and len(regionEstates[r][e]) > 1),
    #       round(sum(len(regionEstates[r][e]) for e in regionEstates[r].keys() if
    #                 '邨' in e or '苑' in e and len(regionEstates[r][e]) > 1)
    #             / sum(len(regionEstates[r][e]) for e in regionEstates[r].keys()) * 100), "%")

    for e in sorted(regionEstates[r], key=lambda e: len(regionEstates[r][e]), reverse=True):
        print(r, e, regionEstates[r][e], len(regionEstates[r][e]))

# print(region)
# # print(dictEstates)
# for k in sorted(dictEstates, key=lambda k: len(dictEstates[k]), reverse=True):
#     print(k, dictEstates[k])

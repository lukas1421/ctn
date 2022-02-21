import re

from methods import getConfirmedDict

regionEstates = getConfirmedDict('file_confirmedBuildings_T')

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

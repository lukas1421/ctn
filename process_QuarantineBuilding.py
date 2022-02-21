import re

####
#### Quarantine Buildings #####
from methods import getQuarantineDict

regionEstates = getQuarantineDict('file_quarantineBuildings_T-1')

# with open("file_quarantineBuildings_T", "r") as file:
#     lines = file.read().rstrip().splitlines()
# regionEstates = {}
#
# for line in lines:
#     patternRegionBuilding = re.compile(r'^(.*?)\s+(.*?)$')
#
#     patternEstates = re.compile(r"([\u4E00-\u9FA5]{2}苑|[\u4E00-\u9FA5]{2}邨)(.*?)$")
#     patternCommon = re.compile(r"^(.*?)(第.{1,3}座)$")
#
#     patternNonestates = re.compile(r"([^\s]+)\s+(.*?)$")
#
#     resRegionBuilding = patternRegionBuilding.match(line)
#
#     if resRegionBuilding:
#         region = resRegionBuilding.group(1)
#         estateFull = resRegionBuilding.group(2)
#
#         if region not in regionEstates:
#             regionEstates[region] = {}
#
#         resEstates = patternEstates.match(estateFull)
#         resCommon = patternCommon.match(estateFull)
#         resNonestates = patternNonestates.match(estateFull)
#
#         if resEstates:
#             estate = resEstates.group(1)
#             building = resEstates.group(2)
#
#             if estate not in regionEstates[region]:
#                 regionEstates[region][estate] = []
#             regionEstates[region][estate].append(building)
#
#         elif resCommon:
#             estate = resCommon.group(1)
#             building = resCommon.group(2)
#
#             if estate not in regionEstates[region]:
#                 regionEstates[region][estate] = []
#             regionEstates[region][estate].append(building)
#
#         elif resNonestates:
#             estate = resNonestates.group(1)
#             building = resNonestates.group(2)
#
#             if estate not in regionEstates[region]:
#                 regionEstates[region][estate] = []
#             regionEstates[region][estate].append(building)

print("*************隔离小区******************")

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

# (str(e) for e in regionEstates[r].keys()

for r in sorted(regionEstates,
                key=lambda r: (sum(len(regionEstates[r][e]) for e in regionEstates[r].keys())), reverse=True):
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

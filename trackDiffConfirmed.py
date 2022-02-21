from methods import getConfirmedDict

regionEstatesT=getConfirmedDict('file_confirmedBuildings_T')
regionEstatesY=getConfirmedDict('file_confirmedBuildings_T-1')

print("*******************************确诊小区*****************************")
totalEstatesInHK = sum(len(regionEstatesT[r]) for r in regionEstatesT.keys())
totalBuildingsInHK = sum(sum(len(regionEstatesT[r][e]) for e in regionEstatesT[r].keys()) for r in regionEstatesT.keys())
totalPublicEstatesInHK = sum(sum(1 for e in regionEstatesT[r].keys() if '邨' in e or '苑' in e)
                             for r in regionEstatesT.keys())
totalPublicBuildingsInHK = sum(sum(len(regionEstatesT[r][e]) for e in regionEstatesT[r].keys() if '邨' in e or '苑' in e)
                               for r in regionEstatesT.keys())

print(" total estate in HK ", totalEstatesInHK)
print(" total Buildings in HK ", totalBuildingsInHK)
print(" total public estates ", totalPublicEstatesInHK)
print(" total public buildings ", totalPublicBuildingsInHK)

for r in sorted(regionEstatesT,
                key=lambda r: sum(len(regionEstatesT[r][v]) for v in regionEstatesT[r].keys()), reverse=True):
    print("***************", r, "****************")
    print("# of estates/HK estates", len(regionEstatesT[r]), round(len(regionEstatesT[r]) / totalEstatesInHK * 100), "%")
    print("# of public estates/region estates", sum(1 for e in regionEstatesT[r].keys() if '邨' in e or '苑' in e),
          round(sum(1 for e in regionEstatesT[r].keys() if '邨' in e or '苑' in e) / len(regionEstatesT[r]) * 100), "%")

    print("# total Buildings/total HK buildings", sum(len(regionEstatesT[r][e]) for e in regionEstatesT[r].keys()),
          round(sum(len(regionEstatesT[r][e]) for e in regionEstatesT[r].keys()) / totalBuildingsInHK * 100), "%")

    print("# of public buildings/region buildings",
          sum(len(regionEstatesT[r][e]) for e in regionEstatesT[r].keys() if '邨' in e or '苑' in e),
          round(sum(len(regionEstatesT[r][e]) for e in regionEstatesT[r].keys() if '邨' in e or '苑' in e)
                / sum(len(regionEstatesT[r][e]) for e in regionEstatesT[r].keys()) * 100), "%")

    for k in sorted(regionEstatesT[r], key=lambda k: len(regionEstatesT[r][k]), reverse=True):
        print(r, k, regionEstatesT[r][k], len(regionEstatesT[r][k]))

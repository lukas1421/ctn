from methods import getQuarantineDict, getConfirmedDict

regionEstatesT = getConfirmedDict('file_confirmedBuildings_T')
regionEstatesY = getConfirmedDict('file_confirmedBuildings_T-1')

increaseRegions = {}
increaseEstates = {}
increaseBuildings = {}

for r in regionEstatesT:
    if r not in regionEstatesY:
        increaseRegions[r] = regionEstatesT[r]
        increaseEstates[r] = regionEstatesT[r]
        increaseBuildings[r] = regionEstatesT[r]
    else:
        for e in regionEstatesT[r]:
            if e not in regionEstatesY[r]:
                if r not in increaseEstates:
                    increaseEstates[r] = {}
                increaseEstates[r][e] = regionEstatesT[r][e]

                if r not in increaseBuildings:
                    increaseBuildings[r] = {}
                increaseBuildings[r][e] = regionEstatesT[r][e]
            else:
                for b in regionEstatesT[r][e]:
                    if b not in regionEstatesY[r][e]:
                        if r not in increaseBuildings:
                            increaseBuildings[r] = {}
                        if e not in increaseBuildings[r]:
                            increaseBuildings[r][e] = []
                        increaseBuildings[r][e].append(b)
# print(increaseEstates)

# DECREASE
decreaseRegions = {}
decreaseEstates = {}
decreaseBuildings = {}

for r in regionEstatesY:
    if r not in regionEstatesT:
        decreaseRegions[r] = regionEstatesY[r]
        decreaseEstates[r] = regionEstatesY[r]
        decreaseBuildings[r] = regionEstatesY[r]
    else:
        for e in regionEstatesY[r]:
            if e not in regionEstatesT[r]:
                if r not in decreaseEstates:
                    decreaseEstates[r] = {}
                decreaseEstates[r][e] = regionEstatesY[r][e]

                if r not in decreaseBuildings:
                    decreaseBuildings[r] = {}
                decreaseBuildings[r][e] = regionEstatesY[r][e]
            else:
                for b in regionEstatesY[r][e]:
                    if b not in regionEstatesT[r][e]:
                        if r not in decreaseBuildings:
                            decreaseBuildings[r] = {}
                        if e not in decreaseBuildings[r]:
                            decreaseBuildings[r][e] = []
                        decreaseBuildings[r][e].append(b)
# print(decreaseBuildings)

# print(decreaseBuildings)
print("********************今天昨天对比 确诊********************")
totalRegionsHKT = len(regionEstatesT.keys())
totalRegionsHKY = len(regionEstatesY.keys())
print("确诊总区 T/T-1", totalRegionsHKT, totalRegionsHKY, str(totalRegionsHKT - totalRegionsHKY))
# print(regionEstatesT.keys())
# print(regionEstatesY.keys())

totalEstatesInHKT = sum(len(regionEstatesT[r]) for r in regionEstatesT.keys())
totalEstatesInHKY = sum(len(regionEstatesY[r]) for r in regionEstatesY.keys())
print("确诊总小区 T/T-1", totalEstatesInHKT, totalEstatesInHKY, str(totalEstatesInHKT - totalEstatesInHKY))

totalBuildingsInHKT = sum(
    sum(len(regionEstatesT[r][e]) for e in regionEstatesT[r].keys()) for r in regionEstatesT.keys())
totalBuildingsInHKY = sum(sum(len(regionEstatesY[r][e])
                              for e in regionEstatesY[r].keys()) for r in regionEstatesY.keys())
print("确诊总楼数 T/T-1 ", totalBuildingsInHKT, totalBuildingsInHKY, str(totalBuildingsInHKT - totalBuildingsInHKY))

# xiaoqu
print("************确诊小区增加****************:", sum(len(increaseEstates[r]) for r in increaseEstates.keys()))

for r in sorted(increaseEstates, key=lambda r: len(increaseEstates[r]) - len(decreaseEstates[r]), reverse=True):
    print(" ")
    print("****", r, "****", "net:", len(increaseEstates[r]) - len(decreaseEstates[r]))

    print("增加小区:", len(increaseEstates[r]), "减少小区:", len(decreaseEstates[r]))

    for e in sorted(increaseEstates[r], key=lambda e: len(increaseEstates[r][e]), reverse=True):
        print('增加',e, increaseEstates[r][e], len(increaseEstates[r][e]))

    print(' ')
    print("减少小区****", len(decreaseEstates[r]))
    for e in sorted(decreaseEstates[r], key=lambda e: len(decreaseEstates[r][e]), reverse=True):
        print('减少',e, decreaseEstates[r][e], len(decreaseEstates[r][e]))

# print(" ")
# print("************确诊小区减少****************", sum(len(decreaseEstates[r]) for r in decreaseEstates.keys()))
#
# for r in sorted(decreaseEstates, key=lambda r: len(decreaseEstates[r]), reverse=True):
#     print(" ")
#     print("****", r, "减少小区****", len(decreaseEstates[r]))
#     for e in sorted(decreaseEstates[r], key=lambda e: len(decreaseEstates[r][e]), reverse=True):
#         print(e, decreaseEstates[r][e], len(decreaseEstates[r][e]))

# buildings
print(" ")
print("************确诊楼增****************:",
      sum(sum(len(increaseBuildings[r][e]) for e in increaseBuildings[r].keys())
          for r in increaseBuildings.keys()))

for r in sorted(increaseBuildings, key=lambda r: (sum(len(increaseBuildings[r][e])
                                                      for e in increaseBuildings[r].keys()) -
                                                  sum(len(decreaseBuildings[r][e]) for e in
                                                      decreaseBuildings[r].keys())), reverse=True):
    # estateIncrease = len(increaseBuildings[r].keys())
    increaseBuildingsInRegion = sum(len(increaseBuildings[r][e]) for e in increaseBuildings[r].keys())
    decreaseBuildingsInRegion = sum(len(decreaseBuildings[r][e]) for e in decreaseBuildings[r].keys())
    print(" ")
    print("****", r, "****","net:", increaseBuildingsInRegion - decreaseBuildingsInRegion)
    print("增加楼:", increaseBuildingsInRegion, "减少楼:", decreaseBuildingsInRegion)
    for k in sorted(increaseBuildings[r], key=lambda k: len(increaseBuildings[r][k]), reverse=True):
        print('增加',k, increaseBuildings[r][k], len(increaseBuildings[r][k]))

    # estateDecrease = len(decreaseBuildings[r])
    # buildingDecrease = sum(len(decreaseBuildings[r][e]) for e in decreaseBuildings[r].keys())
    print(' ')
    print("减少楼****", "Bldg:", decreaseBuildingsInRegion)
    for k in sorted(decreaseBuildings[r], key=lambda k: len(decreaseBuildings[r][k]), reverse=True):
        print('减少',k, decreaseBuildings[r][k], len(decreaseBuildings[r][k]))

# print(" ")
# print("************确诊楼减****************",
#       sum(sum(len(decreaseBuildings[r][e]) for e in decreaseBuildings[r].keys())
#           for r in decreaseBuildings.keys()))
#
# for r in sorted(decreaseBuildings,
#                 key=lambda r: (sum(len(decreaseBuildings[r][e]) for e in decreaseBuildings[r].keys())), reverse=True):
#     totalEstateInRegion = len(decreaseBuildings[r])
#     increaseBuildingsInRegion = sum(len(decreaseBuildings[r][e]) for e in decreaseBuildings[r].keys())
#     print(" ")
#     print("****", r, "减少楼****", "Estates:", totalEstateInRegion, "Bldg:", increaseBuildingsInRegion)
#     for k in sorted(decreaseBuildings[r], key=lambda k: len(decreaseBuildings[r][k]), reverse=True):
#         print(k, decreaseBuildings[r][k], len(decreaseBuildings[r][k]))
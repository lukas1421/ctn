from methods import getQuarantineDict

regionEstatesT = getQuarantineDict('file_quarantineBuildings_T')
regionEstatesY = getQuarantineDict('file_quarantineBuildings_T-1')

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
                        
print("********************今天昨天对比 隔离********************")
totalRegionsHKT = len(regionEstatesT.keys())
totalRegionsHKY = len(regionEstatesY.keys())
print("隔离总区 T/T-1", totalRegionsHKT, totalRegionsHKY, str(totalRegionsHKT - totalRegionsHKY))

totalEstatesInHKT = sum(len(regionEstatesT[r]) for r in regionEstatesT.keys())
totalEstatesInHKY = sum(len(regionEstatesY[r]) for r in regionEstatesY.keys())
print("隔离总小区 T/T-1", totalEstatesInHKT, totalEstatesInHKY, str(totalEstatesInHKT - totalEstatesInHKY))

totalBuildingsInHKT = sum(
    sum(len(regionEstatesT[r][e]) for e in regionEstatesT[r].keys()) for r in regionEstatesT.keys())
totalBuildingsInHKY = sum(sum(len(regionEstatesY[r][e])
                              for e in regionEstatesY[r].keys()) for r in regionEstatesY.keys())
print("隔离总楼数 T/T-1 ", totalBuildingsInHKT, totalBuildingsInHKY, str(totalBuildingsInHKT - totalBuildingsInHKY))


# try new
estateChg = {}
for r in set(list(regionEstatesT.keys()) + list(regionEstatesY.keys())):
    lenT = len(regionEstatesT[r]) if r in regionEstatesT.keys() else 0
    lenY = len(regionEstatesY[r]) if r in regionEstatesY.keys() else 0

    estateChg[r] = lenT - lenY

# print("estate chg", estateChg)
# print(sum(estateChg[k] for k in estateChg.keys()))

for r in sorted(estateChg, key=lambda r: estateChg[r], reverse=True):
    print(' ')
    inc = len(increaseEstates[r]) if r in increaseEstates.keys() else 0
    dec = len(decreaseEstates[r]) if r in decreaseEstates.keys() else 0
    print("****", r, "****", estateChg[r], "加", inc, "减", dec)

    if r in increaseEstates.keys():
        for e in sorted(increaseEstates[r], key=lambda e: len(increaseEstates[r][e]), reverse=False):
            print('增加', e, increaseEstates[r][e], len(increaseEstates[r][e]))
    else:
        print(r, "无增加")

    print(' ')

    if r in decreaseEstates.keys():
        for e in sorted(decreaseEstates[r], key=lambda e: len(decreaseEstates[r][e]), reverse=False):
            print('减少', e, decreaseEstates[r][e], len(decreaseEstates[r][e]))
    else:
        print(r, "无减少")

buildingChg = {}
for r in set(list(regionEstatesT.keys()) + list(regionEstatesY.keys())):
    if r in regionEstatesT.keys():
        lenT = sum(len(regionEstatesT[r][e]) for e in regionEstatesT[r].keys())
    else:
        lenT = 0

    if r in regionEstatesY.keys():
        lenY = sum(len(regionEstatesY[r][e]) for e in regionEstatesY[r].keys())
    else:
        lenY = 0

    buildingChg[r] = lenT - lenY

# print("building chg:", buildingChg)
# print(sum(buildingChg[k] for k in buildingChg.keys()))

print(' ')
print("**********Buildings**********", sum(buildingChg[k] for k in buildingChg.keys()))

for r in sorted(buildingChg, key=lambda r: buildingChg[r], reverse=True):
    print(' ')
    inc = sum(len(increaseBuildings[r][e]) for e in increaseBuildings[r].keys()) if r in increaseBuildings.keys() else 0
    dec = sum(len(decreaseBuildings[r][e]) for e in decreaseBuildings[r].keys()) if r in decreaseBuildings.keys() else 0
    print("****", r, "**** chg:", buildingChg[r], "加:", inc, "减:", dec)

    if r in increaseBuildings.keys():
        for e in sorted(increaseBuildings[r], key=lambda e: len(increaseBuildings[r][e]), reverse=False):
            print('增加', e, increaseBuildings[r][e], len(increaseBuildings[r][e]))
    else:
        print(r, "无增加")

    print(' ')
    if r in decreaseBuildings.keys():
        for e in sorted(decreaseBuildings[r], key=lambda e: len(decreaseBuildings[r][e]), reverse=False):
            print('减少', e, decreaseBuildings[r][e], len(decreaseBuildings[r][e]))
    else:
        print(r, "无减少")


# print("********************今天昨天对比 隔离********************")
# totalRegionsHKT = len(regionEstatesT.keys())
# totalRegionsHKY = len(regionEstatesY.keys())
# print("隔离总区 T/T-1", totalRegionsHKT, totalRegionsHKY, str(totalRegionsHKT - totalRegionsHKY))
# 
# totalEstatesInHKT = sum(len(regionEstatesT[r]) for r in regionEstatesT.keys())
# totalEstatesInHKY = sum(len(regionEstatesY[r]) for r in regionEstatesY.keys())
# print("隔离总小区 T/T-1", totalEstatesInHKT, totalEstatesInHKY, str(totalEstatesInHKT - totalEstatesInHKY))
# 
# totalBuildingsInHKT = sum(
#     sum(len(regionEstatesT[r][e]) for e in regionEstatesT[r].keys()) for r in regionEstatesT.keys())
# totalBuildingsInHKY = sum(sum(len(regionEstatesY[r][e])
#                               for e in regionEstatesY[r].keys()) for r in regionEstatesY.keys())
# print("隔离总楼数 T/T-1 ", totalBuildingsInHKT, totalBuildingsInHKY, str(totalBuildingsInHKT - totalBuildingsInHKY))
# 
# 
# def getLength(dict, key):
#     if key in dict:
#         return len(dict[key])
#     else:
#         return 0
# 
# 
# # try new
# estateChg = {}
# for r in set(list(regionEstatesT.keys()) + list(regionEstatesY.keys())):
#     lenT = len(regionEstatesT[r]) if r in regionEstatesT.keys() else 0
#     lenY = len(regionEstatesY[r]) if r in regionEstatesY.keys() else 0
# 
#     estateChg[r] = lenT - lenY
# 
# # print("estate chg", estateChg)
# # print(sum(estateChg[k] for k in estateChg.keys()))
# 
# for r in sorted(estateChg, key=lambda r: estateChg[r], reverse=True):
#     print(r, estateChg[r])
#     print("****", r, "****")
# 
#     if r in increaseEstates.keys():
#         for e in sorted(increaseEstates[r], key=lambda e: len(increaseEstates[r][e]), reverse=False):
#             print('增加', e, increaseEstates[r][e], len(increaseEstates[r][e]))
#     else:
#         print(r, "无增加")
# 
#     print(' ')
# 
#     if r in decreaseEstates.keys():
#         for e in sorted(decreaseEstates[r], key=lambda e: len(decreaseEstates[r][e]), reverse=False):
#             print('减少', e, decreaseEstates[r][e], len(decreaseEstates[r][e]))
#     else:
#         print(r, "无减少")
# 
# buildingChg = {}
# for r in set(list(regionEstatesT.keys()) + list(regionEstatesY.keys())):
#     if r in regionEstatesT.keys():
#         lenT = sum(len(regionEstatesT[r][e]) for e in regionEstatesT[r].keys())
#     else:
#         lenT = 0
# 
#     if r in regionEstatesY.keys():
#         lenY = sum(len(regionEstatesY[r][e]) for e in regionEstatesY[r].keys())
#     else:
#         lenY = 0
# 
#     buildingChg[r] = lenT - lenY
# 
# # print(buildingChg)
# # print(sum(buildingChg[k] for k in buildingChg.keys()))
# print(' ')
# print("**********Buildings**********")
# 
# for r in sorted(buildingChg, key=lambda r: buildingChg[r], reverse=True):
#     print(' ')
#     print("****", r, "****", buildingChg[r])
# 
#     if r in increaseBuildings.keys():
#         for e in sorted(increaseBuildings[r], key=lambda e: len(increaseBuildings[r][e]), reverse=False):
#             print('增加', e, increaseBuildings[r][e], len(increaseBuildings[r][e]))
#     else:
#         print(r, "无增加")
# 
#     print(' ')
#     if r in decreaseBuildings.keys():
#         for e in sorted(decreaseBuildings[r], key=lambda e: len(decreaseBuildings[r][e]), reverse=False):
#             print('减少', e, decreaseBuildings[r][e], len(decreaseBuildings[r][e]))
#     else:
#         print(r, "无减少")

import re

from methods import getQuarantineDict

regionEstatesT = getQuarantineDict('file_quarantineBuildings_T')
regionEstatesY = getQuarantineDict('file_quarantineBuildings_T-1')
increases = {}

for r in regionEstatesT:
    if r not in regionEstatesY:
        increases[r] = regionEstatesT[r]
    else:
        for e in regionEstatesT[r]:
            if e not in regionEstatesY[r]:
                if r not in increases:
                    increases[r] = {}
                increases[r][e] = regionEstatesT[r][e]
            else:
                for b in regionEstatesT[r][e]:
                    if b not in regionEstatesY[r][e]:
                        if r not in increases:
                            increases[r] = {}
                        if e not in increases[r]:
                            increases[r][e] = []
                        increases[r][e].append(b)
print(increases)

# DECREASE
decreases = {}
for r in regionEstatesY:
    if r not in regionEstatesT:
        decreases[r] = regionEstatesY[r]
    else:
        for e in regionEstatesY[r]:
            if e not in regionEstatesT[r]:
                if r not in decreases:
                    decreases[r] = {}
                decreases[r][e] = regionEstatesY[r][e]
            else:
                for b in regionEstatesY[r][e]:
                    if b not in regionEstatesT[r][e]:
                        if r not in decreases:
                            decreases[r] = {}
                        if e not in decreases[r]:
                            decreases[r][e] = []
                        decreases[r][e].append(b)
print(decreases)

print("************隔离增加**************** TOTAL BUILDINGS UP:",
      sum(sum(len(increases[r][e]) for e in increases[r].keys()) for r in increases.keys()))

for r in sorted(increases, key=lambda r: (sum(len(increases[r][e]) for e in increases[r].keys())), reverse=True):
    totalEstateInRegion = sum(1 for e in increases[r].keys())
    totalBuildingsInRegion = sum(len(increases[r][e]) for e in increases[r].keys())
    print("***************", r, "****************", "Estates:", totalEstateInRegion
          , "Bldg:", totalBuildingsInRegion)
    for k in sorted(increases[r], key=lambda k: len(increases[r][k]), reverse=True):
        print(k, increases[r][k], len(increases[r][k]))

print("                                                                        ")
print("************************************************************************")
print("************隔离减少**************** TOTAL BUILDING DOWN:",
      sum(sum(len(decreases[r][e]) for e in decreases[r].keys()) for r in decreases.keys()))

for r in sorted(decreases, key=lambda r: (sum(len(decreases[r][e]) for e in decreases[r].keys())), reverse=True):
    totalEstateInRegion = sum(1 for e in decreases[r].keys())
    totalBuildingsInRegion = sum(len(decreases[r][e]) for e in decreases[r].keys())
    print("***************", r, "****************", "Estates:", totalEstateInRegion
          , "Bldg:", totalBuildingsInRegion)
    for k in sorted(decreases[r], key=lambda k: len(decreases[r][k]), reverse=True):
        print(k, decreases[r][k], len(decreases[r][k]))

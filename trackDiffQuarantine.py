import re

from methods import getQuarantineDict

regionEstatesT = getQuarantineDict('file_quarantineBuildings_T')
regionEstatesY = getQuarantineDict('file_quarantineBuildings_T-1')
diff = {}

for r in regionEstatesT:
    if r not in regionEstatesY:
        # print("new region:", r)
        diff[r] = regionEstatesT[r]
    else:
        for e in regionEstatesT[r]:
            if e not in regionEstatesY[r]:
                if r not in diff:
                    diff[r] = {}
                diff[r][e] = regionEstatesT[r][e]
            #   print("new estate:", r, e, regionEstatesT[r][e])
            else:
                for b in regionEstatesT[r][e]:
                    if b not in regionEstatesY[r][e]:
                        if r not in diff:
                            diff[r]={}
                        if e not in diff[r]:
                            diff[r][e]=[]
                        diff[r][e].append(b)
            #            print("new building", r, e, b)
print(diff)

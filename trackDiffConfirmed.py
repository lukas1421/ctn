import re

from methods import getQuarantineDict

regionEstatesT = getQuarantineDict('file_confirmedBuildings_T')
regionEstatesY = getQuarantineDict('file_confirmedBuildings_T-1')
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
                            diff[r] = {}
                        if e not in diff[r]:
                            diff[r][e] = []
                        diff[r][e].append(b)
            #            print("new building", r, e, b)
print(diff)

print("************确诊不同****************")
for r in sorted(diff, key=lambda r: (sum(len(diff[r][e]) for e in diff[r].keys())), reverse=True):
    print("***************", r, "****************")
    for k in sorted(diff[r], key=lambda k: len(diff[r][k]), reverse=True):
        print(r, k, diff[r][k], len(diff[r][k]))

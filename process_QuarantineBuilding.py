import re

####
#### Quarantine Buildings #####

with open("file_quarantineBuildings", "r") as file:
    lines = file.read().rstrip().splitlines()
#dictEstates = {}
#regionEstates = {}

# for region in ['觀塘', '西贡']:
#     print(region)

for region in ['西貢','觀塘','沙田']:
    # print(region)
    dictEstates = {}
    #print(lines)

    for line in lines:
        # print(region)
        pattern = re.compile(r'' + region)
        #print(pattern)
        patternRegion = re.compile(region + r'\s+(.*?)$')
        #print(patternRegion)

        patternEstates = re.compile(r"([\u4E00-\u9FA5]{2}苑|[\u4E00-\u9FA5]{2}邨)(.*?)$")
        # patternCommon = re.compile(r"([\u4E00-\u9FA5]{2}廣場|[\u4E00-\u9FA5]{2,3}園)(.*?)$")
        # patternCommon = re.compile(r"([\u4E00-\u9FA5]{2,3}廣場|園)(.*?)$")
        # patternCommon = re.compile(r"^(.*?)(第.*?)$")
        patternCommon = re.compile(r"^(.*?)(第.{1,3}座)$")

        patternNonestates = re.compile(r"([^\s]+)\s+(.*?)$")

        res = pattern.match(line)
        if res:
            resSaikung = patternRegion.match(line)
            if resSaikung:
                resEstates = patternEstates.match(resSaikung.group(1))
                resCommon = patternCommon.match(resSaikung.group(1))
                resNonestates = patternNonestates.match(resSaikung.group(1))

                if resEstates:
                    estate = resEstates.group(1)
                    building = resEstates.group(2)

                    if estate not in dictEstates:
                        dictEstates[estate] = []
                    dictEstates[estate].append(building)

                elif resCommon:
                    estate = resCommon.group(1)
                    building = resCommon.group(2)

                    if estate not in dictEstates:
                        dictEstates[estate] = []
                    dictEstates[estate].append(building)

                elif resNonestates:
                    estate = resNonestates.group(1)
                    building = resNonestates.group(2)

                    if estate not in dictEstates:
                        dictEstates[estate] = []

                    dictEstates[estate].append(building)

    print("*************隔离小区******************")
    print(region)
    #print("dict estates",dictEstates)
    for k in sorted(dictEstates, key=lambda k: len(dictEstates[k]), reverse=True):
        print(k, dictEstates[k])


#     if region not in regionEstates:
#         regionEstates[region]=[]
#     regionEstates[region].append(dictEstates)
#
#
# # print(dictEstates)
# for region in regionEstates:
#     dictEstates = regionEstates[region]
#     print(region)
#     for k in sorted(dictEstates, key=lambda k: len(dictEstates[k]), reverse=True):
#         print(k, dictEstates[k])

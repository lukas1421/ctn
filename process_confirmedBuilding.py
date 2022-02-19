import re

with open("file_confirmedBuildings", "r") as file:
    lines = file.read().rstrip().splitlines()
# dictEstates = {}

for region in ['西貢','觀塘','沙田']:

    dictEstates = {}
    for line in lines:
        # print(region)
        pattern = re.compile(r'' + region)
        #print(pattern)
        patternRegion = re.compile(region + r'\s+(.*?)$')
        #print(patternRegion)
        # pattern = re.compile(r'西貢')
        # pattern1 = re.compile(r'西貢\s+(.*?)$')

        patternEstates = re.compile(r"([\u4E00-\u9FA5]{2}苑|[\u4E00-\u9FA5]{2}邨)(.*?)$")
        patternPhase = re.compile(r"^(.*?期)(.*?)$")
        patternNonestates = re.compile(r"([^\s]+)\s+(.*?)$")

        resSaikung = pattern.match(line)
        if resSaikung:
            res1 = patternRegion.match(line)
            if res1:
                resEstate = patternEstates.match(res1.group(1))
                resPhase = patternPhase.match(res1.group(1))
                resultNonestate = patternNonestates.match(res1.group(1))

                if resEstate:
                    estate = resEstate.group(1)
                    building = resEstate.group(2)

                    if estate not in dictEstates:
                        dictEstates[estate] = []
                    dictEstates[estate].append(building)
                elif resPhase:
                    estate = resPhase.group(1)
                    building = resPhase.group(2)

                    if estate not in dictEstates:
                        dictEstates[estate] = []
                    dictEstates[estate].append(building)
                elif resultNonestate:
                    estate = resultNonestate.group(1)
                    building = resultNonestate.group(2)

                    if estate not in dictEstates:
                        dictEstates[estate] = []

                    dictEstates[estate].append(building)

    print("*******************************确诊小区*****************************")
    print(region)
    # print(dictEstates)
    for k in sorted(dictEstates, key=lambda k: len(dictEstates[k]), reverse=True):
        print(k, dictEstates[k])

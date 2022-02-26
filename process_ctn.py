import re

districtNames = []
with open('list_CTN_districts','r')  as file:
    districts = file.read().rstrip().splitlines()

for dist in districts:
    districtNames.append(dist)

print(districtNames)

with open("file_ctn", "r") as file:
    lines = file.read().rstrip().splitlines()
dictEstates = {}
listEstates = []

for line in lines:
    # print(line)
    pattern = re.compile(r'\d{1,}\.\s{1}')

    res = pattern.match(line)
    if res:
        # print(line)

        # pattern2 = re.compile(r"^\d{1,2}\.\s([\u4E00-\u9FA5]{2}).*?([\u4E00-\u9FA5]{2}苑)")
        # res2 = pattern2.match(line)

        # pattern3 = re.compile(r"^\d{1,2}\.\s([\u4E00-\u9FA5]{2})([\u4E00-\u9FA5]{4})")
        # pattern3 = re.compile(r"^\d{1,2}\.\s([\u4E00-\u9FA5]{2})(.{5})")
        patternTwoChar = re.compile(r"^\d{1,2}\.\s\"*([\u4E00-\u9FA5]{2})(.*)$")
        patternThreeChar = re.compile(r"^\d{1,2}\.\s\"*([\u4E00-\u9FA5]{3})(.*)$")

        resTwoChar = patternTwoChar.match(line)
        resThreeChar = patternThreeChar.match(line)

        if resTwoChar and resThreeChar:
            districtTwoChar = resTwoChar.group(1)
            districtThreeChar = resThreeChar.group(1)

            if districtTwoChar in districtNames:
                district = districtTwoChar
                estate = resTwoChar.group(2)
            elif districtThreeChar in districtNames:
                district = districtThreeChar
                estate = resThreeChar.group(2)
            else:
                raise Exception("not found", line)

            if district not in dictEstates:
                dictEstates[district] = []
            dictEstates[district].append(estate)


for k in sorted(dictEstates, key=lambda k: len(dictEstates[k]), reverse=True):
    print(k, dictEstates[k])

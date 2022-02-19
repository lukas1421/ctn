import re

with open("file_confirmedBuildings", "r") as file:
    lines = file.read().rstrip().splitlines()
dictEstates = {}

for line in lines:

    pattern = re.compile(r'西貢')
    pattern1 = re.compile(r'西貢\s+(.*?)$')

    patternEstates = re.compile(r"([\u4E00-\u9FA5]{2}苑|[\u4E00-\u9FA5]{2}邨)(.*?)$")
    patternNonestates = re.compile(r"([^\s]+)\s+(.*?)$")

    res = pattern.match(line)
    if res:
        res1 = pattern1.match(line)
        if res1:
            res2 = patternEstates.match(res1.group(1))
            res3 = patternNonestates.match(res1.group(1))

            if res2:
                estate = res2.group(1)
                building = res2.group(2)

                if estate not in dictEstates:
                    dictEstates[estate] = []
                dictEstates[estate].append(building)

            elif res3:
                estate = res3.group(1)
                building = res3.group(2)

                if estate not in dictEstates:
                    dictEstates[estate] = []

                dictEstates[estate].append(building)


# print(dictEstates)
for k in sorted(dictEstates, key=lambda k: len(dictEstates[k]), reverse=True):
    print(k, dictEstates[k])

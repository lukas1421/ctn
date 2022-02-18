import re

with open("file_building_list", "r") as file:
    lines = file.read().rstrip().splitlines()
dictEstates = {}
#listEstates = []

for line in lines:
    # print(line)
    # pattern = re.compile(r'\d{1,2}\.\s{1}')

    pattern = re.compile(r'西貢')
    pattern1 = re.compile(r'西貢\s+(.*?)$')

    patternEstates = re.compile(r"([\u4E00-\u9FA5]{2}苑|[\u4E00-\u9FA5]{2}邨)(.*?)$")
    patternNonestates = re.compile(r"([^\s]+)(.*?)$")
    # patternEstates = re.compile(r"([\u4E00-\u9FA5]{2}苑|[\u4E00-\u9FA5]{2}邨)")

    # pattern2 = re.compile(r'西貢\s{1}([\u4E00-\u9FA5]{3})\b')

    # pattern2 = re.compile(r"^\d{1,2}\.\s([\u4E00-\u9FA5]{2}).*?([\u4E00-\u9FA5]{2}苑)")
    # # pattern3 = re.compile(r"^\d{1,2}\.\s([\u4E00-\u9FA5]{2})([\u4E00-\u9FA5]{4})")
    # pattern3 = re.compile(r"^\d{1,2}\.\s([\u4E00-\u9FA5]{2})(.{4})")
    res = pattern.match(line)
    if res:
        # print(line)
        res1 = pattern1.match(line)
        if res1:
            #print("res1 group1", res1.group(1))
            res2 = patternEstates.match(res1.group(1))
            res3 = patternNonestates.match(res1.group(1))

            if res2:
                #print("res2", res2.group(1), res2.group(2))
                estate = res2.group(1)
                building = res2.group(2)

                if estate not in dictEstates:
                    dictEstates[estate] = []
                dictEstates[estate].append(building)

            elif res3:
                #print("res3", res3.group(1), res3.group(2))
                estate = res3.group(1)
                building = res3.group(2)

                if estate not in dictEstates:
                    dictEstates[estate] = []

                dictEstates[estate].append(building)




        # res3 = pattern3.match(line)
        # print(res2)
        # if res3:
        #     district = res3.group(1)
        #     estate = res3.group(2)
        #
        #     # print(district, estate)
            # listEstates.append(res2.group(2))
            # print(line, ":", res2.group(1))

# print(dictEstates)
for k in sorted(dictEstates, key=lambda k: len(dictEstates[k]), reverse=True):
    print(k, dictEstates[k])

import re

with open("ctn", "r") as file:
    lines = file.read().rstrip().splitlines()
dictEstates = {}
listEstates = []

for line in lines:
    # print(line)
    pattern = re.compile(r'\d{1,2}\.\s{1}')
    pattern2 = re.compile(r"^\d{1,2}\.\s([\u4E00-\u9FA5]{2}).*?([\u4E00-\u9FA5]{2}苑)")
    # pattern3 = re.compile(r"^\d{1,2}\.\s([\u4E00-\u9FA5]{2})([\u4E00-\u9FA5]{4})")
    pattern3 = re.compile(r"^\d{1,2}\.\s([\u4E00-\u9FA5]{2})(.{4})")
    res = pattern.match(line)
    if res:
        print(line)
        res2 = pattern2.match(line)
        res3 = pattern3.match(line)
        # print(res2)
        if res3:
            district = res3.group(1)
            estate = res3.group(2)

            # print(district, estate)
            if district not in dictEstates:
                dictEstates[district] = []

            dictEstates[district].append(estate)
            # listEstates.append(res2.group(2))
            # print(line, ":", res2.group(1))

# print(dictEstates)
for k in sorted(dictEstates, key=lambda k: len(dictEstates[k]), reverse=True):
    print(k, dictEstates[k])

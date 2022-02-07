import re

with open("ctn", "r") as file:
    lines = file.read().rstrip().splitlines()

for line in lines:
    # print(line)
    pattern = re.compile(r'\d{1,2}\.\s{1}')
    pattern2 = re.compile(r"^\d{1,2}\.\s([\u4E00-\u9FA5]{2}).*?([\u4E00-\u9FA5]{2}邨)")
    res = pattern.match(line)
    if res:
        # print(line)
        res2 = pattern2.match(line)
        # print(res2)
        if res2:
            print(res2.group(1), res2.group(2))
            # print(line, ":", res2.group(1))

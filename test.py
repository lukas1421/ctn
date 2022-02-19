import re

shatian = '沙田第一城第三十四座'

# patternCommon = re.compile(r"(第.*)$")
#patternCommon = re.compile(r"(第.*?(?!.*第))$")
# patternCommon = re.compile(r"(第.*?)$")
patternCommon = re.compile(r"(.*?)(第.*?(?!第.*?))$")

resCommon = patternCommon.match(shatian)
print(resCommon)

# estate = resCommon.group(1)
#building = resCommon.group(2)

print(resCommon.group(0))
print(resCommon.group(1))
print(resCommon.group(2))
#print(building)
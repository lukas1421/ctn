import re
line = 'MALIBU MALI'
# line = '12'
# pattern=re.compile(r'^([\w|\s]+)\s(第?([\u4E00-\u9FA5]|\d)+(.+))$')

# pattern=re.compile(r"^([^第]+)\s*(.+座)$")

# pattern=re.compile(r'^(\D+(?!\s+))\s*(.+座)$')
print(re.search(r'(\D+(?!BU)(.*?))', line))

# # pattern=re.compile(r'^([\w|\s]+)\s(第?[\u4E00-\u9FA5]+(.+))$')
# res=pattern.match(line)
# if res:
#     print('group:',res.group())
#     print('group0:',res.group(0))
#     print('group1:',res.group(1))
#     print('group2:',res.group(2))

# a = "123abc"
# print(re.match("[a-z]+",a))
# print(re.search("[a-z]+",a))


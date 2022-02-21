import re
line = 'Capri 十A 座'
# line = '12'
pattern=re.compile(r'^([\w|\s]+)\s(第?([\u4E00-\u9FA5]|\d)+(.+))$')
# pattern=re.compile(r'^([\w|\s]+)\s(第?[\u4E00-\u9FA5]+(.+))$')
res=pattern.match(line)
if res:
    print('group0:',res.group(0))
    print('group1:',res.group(1))
    print('group2:',res.group(2))
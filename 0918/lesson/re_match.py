import re
source = 'Lux, the Lady of Luminosity'
m = re.match('Lux', source)
if m:
    print(m.group())

m = re.findall('L.{2}', source)
print(m)


import string
printable = string.printable
w = re.findall('\w', printable)
print(w)
d = re.findall('\d', printable)
print(d)


l = re.findall('L\w*', source)
print(l)

match_list = re.finditer('L\w*', source)
for m in match_list:
    print(m.group())

bo = re.findall(r'\bo\w*', source)
print(bo)


s = 'cat'
se = re.findall(r'[abc]at',s)
print(se)





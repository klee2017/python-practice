import re
f = open('sample.txt', 'rt')
source = f.read().strip().replace('\t', '')

p = re.compile(r'<td class="title".*?>.*?</td>', re.DOTALL)
result = re.findall(p, source)
for index, item in enumerate(result):
    print('== index %s ==' % index)

    cur_strip_item = re.sub(r'>\s*?<', r'><', item, flags=re.DOTALL)
    print(cur_strip_item)

    cur_title = re.sub(r'.*?<a.*?>(.*?)</a>.*', r'\g<1>', cur_strip_item)
    print(cur_title)

print('Total items:', len(result))



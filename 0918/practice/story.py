import re

story = '''Born to the prestigious Crownguards, the paragon family of Demacian service, Luxanna was destined for greatness. She grew up as the family's only daughter, and she immediately took to the advanced education and lavish parties required of families as high profile as the Crownguards. As Lux matured, it became clear that she was extraordinarily gifted. She could play tricks that made people believe they had seen things that did not actually exist. She could also hide in plain sight. Somehow, she was able to reverse engineer arcane magical spells after seeing them cast only once. She was hailed as a prodigy, drawing the affections of the Demacian government, military, and citizens alike.
As one of the youngest women to be tested by the College of Magic, she was discovered to possess a unique command over the powers of light. The young Lux viewed this as a great gift, something for her to embrace and use in the name of good. Realizing her unique skills, the Demacian military recruited and trained her in covert operations. She quickly became renowned for her daring achievements; the most dangerous of which found her deep in the chambers of the Noxian High Command. She extracted valuable inside information about the Noxus-Ionian conflict, earning her great favor with Demacians and Ionians alike. However, reconnaissance and surveillance was not for her. A light of her people, Lux's true calling was the League of Legends, where she could follow in her brother's footsteps and unleash her gifts as an inspiration for all of Demacia.
'''

print('1.', re.findall('Lux', story))
print('2.', re.findall('Lux|her|she', story))
print('3.', re.findall('[Ll]ux|[Hh]er|[Ss]he', story))
print('4.', re.findall('^Born', story))
print('5.', re.findall('Demacia$', story))

print('6.', re.findall('was', story))
print('7.', re.findall('(?<=she) was', story))
print('8.', re.findall('\w+(?<!she) was', story))
print('9.', re.findall('\bwas\b', story))
print('10.', re.findall(r'\bwas\b', story))


print('실습')

print('1.', re.findall(r'\ba\w{3}\b',story))
print('2.', re.findall(r'\w+?r[\b\W]',story))


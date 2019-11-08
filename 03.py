#!/usr/bin/env python3

import re

text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
count_lsit = list()

text_mod = re.sub('\.',"",text)
list1 = re.split(' |, ', text_mod)

for word in list1:
    count = len(word)
    count_lsit.append(count)

print(count_lsit)


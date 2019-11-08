#!/usr/bin/env python3

import re

num = 1
text = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
text_mod = re.sub('\.',"",text)
list1 = re.split(' |, ', text_mod)
dic1 = {}

for word in list1:
    if re.compile(r'^(1|5|6|7|8|9|15|16|19)$').search( str(num) ):
        dic1[num] = word[0]
        print(num)
    else:
        dic1[num] = word[0] + word[1]
    num += 1

print(dic1)
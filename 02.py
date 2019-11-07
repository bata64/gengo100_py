#!/usr/bin/env python3

text1 = 'パトカー'
text2 = 'タクシー'

list1 = list(text1)
list2 = list(text2)
list3 = list()

for a,b in zip(text1,text2):
    list3.append(a)
    list3.append(b)

text="".join(list3)
print (text)


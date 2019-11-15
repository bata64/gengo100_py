#!/usr/bin/env python3

import re

def main():
    str1 = 'I am an NLPer'
    result_word = ngram( str1, 'word', 2 )
    result_char = ngram( str1, 'char', 2 )

def ngram(text, type, num):
    if re.compile(r'^word$').search( type ):
        list1 = re.split(' |, ', text)
    elif re.compile(r'^char$').search( type ):
        text_mod = re.sub(' ','',text)
        list1 = list(text_mod)
    print(list1)

if __name__ == '__main__':
    main()

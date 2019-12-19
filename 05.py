#!/usr/bin/env python3

import re

def main():
    str1 = 'I am an NLPer'
    result_word = ngram( str1, 'word', 2 )
    result_char = ngram( str1, 'char', 2 )
    print(result_word,result_char)

def ngram(text, type, num):
    if re.compile(r'^word$').search( type ):
        list1 = re.split(' |, ', text)
    elif re.compile(r'^char$').search( type ):
        text_mod = re.sub(' ','',text)
        list1 = list(text_mod)
    
    if num == 1:
        return list1
    else:
        for i in range(len(list1)):
            data_ngram = list1[ i ]
            for j in range( num ):
        return list1
        

if __name__ == '__main__':
    main()

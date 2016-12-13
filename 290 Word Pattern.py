#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  290 Word Pattern.py
#  
'''Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:

    pattern = "abba", str = "dog cat cat dog" should return true.
    pattern = "abba", str = "dog cat cat fish" should return false.
    pattern = "aaaa", str = "dog cat cat dog" should return false.
    pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space. 
'''

def wordPattern(pattern,s):
    reb=False
    if pattern!='' and str!='':
        pa=pattern.lower()
        pl=list(pa)
        #print(pl)
        sl=s.split(' ')
        #print(sl) 
        kind=[]
        sk=[]
        for k in pa:
            if k not in kind:
                kind.append(k)
        for i in sl:
            if i not in sk:
                sk.append(i)        
        iteml=[]
        if len(kind)==len(sk) and len(pl)==len(sl):
            for n in range(0,len(kind)):
                iteml.append((sk[n],kind[n]))
            d=dict(iteml)
            rep=''
            for si in sl:
                rep=rep+d[si]
            if rep==pattern:
                reb=True
            rep=''
            for si in sl:
                rep=rep+d[si]
            if rep==pattern:
                reb=True
    return reb

def main(args):
    pattern = "abba"
    #str = "dog cat cat dog"
    #str = "dog cat cat cat"
    #str = "dog cat cat"
    print(wordPattern(pattern,str))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

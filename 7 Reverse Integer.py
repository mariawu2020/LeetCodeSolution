#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  7 Reverse Integer.py
#  
'''Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321 
'''
def reverse(x):    
    s=str(x)
    sl=list(s)
    rel=[]
    for i in range(len(sl),0,-1):
        rel.append(sl[i-1])
    if rel[-1]=='-':
        rel.pop()
        r=''.join(rel)
        if x>-2147483648 and -int(r)>-2147483648:
            return -int(r)
        else:
            return 0
    elif x<4294967296 and x>=0 and int(''.join(rel))<4294967296:
        return int(''.join(rel))
    else:
        return 0

def main(args):
    print(reverse(-123))
    print(reverse(123))
    print(reverse(1534236469))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

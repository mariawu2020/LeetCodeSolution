#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  6 ZigZag Conversion .py
#  
''' The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". '''
import math
def convert(s, numRows):
    sl = list(s)
    # 拟处理字符串字数
    snum = len(sl)
    if snum > numRows and numRows > 1:
        li = []
        # 循环间隔
        cyn = 2 * numRows - 2
        # 循环次数
        cycs = snum // cyn
        if snum % cyn != 0:
            cycs = cycs + 1

        # 构造新list
        nl = []
        for i in range(0, cycs * cyn):
            if i < snum:
                nl.append(sl[i])
            else:
                nl.append('')

        # 处理整数循环次数
        rels = []
        for c in range(0, cycs):
            li = nl[c * cyn:(c + 1) * cyn]
            rel = []
            for i in range(0, numRows):
                if i == 0 or i == numRows - 1:
                    s = li[i]
                else:
                    s = li[i] + li[cyn - i]
                rel.append(s)
            rels = rels + rel
        #print(rels)
        sout = ''
        #c = int(math.ceil(len(rels) / numRows))
        #if len(rels) % numRows != 0:
        #    c = c + 1
        #resnum = cycs * numRows
        #resultlist = []
        #for i in range(0, resnum):
        #    if i < len(rels):
        #        resultlist.append(rels[i])
        #    else:
        #        resultlist.append('')
        for j in range(0, numRows):
            for i in range(0, cycs):
                sout = sout + rels[i * numRows + j]
        return sout
    else:
        return s

def main(args):
    print(convert('PAYPALISHIRING',3))
    print(convert('', 1))
    print(convert('P', 1))
    print(convert('PA', 1))
    print(convert('PAB', 3))
    print(convert('PABCE', 4))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

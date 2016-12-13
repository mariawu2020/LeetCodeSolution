#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 412 Fizz Buzz.py
#412. Fizz Buzz
'''Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''
def fizzBuzz(n):
    li=[]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            li.append('FizzBuzz')
        elif i%3==0 and i%5!=0:
            li.append('Fizz')
        elif i%3!=0 and i%5==0:
            li.append('Buzz')
        else:
            li.append(str(i))
    return li

def main(args):
    print(fizzBuzz(15))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

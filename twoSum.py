#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  twoSum.py
#  1. Two Sum
"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
#  
def twoSum(nums,target):
    n=len(nums)
    li=[]
    res=[]
    for i in range(0,n):
       li.append((nums[i],i))        
    d=dict(li)
    #print(d)
    for j in range(0,n):
        result=target-nums[j]
        if d.has_key(result) and d[result]>j:
            re=[]
            re.append(j)
            re.append(d[result])
            res.append(re)
    return res
    
def twoSum2(nums,target):
    m = len(nums)
    li = []
    for i in range(0,m):
        for j in range(0,m):
            if nums[j] == target-nums[i] and i < j:
                li.append(i)
                li.append(j)
    return li

def main(args):
    print(twoSum2([3,2,4],6))
    li=[]
    for i in range(0,10000,2):
        li.append(i)
    #print li
    print(twoSum(li,9990))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

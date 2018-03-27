#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  4 Median of Two Sorted Arrays.py
#  
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

有两个大小为 m 和 n 的排序数组 nums1 和 nums2 。

请找出两个排序数组的中位数并且总的运行时间复杂度为 O(log (m+n)) 。

示例 1:

nums1 = [1, 3]
nums2 = [2]

中位数是 2.0
 

示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5
"""
#list很小的时候适用，逻辑简单
def findMedianSortedArrays(nums1, nums2):
        #数组合并排序
        nums=sorted(nums1+nums2)
        #list数值转化为float格式，因为int除取整
        #nums=map(float,nums)
        l=len(nums)
        if l%2==1:
            if l==1:
                return(nums[0])
            else:
                return(float(nums[int((l-1)/2)]))
        elif l%2==0:
            return((float(nums[int(l/2)])+float(nums[int(l/2-1)]))/2)
    
def main(args):
    print(findMedianSortedArrays([],[3]))
    print(findMedianSortedArrays([1,2],[3]))
    print(findMedianSortedArrays([1,2],[3,4]))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

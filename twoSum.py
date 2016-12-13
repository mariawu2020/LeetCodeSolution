class Solution(object):
    # 1. Two Sum
    """Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """
    #if the list is small
    def twoSum(nums, target):
        m = len(nums)
        li = []
        for i in range(0,m):
            for j in range(0,m):
                if nums[j] == target-nums[i] and i < j:
                    li.append(i)
                    li.append(j)
        return li
    
    #if the list is much bigger
    #dict in python used Hash
    def twoSum(nums,target):
        n=len(nums)
        li=[]
        re=[]
        for i in range(0,n):
           li.append((nums[i],i))        
        d=dict(li)
        #print(d)
        for j in range(0,n):
            result=target-nums[j]
            if d.has_key(result) and d[result]>j:
                re.append(j)
                re.append(d[result])
        return re

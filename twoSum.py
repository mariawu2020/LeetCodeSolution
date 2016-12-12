class Solution(object):
    # 1. Two Sum
    """Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """
    def twoSum(self, nums, target):
        m = len(nums) - 1
        li = []
        for i in range(m, 0, -1):
            for j in range(0, m):
                if nums[i] + nums[j] == target and i > j:
                    li.append(j)
                    li.append(i)
        return li

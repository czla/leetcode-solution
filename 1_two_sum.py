# Description:  给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
#               你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# Examples:     给定 nums = [2, 7, 11, 15], target = 9
#               因为 nums[0] + nums[1] = 2 + 7 = 9
#               所以返回 [0, 1]
# Author:       zlchen
# Date:         4/27/2019
# Performance:  1272 ms, surpass 40.70%'s python3 submissions


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try:
                j = nums[i + 1:].index(target - nums[i])
                return [i, j + i + 1]
            except:
                continue
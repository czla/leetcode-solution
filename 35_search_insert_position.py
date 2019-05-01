# Description:  给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
#               如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
#               你可以假设数组中无重复元素。
#
# Examples:     输入: [1,3,5,6], 5,   输出: 2
#               输入: [1,3,5,6], 2,   输出: 1
#               输入: [1,3,5,6], 7,   输出: 4
#               输入: [1,3,5,6], 0,   输出: 0
#
# Author:       zlchen
# Date:         4/30/2019
# Performance:  56 ms, surpass 61.69%'s python3 submissions


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            index = nums.index(target)
        except:
            nums.append(target)
            index = sorted(nums).index(target)

        return index
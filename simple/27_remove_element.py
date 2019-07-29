# Description:  给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
#
#               不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
#               元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
#
#
#
#
# Examples:     输入: [3,2,2,3], 3                  输出: 2
#               输入: [0,1,2,2,3,0,4,2], 2          输出: 5
#
# Difficulty:   Simple
# Author:       zlchen
# Date:         7/29/2019
# Performance:  48 ms, surpass 84.29%'s python3 submissions


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == val:
                del nums[i]
                length -= 1
            else:
                i += 1

        return length

    # faster
    def removeElement2(self, nums: List[int], val: int) -> int:
        while True:
            try:
                nums.remove(val)
            except:
                return len(nums)
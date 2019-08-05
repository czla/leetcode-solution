# Description:  实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
#               如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
#               必须原地修改，只允许使用额外常数空间。
#
#
#
# Examples:     输入: [1,2,3]      输出：[1,3,2]
#               输入: [3,2,1]      输出：[1,2,3]
#               输入: [1,1,5]      输出：[1,5,1]
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         8/5/2019
# Performance:  72 ms, surpass 28.78%'s python3 submissions


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length < 2:
            return

        # find the first pair, where n[index-1] <= n[index]
        index = -1
        while (nums[index] <= nums[index - 1]):
            index -= 1
            if index == -length:  # can not find pair, already ordered
                nums.reverse()
                return

        tmp = nums[index - 1]  # value to be swapped
        index1 = index - 1  # index to be swapped

        # find another index to be swapped, whose value is bigger than tmp and closest to tmp
        while nums[index] > tmp and index < 0:
            index += 1

        # swap
        nums[index1], nums[index - 1] = nums[index - 1], nums[index1]
        nums[index1 + 1:] = nums[:index1:-1]  # reverse the value of n[index+1:]

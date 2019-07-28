# Description:  给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
#               不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
#
# Examples:     输入: [1,1,2]                  输出: 2
#               输入: [0,0,1,1,1,2,2,3,3,4]    输出: 5
#
# Difficulty:   Simple
# Author:       zlchen
# Date:         7/28/2019
# Performance:  60 ms, surpass 27.55%'s python3 submissions


class Solution:
    # 手动遍历删除重复元素
    def removeDuplicates(self, nums) -> int:
        length = len(nums)
        i = 0
        while i < length - 1:
            if nums[i] == nums[i + 1]:
                del (nums[i + 1])
                # nums.pop(i+1)     # slower than del
                length -= 1
            else:
                i += 1

        return length

nums = [0,0,1,1,1,2,2,3,3,4]
Solution().removeDuplicates(nums)
# Description:  给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
#
#
# Examples:     输入: nums = [5,7,7,8,8,10], target = 8     输出：[3,4]
#               输入: nums = [5,7,7,8,8,10], target = 6     输出：[-1,-1]
#
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         8/12/2019
# Performance:  124 ms, surpass 29.51%'s python3 submissions


class Solution:
    def searchRange(self, nums, target: int):
        try:
            i = nums.index(target)
        except:
            return [-1, -1]

        n = 0
        j = i
        length = len(nums)
        while nums[j] == target:
            j += 1
            n += 1
            if j == length:
                break

        return [i, i + n - 1]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    print(Solution().searchRange(nums, target))
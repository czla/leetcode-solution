# Description:  给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
#
# Examples:     输入:[1, 2, 0]                输出：3
#               输入:[3, 4, -1, 1]            输出：2
#               输入:[7, 8, 9, 11, 12]        输出：1
#
# Difficulty:   Hard
# Author:       zlchen
# Date:         8/19/2019
# Performance:  56 ms, surpass 48.41%'s python3 submissions


class Solution:
    def firstMissingPositive(self, nums) -> int:
        for i in range(1, len(nums) + 2):
            if i not in nums:
                return i

    def firstMissingPositive2(self, nums) -> int:
        nums.sort()

        if 1 in nums:
            index = nums.index(1)
            length = len(nums)

            while index < length - 1 and nums[index + 1] - nums[index] < 2:
                index += 1
                if index == length - 1:
                    break
            return nums[index] + 1
        else:
            return 1


if __name__ == '__main__':
    nums = [1]
    print(Solution().firstMissingPositive(nums))
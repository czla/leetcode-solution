# Description:  给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
#               你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
#
# Examples:     输入: [2,2,1],        输出: 1
#               输入: [4,1,2,1,2],    输出: 4
#
# Difficulty:   Simple
# Author:       zlchen
# Date:         9/13/2019
# Performance:  136 ms, surpass 40.25%'s python3 submissions


class Solution:
    def singleNumber(self, nums) -> int:
        nums.sort()
        length = len(nums)
        i = 0
        while i < length - 2:
            if nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]

        return nums[-1]


if __name__ == '__main__':
    nums = [4,1,2,1,2]
    print(Solution().singleNumber(nums))
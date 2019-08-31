# Description:  给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
#               其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#
#               说明：请不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
#
# Examples:     输入: [1,2,3,4]
#               输出：[24,12,8,6]
#
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         8/31/2019
# Performance:  172 ms, surpass 50.76%'s python3 submissions


class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        left_prod, right_prod = [1] * length, [1] * length

        for i in range(1, length):
            left_prod[i] = left_prod[i - 1] * nums[i - 1]
            right_prod[length - i - 1] = right_prod[length - i] * nums[length - i]

        ans = [i*j for i,j in zip(left_prod,right_prod)]
        return ans


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(Solution().productExceptSelf(nums))
# Description:  给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
#
#               返回这三个数的和。假定每组输入只存在唯一答案。
#
# Examples:     输入: nums = [-1，2，1，-4], target = 1     输出: 2. 最接近的为(-1 + 2 + 1 = 2)
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         5/4/2019
# Performance:  184 ms, surpass 45.68%'s python3 submissions


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        length = len(nums)
        if length < 3:
            return None
        nums.sort()
        ans = sum(nums[:3])
        if ans  - target >= 0 or length == 3:
            return ans

        for i in range(length - 2):
            j = i + 1
            k = length - 1
            while(j < k):
                temp = nums[i] + nums[j] + nums[k]
                ans = temp if abs(temp - target) < abs(ans - target) else ans
                if ans == target:
                    return ans
                if temp < target:
                    j += 1
                else:
                    k -= 1

        return ans

if __name__ == '__main__':
    nums = [1,2,4,8,16,32,64,128]
    target = 82
    print(Solution().threeSumClosest(nums, target))
# Description:  给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
#               使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
#               注意：答案中不可以包含重复的四元组。
#
# Examples:     输入: nums = [1, 0, -1, 0, -2, 2], target = 0
#               输出: [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         5/6/2019
# Performance:  876 ms, surpass 64.67%'s python3 submissions


class Solution:
    def fourSum(self, nums, target: int):
        length = len(nums)
        if length < 4:
            return []
        nums.sort()
        ans = []
        if sum(nums[:4]) > target or sum(nums[-4:]) < target:
            return []

        for i in range(length - 3):
            for j in range(i + 1, length - 2):
                start = j + 1
                end = length - 1
                while start < end:
                    temp = nums[i] + nums[j] + nums[start] + nums[end]
                    if temp == target:
                        temp_ans = [nums[i], nums[j], nums[start], nums[end]]
                        if temp_ans not in ans:
                            ans.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1
                    elif temp < target:
                        start += 1
                    elif temp > target:
                        end -= 1

        return ans

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(Solution().fourSum(nums, target))
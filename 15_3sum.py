# Description:  给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
#               找出所有满足条件且不重复的三元组。
#
#               注意：答案中不可以包含重复的三元组。
#
# Examples:     输入: [-1, 0, 1, 2, -1, -4],     输出: [[-1, 0, 1], [-1, -1, 2]]
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         5/3/2019
# Performance:  412 ms, surpass 98.96%'s python3 submissions


class Solution:
    def threeSum(self, nums):
        length = len(nums)
        if length < 3:
            return []
        repeat = {}
        for i in nums:
            try:
                repeat[i] += 1
            except:
                repeat[i] = 1

        ans = []
        posnum = [value for value in repeat if value > 0]
        negnum = [value for value in repeat if value < 0]

        if repeat.get(0, 0) > 2:
            ans.append([0, 0, 0])

        for i, pos in enumerate(posnum):
            if repeat[pos] > 1 and - 2 * pos in repeat:
                ans.append([pos, pos, - 2 * pos])
            for pos2 in posnum[i + 1:]:
                if - pos - pos2 in repeat:
                    ans.append([pos, pos2, - pos - pos2])

        for j, neg in enumerate(negnum):
            if repeat[neg] > 1 and - 2 * neg in repeat:
                ans.append([neg, neg, - 2 * neg])
            for neg2 in negnum[j + 1:]:
                if - neg - neg2 in repeat:
                    ans.append([neg, neg2, - neg - neg2])

        if 0 in repeat:
            for x in posnum:
                if - x in negnum:
                    ans.append([0, x, -x])

        return ans

    # threeSum_2 is slower, using dynamic programming.
    def twoSum(self, nums, target):
        length = len(nums)
        if length < 2:
            return []
        ans = []

        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target and [nums[i], nums[j]] not in ans:
                    ans.append([nums[i], nums[j]])
        return ans

    def threeSum_2(self, nums):
        # nums = list(set(nums))
        length = len(nums)
        if length < 3:
            return []

        dp = [[] for _ in range(length)]
        dp[2] = [[nums[0], nums[1], nums[2]], ] if nums[0] + nums[1] + nums[2] == 0 else []

        for i in range(2, length - 1):
            dp[i + 1] = dp[i]
            ans = self.twoSum(nums[:i + 1], -nums[i + 1])
            for j in ans:
                # if not any([{j[0], j[1], nums[i + 1]} == set(k) for k in dp[i]]):
                if not any(list({j[0], j[1], nums[i + 1]} == k for k in map(set,dp[i]))):
                    dp[i + 1].append([j[0], j[1], nums[i + 1]])

        return dp[-1]


if __name__ == '__main__':
    nums = [3,0,-2,-1,1,2]
    # print(Solution().twoSum(nums, 5))
    print(Solution().threeSum(nums))
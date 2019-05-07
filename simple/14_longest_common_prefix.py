# Description:  编写一个函数来查找字符串数组中的最长公共前缀。
#
#               如果不存在公共前缀，返回空字符串 ""。
#
# Examples:     输入: ["flower","flow","flight"],     输出: "fl"
#               输入: ["dog","racecar","car"],        输出: ""
#
# Difficulty:   Simple
# Author:       zlchen
# Date:         5/2/2019
# Performance:  68 ms, surpass 33.29%'s python3 submissions


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        nums = len(strs)
        if nums < 1:
            return ''

        # dp[index] means longestCommonPrefix of strs[0:index].
        dp = [''] * nums
        dp[0] = strs[0]

        for i in range(nums - 1):
            for j, c in enumerate(dp[i]):
                if j < len(strs[i + 1]) and c == strs[i + 1][j]:
                    if j == len(dp[i]) - 1:
                        dp[i + 1] = dp[i][:j + 1]
                    continue
                dp[i+1] = dp[i][:j]
                break

        return dp[-1]


if __name__ == '__main__':
    strs = ['c', 'c']
    print(Solution().longestCommonPrefix(strs))
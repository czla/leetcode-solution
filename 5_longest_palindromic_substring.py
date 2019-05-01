# Description:    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# Examples:       输入: "babad", 输出: "bab", 注意: "aba" 也是一个有效答案。
#                 输入: "cbbd",  输出: "bb"
#
# Difficulty:     Medium
# Author:         zlchen
# Date:           4/29/2019
# Performance:    7476 ms, surpass 13.37%'s python3 submissions


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return s

        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        max_length = 1
        begin = 0

        for j in range(len(s)):
            for i in range(j + 1):
                if s[i] == s[j]:
                    if (j - i) <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > max_length:
                    max_length = j - i + 1
                    begin = i

        return s[begin: begin + max_length]

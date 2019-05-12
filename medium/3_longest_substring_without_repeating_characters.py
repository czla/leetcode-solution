# Description:  给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# Examples:     输入: "abcabcbb"      输出: 3   原因：无重复字符的最长子串是 "abc"
#               输入: "bbbbb"         输出: 1   原因：无重复字符的最长子串是 "b"
#               输入: "pwwkew"        输出: 3   原因：无重复字符的最长子串是 "wke"
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         5/12/2019
# Performance:  104 ms, surpass 77.54%'s python3 submissions


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        start = 0
        end = 0     # the processing string s[:end)
        ans = 0     # answer of processing string
        while end < length:
            if s[end] in s[start: end]:
                start += 1
            else:
                end += 1
                ans = max(ans, end - start)
        return ans

if __name__ == '__main__':
    s = 'au'
    print(Solution().lengthOfLongestSubstring(s))
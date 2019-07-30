# Description:  实现 strStr() 函数。
#
#               给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle
#               字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。
#               当 needle 是空字符串时我们应当返回 0
#
#
#
#
#
# Examples:     输入: haystack = "hello", needle = "ll"                 输出: 2
#               输入: haystack = "aaaaa", needle = "bba"                输出: -1
#
# Difficulty:   Simple
# Author:       zlchen
# Date:         7/30/2019
# Performance:  40 ms, surpass 98.05%'s python3 submissions


class Solution:
    # find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回-1
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    # index方法是在字符串里查找子串第一次出现的位置，类似字符串的find方法，
    # 不过比find方法更好的是，如果查找不到子串，会抛出异常，而不是返回 - 1
    def strStr2(self, haystack: str, needle: str) -> int:
        try:
            ans = haystack.index(needle)
        except:
            ans = -1

        return ans

    # 滑窗逐个比较
    def strStr3(self, haystack: str, needle: str) -> int:
        length = len(needle)
        for i in range(len(haystack) - length + 1):
            if haystack[i: i + length] == needle:
                return i

        return -1
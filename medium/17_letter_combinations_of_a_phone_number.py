# Description:  给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
#               给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#               {1:'', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
#
#               注意：答案中不可以包含重复的三元组。
#
# Examples:     输入: "23",     输出: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         5/5/2019
# Performance:  56 ms, surpass 48.77%'s python3 submissions


class Solution:
    def letterCombinations(self, digits: str):
        letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        length = len(digits)
        if length < 1:
            return []
        ans = [i for i in letters[int(digits[0])]]
        for i in range(1, length):
            ans = [x + y for x in ans for y in letters[int(digits[i])]]

        return ans


if __name__ == '__main__':
    digits = ''
    print(Solution().letterCombinations(digits))
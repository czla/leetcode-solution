# Description:  给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# Examples:     输入: n = 3
#               输出: [
#                       "((()))",
#                       "(()())",
#                       "(())()",
#                       "()(())",
#                       "()()()"
#                     ]
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         5/14/2019
# Performance:  96 ms, surpass 19.36%'s python3 submissions


class Solution:
    def generateParenthesis(self, n: int):
        result = []

        def trackback(S="", left=0, right=0):
            if len(S) == 2 * n:
                result.append(S)
            if left < n:
                trackback(S + '(', left + 1, right)
            if right < left:
                trackback(S + ')', left, right + 1)

        trackback()
        return result

if __name__ == '__main__':
    print(Solution().generateParenthesis(2))
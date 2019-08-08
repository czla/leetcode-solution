# Description:  给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
#
# Examples:     输入: '(()'       输出:2    解释: 最长有效括号子串为 '()'
#               输入: ')()())'    输出:4    解释: 最长有效括号子串为 '()()'
#
#
# Difficulty:   Hard
# Author:       zlchen
# Date:         8/8/2019
# Performance:  56 ms, surpass 96.69%'s python3 submissions


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = []
        stack.append(-1)
        for index, char in enumerate(s):
            if char == ')':
                stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    ans = max(ans, index - stack[-1])
            else:
                stack.append(index)

        return ans

    def isvalid(self, s:str) -> bool:
        if len(s) % 2 == 1:
            return False
        while '()' in s:
            s = s.replace('()', '')

        return s == ''


    # brute force search, slower
    def longestValidParentheses2(self, s: str) -> int:
        length = len(s)
        ans = 0
        for i in range(length):
            for j in range(i + 2, length + 1, 2):
                if self.isvalid(s[i:j]):
                    cur_length = j - i
                    ans = max(ans, cur_length)

        return ans


if __name__ == '__main__':
    s = '()(())(()'
    # print(Solution().longestValidParentheses(s))
    print(Solution().longestValidParentheses2(s))
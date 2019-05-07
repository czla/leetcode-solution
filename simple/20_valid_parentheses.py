# Description:  给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
#               有效字符串需满足：
#                   1. 左括号必须用相同类型的右括号闭合。
#                   2. 左括号必须以正确的顺序闭合。

#               注意空字符串可被认为是有效字符串。
#
# Examples:     输入: "()",       输出: true
#               输入: "()[]{}",   输出: true
#               输入: "(]",       输出: false
#               输入: "([)]",     输出: false
#               输入: "{[]}",     输出: true
#
# Difficulty:   Simple
# Author:       zlchen
# Date:         4/30/2019
# Performance:  76 ms, surpass 35.81%'s python3 submissions


class Solution:
    def isValid(self, s: str) -> bool:
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]', '')
            s = s.replace('()', '')
            s = s.replace('{}', '')
        return s == ''
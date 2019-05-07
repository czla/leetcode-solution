# Description:  判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# Examples:     输入: 121,    输出: true
#               输入: -121,   输出: false, 解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#               输入: 10,     输出: false, 解释: 从右向左读, 为 01 。因此它不是一个回文数。
#               输入: "words and 987",    输出: 0, 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。无法执行有效的转换。
#               输入: "-91283472332", 输出: -2147483648, 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 因此返回 INT_MIN (−2^31) 。
#
# Difficulty:   Simple
# Author:       zlchen
# Date:         4/30/2019
# Performance:  420 ms, surpass 23.67%'s python3 submissions


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = str(x)
        if y[::-1] == y:
            return True
        else:
            return False
# Description:  给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#               假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
#               请根据这个假设，如果反转后整数溢出那么就返回 0。
#
# Examples:     输入: 123,    输出: 321
#               输入: -123,   输出: -321
#               输入: 120,    输出: 21
#
# Author:       zlchen
# Date:         4/29/2019
# Performance:  56 ms, surpass 98.47%'s python3 submissions


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            res = -int(str(-x)[::-1])
        else:
            res = int(str(x)[::-1])
        return res if res >= -2**31 and res <= 2**31-1 else 0
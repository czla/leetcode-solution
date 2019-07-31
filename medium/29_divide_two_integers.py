# Description:  给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#
#               返回被除数 dividend 除以除数 divisor 得到的商。
#               被除数和除数均为 32 位有符号整数。
#               除数不为 0。
#               假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
#
#
# Examples:     输入: dividend = 10, divisor = 3      输出：3
#               输出: dividend = 7, divisor = -3      输出：-2
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         7/31/2019
# Performance:  56 ms, surpass 58.81%'s python3 submissions


class Solution:
    # 每次叠加divisor，当dividend很大，divisor很小时容易超时
    def divide(self, dividend: int, divisor: int) -> int:
        lower_bound = - 2 ** 31
        upper_bound = 2 ** 31 - 1
        if dividend < lower_bound or dividend > upper_bound or divisor < lower_bound or divisor > upper_bound:
            return upper_bound

        pos_flag = True
        if divisor < 0 :
            pos_flag = not pos_flag
            divisor = -divisor

        if dividend < 0:
            dividend = -dividend
            pos_flag = not pos_flag

        ans = 0
        seg = divisor
        while divisor <= dividend:
            ans += 1
            divisor += seg

        return ans if pos_flag else -ans

    # 移位操作
    def divide2(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0) ^ (divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        # 把除数不断左移，直到它大于被除数
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        result = 0
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                result += 1 << count  # 这里的移位运算是把二进制（第count+1位上的1）转换为十进制
                dividend -= divisor
        if sign: result = -result
        return result if -(1 << 31) <= result <= (1 << 31) - 1 else (1 << 31) - 1
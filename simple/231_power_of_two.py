# Description:  给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
#
#
# Examples:     输入: 1,      输出: true    解释: 2^0 = 1
#               输入: 16,     输出: true    解释: 2^4 = 16
#               输入: 218,    输出: false
#
# Difficulty:   Simple
# Author:       zlchen
# Date:         9/13/2019
# Performance:  48 ms, surpass 84.88%'s python3 submissions


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            n /= 2

        return True if n == 1 else False


if __name__ == '__main__':
    n = 218
    print(Solution().isPowerOfTwo(n))
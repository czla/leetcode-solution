# Description:  给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
#
#               说明：
#                   * num1 和 num2 的长度小于110
#                   * num1 和 num2 只包含数字 0-9。
#                   * num1 和 num2 均不以零开头，除非是数字 0 本身。
#                   * 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
#
#
# Examples:     输入: num1 = "2", num2 = "3"
#               输出："6"
#
#               输入: num1 = "123", num2 = "456"
#               输出："56088"
#
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         8/21/2019
# Performance:  52 ms, surpass 89.60%'s python3 submissions


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))


if __name__ == '__main__':
    num1 = '123'
    num2 = '456'
    print(Solution().multiply(num1, num2))
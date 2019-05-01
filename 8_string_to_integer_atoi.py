# Description:  将字符串转换成整数。
#               首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
#               当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，
#               作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
#
#               该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
#
#               注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，不需要进行转换。
#
#               在任何情况下，若函数不能进行有效的转换时，请返回 0。
#               假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−2^31,  2^31 − 1]。
#               如果数值超过这个范围，返回 INT_MAX (2^31 − 1) 或 INT_MIN (−2^31) 。
#
# Examples:     输入: "42",   输出: 42
#               输入: "   -42",   输出: -42, 解释：第一个非空白字符为 '-', 尽可能将负号与后面所有连续出现的数字组合起来。
#               输入: "4193 with words",  输出: 4193, 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
#               输入: "words and 987",    输出: 0, 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。无法执行有效的转换。
#               输入: "-91283472332", 输出: -2147483648, 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 因此返回 INT_MIN (−2^31) 。
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         4/30/2019
# Performance:  64 ms, surpass 84.77%'s python3 submissions


def find_num(str):
    for i, v in enumerate(str):
        if v.isdigit():
            continue
        else:
            break

    return 0 if i == 0 else int(str[:i])


class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        int_min = - 2 ** 31
        int_max = 2 ** 31 - 1
        try:
            if 'e' in str:
                str = str.replace('e', '#')
            ans = int(float(str))
        except:
            ans = 0
            if str[0] == '-' or str[0] == '+':
                if not str[1].isnumeric():
                    ans = 0
                else:
                    ans = find_num(str[1:])
                    ans = ans if str[0] == '+' else -ans
            elif str[0].isdigit():
                ans = find_num(str)
            else:
                ans = 0

        finally:
            ans = min(max(int_min, ans), int_max)
            return ans
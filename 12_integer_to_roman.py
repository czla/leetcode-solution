# Description:  罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
#
#               字符          数值
#               I             1
#               V             5
#               X             10
#               L             50
#               C             100
#               D             500
#               M             1000
#
#               例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II
#
#               通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。
#               数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。
#               这个特殊的规则只适用于以下六种情况：
#                   1. I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
#                   2. X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
#                   3. C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
#
#               给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
#
# Examples:     输入: 3,     输出: "III"
#               输入: 4,     输出: "IV"
#               输入: 9,     输出: "IX"
#               输入: 58,    输出: "LVIII", 解释: L = 50, V= 5, III = 3.
#               输入: 1994,  输出: "MCMXCIV", 解释: M = 1000, CM = 900, XC = 90, IV = 4.
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         5/2/2019
# Performance:  76 ms, surpass 99.54%'s python3 submissions


class Solution:
    def intToRoman(self, num: int) -> str:
        assert(num >= 1 and num <= 3999), print('输入超出范围！')
        thousand = num // 1000
        ans = thousand * 'M'

        hundred = num % 1000 // 100
        if hundred >= 5:
            if hundred == 9:
                ans += 'CM'
            else:
                ans += 'D' + (hundred - 5) * 'C'
        else:
            if hundred == 4:
                ans += 'CD'
            else:
                ans += (hundred) * 'C'

        ten = num % 100 // 10
        if ten >= 5:
            if ten == 9:
                ans += 'XC'
            else:
                ans += 'L' + (ten - 5) * 'X'
        else:
            if ten == 4:
                ans += 'XL'
            else:
                ans += (ten) * 'X'

        unit = num % 10
        if unit >= 5:
            if unit == 9:
                ans += 'IX'
            else:
                ans += 'V' + (unit - 5) * 'I'
        else:
            if unit == 4:
                ans += 'IV'
            else:
                ans += (unit) * 'I'
        return ans

    # this method is much more concise but slower slightly
    def intToRoman_2(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        ans = ''
        for i in range(len(values)):
            while(num >= values[i]):
                num -= values[i]
                ans += symbols[i]

        return ans



if __name__ == '__main__':
    num = 3632
    print(Solution().intToRoman(num))
    print(Solution().intToRoman_2(num))
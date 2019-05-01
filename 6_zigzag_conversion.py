# Description:  将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#               比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#               L   C   I   R
#               E T O E S I I G
#               E   D   H   N
#               之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#               请你实现这个将字符串进行指定行数变换的函数：
#               string convert(string s, int numRows);
#
# Examples:     输入: s = "LEETCODEISHIRING", numRows = 3, 输出: "LCIRETOESIIGEDHN"
#               输入: s = "LEETCODEISHIRING", numRows = 4, 输出: "LDREOEIIECIHNTSG"
#               解释:
#               L     D     R
#               E   O E   I I
#               E C   I H   N
#               T     S     G
#
# Author:       zlchen
# Date:         4/29/2019
# Performance:  132 ms, surpass 48.54%'s python3 submissions


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) < 3:
            return s

        ans = ''
        sep = 2 * numRows - 2
        for i in range(numRows):
            # print('line: ', i)
            # the first line and last line's seperation is sep
            if i == 0:
                ans = s[::sep]
                # print(ans)
                continue
            if i == numRows - 1:
                ans += s[numRows - 1::sep]
                return ans

            vertical_str = s[i::sep]
            # print('vertical_str: ', vertical_str)

            skew_str = s[2 * numRows - 2 - i::sep]
            # print('skew_str: ', skew_str)
            temp = list(vertical_str)
            for index, value in enumerate(skew_str):
                temp.insert(2 * index + 1, value)

            # print(temp)
            for x in temp:
                ans += str(x)
            # print(skew_str)
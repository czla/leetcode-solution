# Description:  给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
#
#               '.' 匹配任意单个字符。
#               '*' 匹配零个或多个前面的元素。
#               匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

#               说明：
#                   1. s 可能为空，且只包含从 a-z 的小写字母。
#                   2. p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

#               注意空字符串可被认为是有效字符串。
#
# Examples:     输入: s = "aa", p = "a"                   输出: false, 解释: "a" 无法匹配 "aa" 整个字符串。
#               输入: s = "aa", p = "a*"                  输出: true, 解释: '*' 重复 'a' 一次, 字符串可变为 "aa"。
#               输入: s = "ab", p = ".*"                  输出: true, 解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
#               输入: s = "aab", p = "c*a*b"              输出: true, 解释: 'c' 不被重复, 'a' 重复一次可以匹配字符串 "aab"。
#               输入: s = "mississippi", p = "mis*is*p*." 输出: false
#
# Solution:     We define dp[i][j] to be true if s[0..i) matches p[0..j) and false otherwise.
#               The state equations will be:
#                   1. dp[i][j] = dp[i - 1][j - 1], if p[j - 1] != '*' && (s[i - 1] == p[j - 1] || p[j - 1] == '.');
#                   2. dp[i][j] = dp[i][j - 2], if p[j - 1] == '*' and the pattern repeats for 0 time;
#                   3. dp[i][j] = dp[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == '.'), if p[j - 1] == '*' and the pattern repeats for at least 1 time.

# Difficulty:   Hard
# Author:       zlchen
# Date:         5/1/2019
# Performance:  56 ms, surpass 91.57%'s python3 submissions


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in xrange(m+1)]
        dp[0][0] = True
        for i in xrange(0, m+1):
            for j in xrange(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or ( i>0 and (s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j])
                else:
                    dp[i][j] = i>0 and dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
        return dp[m][n]
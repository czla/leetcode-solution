// Description:   给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
//
// Examples:      输入: "babad", 输出: "bab", 注意: "aba" 也是一个有效答案。
//                输入: "cbbd",  输出: "bb"
//
// Difficulty:    Medium
// Author:        zlchen
// Date:          4/29/2019
// Performance:   228 ms, surpass 36.94%'s C++ submissions


class Solution {
public:
    string longestPalindrome(string s) {
        int length = s.length();
        if(length < 1)
            return s;

        bool dp[length][length] = {false};
        int begin=0, max_length=1;
        for(int j=0; j != length; ++j)
        {
            for(int i=0; i != j+1; ++i){
                if(s[i] == s[j]){
                    if(j - i < 2)
                        dp[i][j] = true;
                    else
                        dp[i][j] = dp[i + 1][j - 1];
                }
                else
                    dp[i][j] = false;
                if(dp[i][j] && j-i+1 > max_length)
                {
                    max_length = j - i + 1;
                    begin = i;
                }
            }
        }

        return s.substr(begin, max_length);
    }
};
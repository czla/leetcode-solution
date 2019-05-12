// Description:  给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
//
// Examples:     输入: "abcabcbb"      输出: 3   原因：无重复字符的最长子串是 "abc"
//               输入: "bbbbb"         输出: 1   原因：无重复字符的最长子串是 "b"
//               输入: "pwwkew"        输出: 3   原因：无重复字符的最长子串是 "wke"
//
// Difficulty:   Medium
// Author:       zlchen
// Date:         5/12/2019
// Performance:  48 ms, surpass 53.75%'s C++ submissions


class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start = 0, end = 0, ans = 0;
        int length = s.size();
        while(end < length){
            if(s.substr(start, end - start).find(s[end]) != string::npos)
                start++;
            else{
                end++;
                ans = max(ans, end - start);
            }
        }

        return ans;
    }
};
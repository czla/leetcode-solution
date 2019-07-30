// Description:  实现 strStr() 函数。
//
//               给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle
//               字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。
//               当 needle 是空字符串时我们应当返回 0
//
//
//
//
//
// Examples:     输入: haystack = "hello", needle = "ll"                 输出: 2
//               输入: haystack = "aaaaa", needle = "bba"                输出: -1
//
// Difficulty:   Simple
// Author:       zlchen
// Date:         7/30/2019
// Performance:  4 ms, surpass 94.25%'s python3 submissions


class Solution {
public:
    // find()返回值是字母在母串中的位置（下标记录），如果没有找到，那么会返回一个特别的标记npos
    int strStr(string haystack, string needle) {
        int ans = haystack.find(needle);
        if(ans == haystack.npos)
            ans = -1;

        return ans;
    }

    // s.substr(pos, n)包含s中从pos开始的n个字符的拷贝
    // slower, 12ms
    int strStr(string haystack, string needle) {
        int length = needle.size();
        if(length > haystack.size())
            return -1;

        for(int i = 0; i != haystack.size() - length + 1; ++i){
            if(haystack.substr(i, length) == needle)
                return i;
        }

        return -1;
    }
};
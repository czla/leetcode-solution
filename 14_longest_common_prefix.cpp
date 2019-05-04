// Description:  编写一个函数来查找字符串数组中的最长公共前缀。
//
//               如果不存在公共前缀，返回空字符串 ""。
//
// Examples:     输入: ["flower","flow","flight"],     输出: "fl"
//               输入: ["dog","racecar","car"],        输出: ""
//
// Difficulty:   Simple
// Author:       zlchen
// Date:         5/2/2019
// Performance:  12 ms, surpass 95.26%'s C++ submissions


class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int nums = strs.size();
        if(nums < 1)
            return "";
        // dp[index] means longestCommonPrefix of strs[0:index].
        string dp[nums];
        dp[0] = strs[0];

        for(int i = 0; i != nums - 1; ++i){
            for(int j = 0; j != dp[i].size(); ++j){
                if(j < dp[i + 1].size() - 1 && dp[i][j] == strs[i + 1][j]){
                    if(j == dp[i].size() - 1){
                        dp[i + 1] = dp[i].substr(0, j + 1);
                        }
                    continue;
                }
                dp[i + 1] = dp[i].substr(0, j);
                break;
            }
        }
        return dp[nums - 1];
    }
};
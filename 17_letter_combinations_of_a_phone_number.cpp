// Description:  给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
//
//               给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
//               {1:'', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
//
//               注意：答案中不可以包含重复的三元组。
//
// Examples:     输入: "23",     输出: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
//
// Difficulty:   Medium
// Author:       zlchen
// Date:         5/5/2019
// Performance:  8 ms, surpass 95.24%'s C++ submissions


class Solution {
public:
    vector<string> letterCombinations(string digits) {
        int length = digits.size();
        vector<string> ans;
        if(length < 1)
            return ans;
        string letters[] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        for(int i = 0; i != letters[digits[0] - '0'].size(); ++i){
            ans.push_back(letters[digits[0] - '0'].substr(i,1));
        }
        for(int i = 1; i != length; ++i){
            vector<string> ans_temp;
            for(int j = 0; j != ans.size(); ++j){
                for(int k = 0; k != letters[digits[i] - '0'].size(); ++k){
                    string temp = ans[j] + letters[digits[i] - '0'].substr(k,1);
                    ans_temp.push_back(temp);
                }
            }
            ans.clear();
            ans = ans_temp;
        }
        return ans;
    }
};
// Description:  给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
//
//
// Examples:     输入: '(()'       输出:2    解释: 最长有效括号子串为 '()'
//               输入: ')()())'    输出:4    解释: 最长有效括号子串为 '()()'
//
//
// Difficulty:   Hard
// Author:       zlchen
// Date:         8/8/2019
// Performance:  8 ms, surpass 84.33%'s C++ submissions


class Solution {
public:
    int longestValidParentheses(string s) {
        int ans = 0;
        int length = s.size();
        vector<int> stack = {-1};
        for(int i = 0; i != length; ++i){
            if(s[i] == ')'){
                stack.pop_back();
                if(stack.size() == 0)
                    stack.push_back(i);
                else
                    ans = max(ans, i - *stack.rbegin());
            }
            else
                stack.push_back(i);
        }

        return ans;
    }
};
// Description:  给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
//
// Examples:     输入:[0,1,0,2,1,0,1,3,2,1,2,1]                输出：6
//
//
//
// Difficulty:   Hard
// Author:       zlchen
// Date:         8/20/2019
// Performance:  8 ms, surpass 82.00%'s C++ submissions


class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0, length = height.size();
        if(length < 3)
            return 0;

        vector<int> left_max(length, height[0]), right_max(length, height[length - 1]);
        for(int i = 1; i != length; ++i)
            left_max[i] = max(left_max[i - 1], height[i]);

        for(int i = length - 2; i != -1; --i)
            right_max[i] = max(right_max[i + 1], height[i]);

        for(int i = 1; i != length - 1; ++i)
            ans += min(left_max[i], right_max[i]) - height[i];

        return ans;
    }
};
// Description:  给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
//               其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
//
//               说明：请不要使用除法，且在 O(n) 时间复杂度内完成此题。
//
//
// Examples:     输入: [1,2,3,4]
//               输出：[24,12,8,6]
//
//
// Difficulty:   Medium
// Author:       zlchen
// Date:         8/31/2019
// Performance:  88 ms, surpass 30.62%'s C++ submissions


class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int length = nums.size();
        vector<int> left_prod(length, 1), right_prod(length, 1), ans;

        for(int i = 1; i != length; ++i){
            left_prod[i] = left_prod[i - 1] * nums[i - 1];
            right_prod[length - i - 1] = right_prod[length - i] * nums[length - i];
        }

        for(int i = 0; i != length; ++i)
            ans.push_back(left_prod[i] * right_prod[i]);
        return ans;
    }
};
// Description:  给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
//
//               你的算法时间复杂度必须是 O(log n) 级别。
//
//               如果数组中不存在目标值，返回 [-1, -1]。
//
//
//
// Examples:     输入: nums = [5,7,7,8,8,10], target = 8     输出：[3,4]
//               输入: nums = [5,7,7,8,8,10], target = 6     输出：[-1,-1]
//
//
// Difficulty:   Medium
// Author:       zlchen
// Date:         8/12/2019
// Performance:  16 ms, surpass 42.08%'s C++ submissions


class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int>::iterator i = find(nums.begin(), nums.end(), target);
        vector<int> ans;
        if(i == nums.end()){
            ans = {-1, -1};
            return ans;}

        int n = 0, length = nums.size();
        vector<int>::iterator j = i;
        while(*j == target){
            j++;
            n++;
            if(j == nums.end())
                break;
        }

        ans = {i - nums.begin(), i - nums.begin() + n - 1};

        return ans;
    }
};
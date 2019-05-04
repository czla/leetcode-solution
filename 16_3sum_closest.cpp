// Description:  给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
//
//               返回这三个数的和。假定每组输入只存在唯一答案。
//
// Examples:     输入: nums = [-1，2，1，-4], target = 1     输出: 2. 最接近的为(-1 + 2 + 1 = 2)
//
// Difficulty:   Medium
// Author:       zlchen
// Date:         5/4/2019
// Performance:  12 ms, surpass 97.91%'s C++ submissions


class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int length = nums.size();
        if(length < 3)
            return NULL;
        sort(nums.begin(), nums.end());
        int ans = nums[0] + nums[1] + nums[2];
        if(ans - target >= 0 || length == 3)
            return ans;

        for(vector<int>::iterator i = nums.begin(); i != nums.end() - 2; ++i){
            if(i != nums.begin() && *i == *(i-1))
                continue;
            vector<int>::iterator j = i + 1, k = nums.end() - 1;
            while(j < k){
                int temp = *i + *j + *k;
                ans = abs(temp - target) < abs(ans - target) ? temp: ans;
                if(temp == target)
                    return ans;
                if(temp > target)
                    k--;
                else
                    j++;
            }
        }

        return ans;
    }
};
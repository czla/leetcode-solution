// Description:  给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
//               你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
//
// Examples:     给定 nums = [2, 7, 11, 15], target = 9
//               因为 nums[0] + nums[1] = 2 + 7 = 9
//               所以返回 [0, 1]
// Difficulty:   Simple
// Author:       zlchen
// Date:         4/27/2019
// Performance:  164 ms, surpass 49.55%'s C++ submissions


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> a;
        for(vector<int>::iterator iter1 = nums.begin(); iter1 != nums.end(); ++iter1)
        {
            vector<int>::iterator iter2 = find(iter1+1, nums.end(), target - *iter1);
            if (iter2 == nums.end())
            {
                continue;
            }

            a.push_back(iter1 - nums.begin());
            a.push_back(iter2 - nums.begin());
        }

        return a;
    }
};
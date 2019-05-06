// Description:  给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
//               使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
//
//               注意：答案中不可以包含重复的四元组。
//
// Examples:     输入: nums = [1, 0, -1, 0, -2, 2], target = 0
//               输出: [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]
//
// Difficulty:   Medium
// Author:       zlchen
// Date:         5/6/2019
// Performance:  36 ms, surpass 92.21%'s C++ submissions


class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int length = nums.size();
        vector<vector<int>> ans;
        if(length < 4)
            return ans;
        sort(nums.begin(), nums.end());
        if(accumulate(nums.begin(), nums.begin() + 4, 0) > target || accumulate(nums.end() - 4, nums.end(), 0) < target)
            return ans;

        // index will be faster than iterator for leetcode
        for(int i = 0; i != length - 3; ++i){
            for(int j = i + 1; j != length - 2; ++j){
                int start = j + 1, end = length - 1;
                while(start < end){
                    int temp = nums[i] + nums[j] + nums[start] + nums[end];
                    if(temp == target){
                        vector<int> temp_ans{nums[i], nums[j], nums[start], nums[end]};
                        if(find(ans.begin(), ans.end(), temp_ans) == ans.end())
                            ans.push_back(temp_ans);
                        start++;
                        end--;
                    }
                    else if(temp < target)
                        start++;
                    else if(temp > target)
                        end--;
                }
            }
        }

        return ans;
    }
};
// Description:  假设按照升序排序的数组在预先未知的某个点上进行了旋转。
//
//               ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
//
//               搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
//
//               你可以假设数组中不存在重复的元素。
//
//               你的算法时间复杂度必须是 O(log n) 级别。
//
//
//
// Examples:     输入: nums = [4,5,6,7,0,1,2], target = 0     输出：4
//               输入: nums = [4,5,6,7,0,1,2], target = 3     输出：-1
//
//
// Difficulty:   Medium
// Author:       zlchen
// Date:         8/9/2019
// Performance:  0 ms, surpass 100%'s C++ submissions


class Solution {
public:
    int search(vector<int>& nums, int target) {
         int ans = -1;
         vector<int>::iterator index = find(nums.begin(), nums.end(), target);
         if(index != nums.end())
             ans = index - nums.begin();

         return ans;
    }


    int search2(vector<int>& nums, int target) {
        int length = nums.size();
        for(int i = 0; i != length; ++i){
            if(target == nums[i])
                return i;
            else if(target > nums[i])
                continue;
            else{
                for(int j = length - 1; j != 0; --j){
                    if(nums[j] > nums[0])
                        return -1;
                    if(target == nums[j])
                        return j;
                }
            }
        }

        return -1;
    }
};
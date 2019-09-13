// Description:  给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
//
//               你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
//
//
// Examples:     输入: [2,2,1],        输出: 1
//               输入: [4,1,2,1,2],    输出: 4
//
// Difficulty:   Simple
// Author:       zlchen
// Date:         9/13/2019
// Performance:  24 ms, surpass 45.59%'s C++ submissions


class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int length = nums.size();
        int i = 0;
        sort(nums.begin(), nums.end());
        while(i < length - 2){
            if(nums[i] == nums[i + 1])
                i += 2;
            else
                return nums[i];
        }

        return nums[length - 1];
    }
};
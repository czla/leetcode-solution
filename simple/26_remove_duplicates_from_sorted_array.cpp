// Description:  给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
//
//               不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
//
//
// Examples:     输入: [1,1,2]                  输出: 2
//               输入: [0,0,1,1,1,2,2,3,3,4]    输出: 5
//
// Difficulty:   Simple
// Author:       zlchen
// Date:         7/28/2019
// Performance:  28 ms, surpass 91.21%'s C++ submissions


class Solution {
public:
    // 使用 unique 函数将重复的相邻元素放在 vector 末尾，返回值为末尾第一个重复元素的地址
    // 最后调用 erase 函数，删掉重复元素
    int removeDuplicates(vector<int>& nums) {
        nums.erase(unique(nums.begin(), nums.end()), nums.end());
        return nums.size();
    }

    // 手动遍历删除重复元素
    int removeDuplicates2(vector<int>& nums) {
         int length = nums.size();
         int i = 0;
         while(i < length - 1){
             if(nums[i] == nums[i + 1]){
                 nums.erase(nums.begin() + i + 1);
                 length--;
             }
             else
                 i++;
         }

         return length;

    }
};
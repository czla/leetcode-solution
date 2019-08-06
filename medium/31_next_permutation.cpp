// Description:  实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
//
//               如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
//
//               必须原地修改，只允许使用额外常数空间。
//
//
//
// Examples:     输入: [1,2,3]      输出：[1,3,2]
//               输入: [3,2,1]      输出：[1,2,3]
//               输入: [1,1,5]      输出：[1,5,1]
//
// Difficulty:   Medium
// Author:       zlchen
// Date:         8/5/2019
// Performance:  16 ms, surpass 53.77%'s C++ submissions


class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int length = nums.size();
        if(length < 2)
            return;

        // find the first pair, where n[index-1] <= n[index]
        int index = length - 1;

        while(nums[index] <= nums[index - 1]){
            index--;

            if(index == 0){
                reverse(nums.begin(), nums.end());  // can not find pair, already ordered
                return;
            }
        }

        int tmp = nums[index - 1];   // value to be swapped
        int index1 = index - 1;     // index to be swapped

        // find another index to be swapped, whose value is bigger than tmp and closest to tmp
        while(nums[index] > tmp ){
            index++;
            if(index == length)
                break;
        }

        // swap
        swap(nums[index1], nums[index - 1]);
        reverse(nums.begin() + index1 + 1, nums.end());
    }
};
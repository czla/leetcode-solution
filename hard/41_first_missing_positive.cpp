// Description:  给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
//
// Examples:     输入:[1, 2, 0]                输出：3
//               输入:[3, 4, -1, 1]            输出：2
//               输入:[7, 8, 9, 11, 12]        输出：1
//
// Difficulty:   Hard
// Author:       zlchen
// Date:         8/19/2019
// Performance:  4 ms, surpass 85.58%'s C++ submissions


class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
         for(int i = 1; i != nums.size() + 2; ++i){
         if(find(nums.begin(), nums.end(), i) == nums.end())
             return i;
         }
         return 0;
     }

    int firstMissingPositive2(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int>::iterator index = find(nums.begin(), nums.end(), 1);
        int length = nums.size();
        if(index != nums.end()){
            while(index < nums.end() - 1 && (*(index + 1) - *index < 2)){
                index++;
                if(index == nums.end() - 1)
                    break;
            }
            return *index + 1;
        }
        else
            return 1;
    }
};
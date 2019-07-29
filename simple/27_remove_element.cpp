// Description:  给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
//
//               不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
//
//               元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
//
//
//
//
// Examples:     输入: [3,2,2,3], 3                  输出: 2
//               输入: [0,1,2,2,3,0,4,2], 2          输出: 5
//
// Difficulty:   Simple
// Author:       zlchen
// Date:         7/29/2019
// Performance:  4 ms, surpass 91.65%'s C++ submissions


class Solution {
public:
    // faster, 4ms
    int removeElement(vector<int>& nums, int val) {
        int length = nums.size();
        int i = 0;
        while(i < length){
            if(nums[i] == val){
                nums.erase(nums.begin() + i);
                length--;
            }
            else
                i++;
        }

        return length;
    }

    // remove函数可以将迭代器范围内的等于某个值的元素“删除“（这里的删除是不改变容器的大小，只是将一些不满足条件的元素前移，
    // 这样的话保留的元素都移到了容器的前面，而remove正好就指向这些保留元素后的第一个元素，而后面的就是要删除的。）
    // 然后执行erase操作就可以了
    // 8ms
    int removeElement2(vector<int>& nums, int val) {
        nums.erase(remove(nums.begin(), nums.end(), val), nums.end());

        return nums.size();
    }
};
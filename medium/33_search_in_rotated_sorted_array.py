# Description:  假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
#               ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
#               搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
#               你可以假设数组中不存在重复的元素。
#
#               你的算法时间复杂度必须是 O(log n) 级别。
#
#
#
# Examples:     输入: nums = [4,5,6,7,0,1,2], target = 0     输出：4
#               输入: nums = [4,5,6,7,0,1,2], target = 3     输出：-1
#
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         8/9/2019
# Performance:  60 ms, surpass 42.04%'s python3 submissions


class Solution:
    def search3(self, nums, target: int) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] == target:
                return i

        return -1


    # log(n)
    def search2(self, nums, target: int) -> int:
        length = len(nums)
        for i in range(length):
            if target == nums[i]:
                return i
            elif target > nums[i]:
                continue
            else:
                for j in range(length - 1, 0 , -1):
                    if nums[j] > nums[0]:
                        return -1
                    if target == nums[j]:
                        return j


        return -1


    # faster
    def search3(self, nums, target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1


if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 8
    print(Solution().search(nums, target))
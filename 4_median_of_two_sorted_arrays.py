# Description:  给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#               请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#               你可以假设 nums1 和 nums2 不会同时为空。
#
# Examples:     nums1 = [1, 3] nums2 = [2], 则中位数是 2.0
#               nums1 = [1, 2] nums2 = [3, 4], 则中位数是 (2 + 3)/2 = 2.5
# Author:       zlchen
# Date:         4/28/2019
# Performance:  128 ms, surpass 44.10%'s python3 submissions


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = sorted(nums1 + nums2)
        index = len(num) // 2
        if len(num) % 2 == 1:
            return num[index]
        else:
            return (num[index - 1] + num[index]) / 2
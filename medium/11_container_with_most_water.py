# Description:  给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
#               在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
#               找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
#               说明：你不能倾斜容器，且 n 的值至少为 2。
#
# Examples:     输入: [1,8,6,2,5,4,8,3,7],    输出: 49
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         5/2/2019
# Performance:  88 ms, surpass 62.06%'s python3 submissions


class Solution:
    def maxArea(self, height) -> int:
        length = len(height)
        ans = min(height[0], height[-1]) * (length - 1)

        begin = 0
        end = length - 1

        while(begin < end):
            if (height[begin] < height[end]):
                begin += 1
            else:
                end -= 1
            area = min(height[begin], height[end]) * (end - begin)
            if area > ans:
                ans = area

        return ans


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))
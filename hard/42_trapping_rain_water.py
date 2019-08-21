# Description:  给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
# Examples:     输入:[0,1,0,2,1,0,1,3,2,1,2,1]                输出：6
#
#
#
# Difficulty:   Hard
# Author:       zlchen
# Date:         8/20/2019
# Performance:  76 ms, surpass 51.89%'s python3 submissions


class Solution:
    # O(n)
    def trap(self, height) -> int:
        ans = 0
        length = len(height)
        if length < 3:
            return 0

        left_max, right_max = [height[0]] * length, [height[length - 1]] * length
        for i in range(1, length):
                left_max[i] = max(height[i], left_max[i - 1])
        for i in range(length - 2, -1, -1):
                right_max[i] = max(height[i], right_max[i + 1])

        for i in range(1, length - 1):
            ans += min(left_max[i], right_max[i]) - height[i]   # trap water at every location

        return ans


    # O(n2)
    def trap2(self, height) -> int:
        ans = 0
        length = len(height)
        if length < 3:
            return 0

        for i in range(1, length - 1):
            left_max, right_max = 0, 0
            for j in range(0, i + 1):
                left_max = max(left_max, height[j])
            for k in range(i, length):
                right_max = max(right_max, height[k])

            ans += min(left_max, right_max) - height[i]     # trap water at every location

        return ans

    def count_middle_zero(self, height):
        cnt = 0
        length = len(height)
        start, end = 0, length - 1
        while start < end:
            if height[start] != 0 and height[end] != 0:
                break
            if height[start] == 0:
                start += 1
            if height[end] == 0:
                end -= 1

        # for i in range(start, end + 1):
        #     if height[i] == 0:
        #         cnt += 1

        return height[start: end + 1].count(0)

    # slower
    def trap3(self, height) -> int:
        ans = 0
        if len(height) < 3:
            return 0
        max_height = max(height)
        while max_height:
            ans += self.count_middle_zero(height)
            height = [max(0, i - 1) for i in height]
            max_height -= 1

        return ans


if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(height))
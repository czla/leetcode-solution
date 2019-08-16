# Description:  给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
#               candidates 中的数字可以无限制重复被选取。
#
#               说明：
#                   * 所有数字（包括 target）都是正整数。
#                   * 解集不能包含重复的组合。 
#
#
# Examples:     输入: candidates = [2,3,6,7], target = 7
#               输出：[[7], [2,2,3]]
#
#               输入: candidates = [2,3,5], target = 8
#               输出：[[2,2,2,2], [2,3,3], [3,5]]
#
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         8/16/2019
# Performance:  92 ms, surpass 66.47%'s python3 submissions


class Solution:
    def combinationSum(self, candidates, target: int):
        candidates = [i for i in candidates if i <= target]
        candidates.sort()
        ans = []
        length = len(candidates)
        if length == 1:
            if target % candidates[0] == 0:
                return [[candidates[0]] * (target // candidates[0])]
            else:
                return []
        elif length == 0:
            return []


        # recursion
        tmp = self.combinationSum(candidates[:length - 1], target)  # get tmp answer without using the last value
        if tmp:
            ans += tmp
        N = target // candidates[length - 1]    # use the last value N times
        for i in range(1, N + 1):
            sub = target - i * candidates[length - 1]
            print(sub)

            # finished with only last value i times
            if sub == 0:
                tmp = [[candidates[length - 1]] * i]
                ans += tmp
            else:
                tmp = self.combinationSum(candidates[:length - 1], sub)
                for x in tmp:
                    x += i * [ candidates[length - 1]]
                if tmp:
                    ans += tmp

        return ans


if __name__ == '__main__':
    candidates = [1,2]
    target = 4
    print(Solution().combinationSum(candidates, target))
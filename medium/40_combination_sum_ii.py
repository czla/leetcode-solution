# Description:  给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
#               candidates 中的每个数字在每个组合中只能使用一次。
#
#               说明：
#                   * 所有数字（包括 target）都是正整数。
#                   * 解集不能包含重复的组合。 
#
#
# Examples:     输入: candidates = [10,1,2,7,6,1,5], target = 8
#               输出：[[1,7], [1,2,5], [2,6], [1,1,6]]
#
#               输入: candidates = [2,5,2,1,2], target = 5
#               输出：[[1,2,2], [5]]
#
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         8/17/2019
# Performance:  128 ms, surpass 39.63%'s python3 submissions


class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates = [i for i in candidates if i <= target]
        candidates.sort()
        ans = []
        length = len(candidates)
        if length == 1:
            if target == candidates[0]:
                return [[target]]
            else:
                return []
        elif length == 0:
            return []


        # recursion
        tmp = self.combinationSum2(candidates[:length - 1], target)  # get tmp answer without using the last value
        for x in tmp:
            if x not in ans:
                ans.append(x)
        sub = target - candidates[length - 1]

        # finished with only last value i times
        if sub == 0:
            tmp = [candidates[length - 1]]
            if tmp not in ans:
                ans.append(tmp)
        else:
            tmp = self.combinationSum2(candidates[:length - 1], sub)
            for x in tmp:
                x.append(candidates[length - 1])
                if x not in ans:
                    ans.append(x)

        return ans


if __name__ == '__main__':
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(Solution().combinationSum2(candidates, target))
// Description:  给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
//
//               candidates 中的每个数字在每个组合中只能使用一次。
//
//               说明：
//                   * 所有数字（包括 target）都是正整数。
//                   * 解集不能包含重复的组合。 
//
//
// Examples:     输入: candidates = [10,1,2,7,6,1,5], target = 8
//               输出：[[1,7], [1,2,5], [2,6], [1,1,6]]
//
//               输入: candidates = [2,5,2,1,2], target = 5
//               输出：[[1,2,2], [5]]
//
//
// Difficulty:   Medium
// Author:       zlchen
// Date:         8/17/2019
// Performance:  152 ms, surpass 10.79%'s C++ submissions


class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int>::iterator i;
        for(i = candidates.begin(); i != candidates.end(); ++i){
        if(*i > target)
            break;
        }

        candidates.erase(i, candidates.end());
        vector<vector<int>> ans;
        int length = candidates.size();
        if(length == 1){
            if(target == candidates[0]){
                vector<int> tmp{target};
                ans.push_back(tmp);
                return ans;
            }
            else{
                vector<vector<int>> tmp;
                return tmp;
            }
        }
        else if(length == 0){
                vector<vector<int>> tmp;
                return tmp;
            }

        vector<int> erase_last(candidates.begin(), candidates.end() - 1);
        vector<vector<int>> tmp = combinationSum2(erase_last, target);

        if(tmp.size() > 0){
            for(auto &i:tmp){
                if(find(ans.begin(), ans.end(), i) == ans.end())
                    ans.push_back(i);}}
        int sub = target - candidates[length - 1];

        if(sub == 0){
            vector<int> tmp{target};
            if(find(ans.begin(), ans.end(), tmp) == ans.end())
                ans.push_back(tmp);
        }
        else{
            vector<int> erase_last(candidates.begin(), candidates.end() - 1);
            vector<vector<int>> tmp = combinationSum2(erase_last, sub);
            for(auto &x:tmp){
                x.push_back(candidates[length - 1]);
                if(find(ans.begin(), ans.end(), x) == ans.end())
                    ans.push_back(x);
            }
        }
        return ans;
    }
};
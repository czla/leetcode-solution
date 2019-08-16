// Description:  给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
//
//               candidates 中的数字可以无限制重复被选取。
//
//               说明：
//                   * 所有数字（包括 target）都是正整数。
//                   * 解集不能包含重复的组合。 
//
//
// Examples:     输入: candidates = [2,3,6,7], target = 7
//               输出：[[7], [2,2,3]]
//
//               输入: candidates = [2,3,5], target = 8
//               输出：[[2,2,2,2], [2,3,3], [3,5]]
//
//
// Difficulty:   Medium
// Author:       zlchen
// Date:         8/16/2019
// Performance:  24.06 ms, surpass 66.47%'s C++ submissions


class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
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
            if(target % candidates[0] == 0){
                vector<int> tmp(int(target/candidates[0]), candidates[0]);
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
        vector<vector<int>> tmp = combinationSum(erase_last, target);

        if(tmp.size() > 0){
            for(auto &i:tmp)
                ans.push_back(i);}
        int N = int(target / candidates[length - 1]);
        for(int i = 1; i != N + 1; ++i){
            int sub = target - i * candidates[length - 1];

            if(sub == 0){
                vector<int> tmp(i, candidates[length - 1]);
                ans.push_back(tmp);
            }
            else{
                vector<int> erase_last(candidates.begin(), candidates.end() - 1);
                vector<vector<int>> tmp = combinationSum(erase_last, sub);
                for(auto &x:tmp){
                    for(int j = 0; j != i; ++j)
                        x.push_back(candidates[length - 1]);
                }
                if(tmp.size() > 0){
            for(auto &i:tmp)
                ans.push_back(i);}
            }
        }

        return ans;
    }
};
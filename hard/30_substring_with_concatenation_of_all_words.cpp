// Description:  给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
//
//               注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
//
//               如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
//
//
// Examples:     输入: s = "barfoothefoobarman", words = ["foo","bar"]
//               输出: [0,9]
//               解释：
//                   从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
//                   输出的顺序不重要, [9,0] 也是有效答案。
//               输入: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
//               输出: []
//
// Difficulty:   Hard
// Author:       zlchen
// Date:         8/2/2019
// Performance:  828 ms, surpass 24.35%'s C++ submissions


class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> ans;
        if(words.size() == 0 || s.size() == 0)
            return ans;

        map<string, int> words_dict, cur_dict;

        for(vector<string>::iterator it = words.begin(); it != words.end(); ++it){
            words_dict[*it] += 1;
        }

        cur_dict = words_dict;

        int length = words.size();
        int length_word = words[0].size();
        int length_total = length * length_word;

        for(int i = 0; i != s.size() - length_total + 1; ++i){
            int j = i;
            while(j != length_total + i){
                string cur_word = s.substr(j, length_word);
                if(cur_dict[cur_word] >= 0){
                    cur_dict[cur_word]--;
                    if(cur_dict[cur_word] < 0)
                        break;
                    j += length_word;
                }
                else
                    break;
            }

            if(j == length_total + i)
                ans.push_back(i);

            cur_dict = words_dict;
        }


        return ans;
    }
};
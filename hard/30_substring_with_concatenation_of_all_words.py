# Description:  给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
#
#               注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
#
#               如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
#
# Examples:     输入: s = "barfoothefoobarman", words = ["foo","bar"]
#               输出: [0,9]
#               解释：
#                   从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
#                   输出的顺序不重要, [9,0] 也是有效答案。
#               输入: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
#               输出: []
#
# Difficulty:   Hard
# Author:       zlchen
# Date:         8/1/2019
# Performance:  512 ms, surpass 75.18%'s python3 submissions


import itertools
class Solution:
    def findSubstring(self, s, words):
        ans = []
        if not words or not s:
            return ans
        length = len(words)
        sub = list(itertools.permutations(words, length))
        sub_str = []

        # get all the sub_str, this method takes more memory to store sub_str
        for i in sub:
            tmp = ''.join(i)
            if tmp not in sub_str:
                sub_str.append(tmp)

        # print(sub_str)

        for j in sub_str:
            index = s.find(j)
            while index != -1:
                ans.append(index)
                index = s.find(j, index + 1)
            ans = list(set(ans))

        return ans


    # Recommend!!
    # using hashmap to store words, easier to analyse combination of words
    def findSubstring2(self, s, words):
        ans = []
        if not words or not s:
            return ans

        # get word dict, words_dict[i] counts the times of i
        words_dict = dict()
        for i in words:
            if i in words_dict:
                words_dict[i] += 1
            else:
                words_dict[i] = 1
        # print(words_dict)

        # this dict changes during search
        cur_dict = words_dict.copy()

        length = len(words)
        length_word = len(words[0])
        length_total = length * length_word

        # index of answer
        for i in range(len(s) - length_total + 1):
            j = i
            while j != length_total + i:
                cur_word = s[j:j + length_word]
                if cur_word in cur_dict:
                    cur_dict[cur_word] -= 1
                    if cur_dict[cur_word] < 0:  # not match
                        break
                    j += length_word
                else:
                    break   # not match

            if j == length_total + i:
                ans.append(i)

            # reset cur_dict for every index
            cur_dict = words_dict.copy()

        return ans


if __name__ == '__main__':
    s = 'wordgoodgoodgoodbestword'
    words = ['word', 'good', 'best', 'word']
    print(Solution().findSubstring2(s, words))
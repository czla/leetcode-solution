// Description:  报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
//
//               1.     1
//               2.     11
//               3.     21
//               4.     1211
//               5.     111221
//
//               1 被读作  "one 1"  ("一个一") , 即 11。
//               11 被读作 "two 1s" ("两个一"）, 即 21。
//               21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
//
//               给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
//
//
// Examples:     输入: 1,   输出: "1"
//               输入: 4,   输出: "1211"
//
// Difficulty:   Simple
// Author:       zlchen
// Date:         8/15/2019
// Performance:  8 ms, surpass 68.05%'s python3 submissions


class Solution {
public:
    string countAndSay(int n) {
        if(n == 1)
            return "1";

        // get last answer
        string tmp = countAndSay(n - 1);
        int times = 1, length = tmp.size(), i = 1;
        string ans;

        // recursion
        while(i){
            if(i < length){
                if(tmp[i - 1] == tmp[i])
                    times++;
                else
                    // not equal, append number and its times
                {
                    ans += to_string(times) + tmp[i - 1];
                    times = 1;   // reset times
                }
            }
            else{
                // we're in the end
                ans += to_string(times) + tmp[i - 1];
                break;
            }

            i++;
        }
        return ans;
    }
};
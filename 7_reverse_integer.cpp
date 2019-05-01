// Description:  给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
//               假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
//               请根据这个假设，如果反转后整数溢出那么就返回 0。
//
// Examples:     输入: 123,    输出: 321
//               输入: -123,   输出: -321
//               输入: 120,    输出: 21
//
// Author:       zlchen
// Date:         4/29/2019
// Performance:  16 ms, surpass 77.62%'s cpp submissions


class Solution {
public:
    int reverse(int x) {
        long res;
        if(x < 0)
        {
            string str = to_string(-(long)x);
            string temp(str.rbegin(), str.rend());
            res = -atol(temp.c_str());
        }
        else
        {
            string str = to_string((long)x);
            string temp(str.rbegin(), str.rend());
            res = atol(temp.c_str());
        }

        if(res >= - pow(2,31) && res <= pow(2,31) -1)
            return res;
        else
            return 0;
    }
};
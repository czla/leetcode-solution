// Description:  给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
//
//
// Examples:     输入: 1,      输出: true    解释: 2^0 = 1
//               输入: 16,     输出: true    解释: 2^4 = 16
//               输入: 218,    输出: false
//
// Difficulty:   Simple
// Author:       zlchen
// Date:         9/13/2019
// Performance:  8 ms, surpass 33.18%'s C++ submissions


class Solution {
public:
    bool isPowerOfTwo(int n) {
        double tmp = n;
        while(tmp > 1){
            tmp /= 2.0;
    }
        if(tmp == 1)
            return true;
        else
            return false;}
};
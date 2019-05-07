//Description:  将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
//              比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
//              L   C   I   R
//              E T O E S I I G
//              E   D   H   N
//              之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
//              请你实现这个将字符串进行指定行数变换的函数：
//              string convert(string s, int numRows);
//
//Examples:     输入: s = "LEETCODEISHIRING", numRows = 3, 输出: "LCIRETOESIIGEDHN"
//              输入: s = "LEETCODEISHIRING", numRows = 4, 输出: "LDREOEIIECIHNTSG"
//              解释:
//              L     D     R
//              E   O E   I I
//              E C   I H   N
//              T     S     G
//
//Difficulty:   Medium
//Author:       zlchen
//Date:         4/29/2019
//Performance:  120 ms, surpass 12.01%'s C++ submissions


class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1 || s.size() < 3)
            return s;

        string ans;
        int sep = 2 * numRows -2;

        for(int i = 0; i != numRows; ++i)
        {
            if(i == 0)
            {
                ans = slice(s, 0, sep);
                cout << "line 1 "<<ans<<endl;
                continue;
            }

            if(i == numRows - 1)
            {
                cout << "last line"<<endl;
                ans += slice(s, numRows - 1, sep);
                cout << "line n "<<ans <<endl;
                return ans;
            }

            string vertical_str, skew_str;
            vertical_str = slice(s, i, sep);
            skew_str = slice(s, 2 * numRows - 2 - i, sep);

            for(int j = 0; j != skew_str.size(); ++j)
            {
                vertical_str.insert(2 * j + 1, 1, skew_str[j]);
            }
            ans += vertical_str;
        }
        return ans;
    }

    string slice(string s, int start, int sep)
    {
        string substr;
        for(int i = start; i < s.size(); i += sep)
            substr += s[i];
        return substr;
    }
};
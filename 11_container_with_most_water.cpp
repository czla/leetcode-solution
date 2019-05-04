// Description:     给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
//                  在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
//                  找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
//
// Examples:        输入: [1,8,6,2,5,4,8,3,7],    输出: 49
//
// Difficulty:      Medium
// Author:          zlchen
// Date:            5/2/2019
// Performance:     24 ms, surpass 95.99%'s C++ submissions


class Solution {
public:
    int maxArea(vector<int>& height) {
        int length = height.size();
        int begin = 0, end = length-1;

        int ans = min(height[begin], height[end]) * (length - 1);

        while(begin < end){
            if(height[begin] < height[end])
                begin++;
            else
                end--;

            int area = min(height[begin], height[end]) * (end - begin);

            if(area > ans)
                ans = area;
        }

    return ans;
    }
};
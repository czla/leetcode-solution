// Description:  判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
//
//               数字 1-9 在每一行只能出现一次。
//               数字 1-9 在每一列只能出现一次。
//               数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
//
//
//               说明：
//                   * 一个有效的数独（部分已被填充）不一定是可解的。
//                   * 只需要根据以上规则，验证已经填入的数字是否有效即可。
//                   * 给定数独序列只包含数字 1-9 和字符 '.' 。
//                   * 给定数独永远是 9x9 形式的。
//
//
// Examples:     输入: [["5","3",".",".","7",".",".",".","."],
//                     ["6",".",".","1","9","5",".",".","."],
//                     [".","9","8",".",".",".",".","6","."],
//                     ["8",".",".",".","6",".",".",".","3"],
//                     ["4",".",".","8",".","3",".",".","1"],
//                     ["7",".",".",".","2",".",".",".","6"],
//                     [".","6",".",".",".",".","2","8","."],
//                     [".",".",".","4","1","9",".",".","5"],
//                     [".",".",".",".","8",".",".","7","9"]]
//               输出：true
//
//               输入: [["8","3",".",".","7",".",".",".","."],
//                     ["6",".",".","1","9","5",".",".","."],
//                     [".","9","8",".",".",".",".","6","."],
//                     ["8",".",".",".","6",".",".",".","3"],
//                     ["4",".",".","8",".","3",".",".","1"],
//                     ["7",".",".",".","2",".",".",".","6"],
//                     [".","6",".",".",".",".","2","8","."],
//                     [".",".",".","4","1","9",".",".","5"],
//                     [".",".",".",".","8",".",".","7","9"]]
//               输出：false
//
//
// Difficulty:   Medium
// Author:       zlchen
// Date:         8/13/2019
// Performance:  20 ms, surpass 72.18%'s python3 submissions


class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        map<int,int> tmp;
        vector<map<int, int>> rows(9, tmp);
        vector<map<int, int>> columns(9, tmp);
        vector<map<int, int>> boxes(9, tmp);

        for(int i = 0; i != 9; ++i){
            for(int j = 0; j != 9; ++j){
                char num = board[i][j];
                if(num != '.'){
                    int value = int(num);
                    int box_index = 3 * int(i / 3) + int(j / 3);

                    rows[i][num]++;
                    columns[j][num]++;
                    boxes[box_index][num]++;

                    if(rows[i][num] > 1 || columns[j][num] > 1 || boxes[box_index][num] > 1)
                        return false;
                }
            }
        }

        return true;
    }
};
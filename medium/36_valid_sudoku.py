# Description:  判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
#
#               数字 1-9 在每一行只能出现一次。
#               数字 1-9 在每一列只能出现一次。
#               数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
#
#
#               说明：
#                   * 一个有效的数独（部分已被填充）不一定是可解的。
#                   * 只需要根据以上规则，验证已经填入的数字是否有效即可。
#                   * 给定数独序列只包含数字 1-9 和字符 '.' 。
#                   * 给定数独永远是 9x9 形式的。
#
#
# Examples:     输入: [["5","3",".",".","7",".",".",".","."],
#                     ["6",".",".","1","9","5",".",".","."],
#                     [".","9","8",".",".",".",".","6","."],
#                     ["8",".",".",".","6",".",".",".","3"],
#                     ["4",".",".","8",".","3",".",".","1"],
#                     ["7",".",".",".","2",".",".",".","6"],
#                     [".","6",".",".",".",".","2","8","."],
#                     [".",".",".","4","1","9",".",".","5"],
#                     [".",".",".",".","8",".",".","7","9"]]
#               输出：true
#
#               输入: [["8","3",".",".","7",".",".",".","."],
#                     ["6",".",".","1","9","5",".",".","."],
#                     [".","9","8",".",".",".",".","6","."],
#                     ["8",".",".",".","6",".",".",".","3"],
#                     ["4",".",".","8",".","3",".",".","1"],
#                     ["7",".",".",".","2",".",".",".","6"],
#                     [".","6",".",".",".",".","2","8","."],
#                     [".",".",".","4","1","9",".",".","5"],
#                     [".",".",".",".","8",".",".","7","9"]]
#               输出：false
#
#
# Difficulty:   Medium
# Author:       zlchen
# Date:         8/13/2019
# Performance:  144 ms, surpass 21.34%'s python3 submissions


class Solution:
    def isValidSudoku(self, board) -> bool:
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if  num != '.':
                    num = int(num)
                    box_index = 3 * ( i // 3) + j // 3

                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False

        return True


    def isValid(self, nums):
        nums = [int(i) for i in nums if i != '.']
        return len(nums) == len(set(nums))

    def isValidSudoku2(self, board) -> bool:
        import functools
        for row in board:
            if not self.isValid(row):
                return False

        for i in range(9):
            column = [x[i] for x in board]
            if not self.isValid(column):
                return False

        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                part = [row[y:y+3] for row in board[x:x+3]]
                print(part)
                part = functools.reduce(list.__add__, part)
                print(part)
                if not self.isValid(part):
                    return False

        return True

if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(board))
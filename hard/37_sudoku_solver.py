# Description:  编写一个程序，通过已填充的空格来解决数独问题。
#
#               一个数独的解法需遵循如下规则：
#                   1. 数字 1-9 在每一行只能出现一次。
#                   2. 数字 1-9 在每一列只能出现一次。
#                   3. 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
#
#               注意:
#                   1. 给定的数独序列只包含数字 1-9 和字符 '.'
#                   2. 你可以假设给定的数独只有唯一解.
#                   3. 给定数独永远是 9x9 形式的.
#
# Examples:     输入: board = [["5","3",".",".","7",".",".",".","."],
#                             ["6",".",".","1","9","5",".",".","."],
#                             [".","9","8",".",".",".",".","6","."],
#                             ["8",".",".",".","6",".",".",".","3"],
#                             ["4",".",".","8",".","3",".",".","1"],
#                             ["7",".",".",".","2",".",".",".","6"],
#                             [".","6",".",".",".",".","2","8","."],
#                             [".",".",".","4","1","9",".",".","5"],
#                             [".",".",".",".","8",".",".","7","9"]]
#               修改后：board = [['5', '3', '4', '6', '7', '8', '9', '1', '2'],
#                               ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
#                               ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
#                               ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
#                               ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
#                               ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
#                               ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
#                               ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
#                               ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
#
# Difficulty:   Hard
# Author:       zlchen
# Date:         8/14/2019
# Performance:  240 ms, surpass 77.37%'s python3 submissions


class Solution:
    def solverSudoku(self, board):
        """
        :param board: List[List[str]]
        :return: void Do not return anything, modify board in-place instead.
        """

        def could_place(d, row, col):
            """
            Check if one could place number d in (row, col) cell
            :param d:
            :param row:
            :param col:
            :return: bool
            """
            return not (d in rows[row] or d in columns[col] or d in boxes[box_index(row, col)])

        def place_number(d, row, col):
            """
            Place number d in (row, col)
            :param d:
            :param row:
            :param col:
            :return: void
            """
            rows[row][d] = rows[row].get(d, 0) + 1
            columns[col][d] = columns[col].get(d, 0) + 1
            boxes[box_index(row, col)][d] = boxes[box_index(row, col)].get(d, 0) + 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            """
            Remove a number which doesn't lead to a solution
            :param d:
            :param row:
            :param col:
            :return: void
            """
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'

        def place_next_number(row, col):
            """
            Call backtrack function in recursion to continue to place numbers till we have solution
            :param row:
            :param col:
            :return: Void
            """
            # if we're in the last cell, then we have a solution
            if row == N - 1 and col == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            else:
                # go to next row if we're in the end of the row
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    # go to next column
                    backtrack(row, col + 1)

        def backtrack(row = 0, col = 0):
            """
            Backtracking
            :param row:
            :param col:
            :return:
            """
            # if the cell is empty
            if board[row][col] == '.':
                # iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_number(row, col)

                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_number(row, col)

        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        box_index = lambda row, col: n * (row // n) + (col // n)

        # init rows, columns and boxes
        rows = [{} for i in range(N)]
        columns = [{} for i in range(N)]
        boxes = [{} for i in range(N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)

        sudoku_solved = False
        backtrack()
        # return board

if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    print(Solution().solverSudoku(board))
# https://leetcode.com/problems/valid-sudoku/
# Determine if a 9x9 Sudoku board is valid. Only the filled cells need
# to be validated according to the following rules:
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the 9 3x3 sub-boxes of the grid must contain the digits
#    1-9 without repetition.
# The Sudoku board could be partially filled, where empty cells are
# filled with the character '.'
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# The given board contain only digits 1-9 and the character '.'.
# The given board size is always 9x9.

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row
        for x in range(9):
            row = set()
            for y in range(9):
                # first add the numeral to the row set
                if board[x][y] != ".":
                    if board[x][y] in row:
                        return False
                    else:
                        row.add(board[x][y])
                
                # secondly check the whole column for the current 'y'
                # but do it only in the first run! (x=0)
                if x == 0:
                    col = set()
                    for p in range(9):
                        if board[p][y] != ".":
                            if board[p][y] in col:
                                print("col", p, y)
                                return False
                            else:
                                col.add(board[p][y])

        # check each 3x3 square
        for x in (1, 4, 7):
            for y in (1, 4, 7):
                square = set()
                map_x = (x-1, x, x+1)
                map_y = (y-1, y, y+1)
                for p in map_x:
                    for q in map_y:
                        if board[p][q] != ".":
                            if board[p][q] in square:
                                return False
                            else:
                                square.add(board[p][q])

        return True


board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]]

board1 = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]
                        
board2 =    [[1, 3, 2, 5, 7, 9, 4, 6, 8]
            ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
            ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
            ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
            ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
            ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
            ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
            ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
            ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]

solution = Solution()
print(solution.isValidSudoku(board))
print(solution.isValidSudoku(board1))
print(solution.isValidSudoku(board2))
# https://leetcode.com/problems/surrounded-regions/

# Given a 2D board containing 'X' and 'O' (the letter O), capture all
# regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # don't do anything
        # it's too small for any 'O' to be surrounded
        if len(board) < 3 or len(board[0]) < 3:
            return None
        
        self.board = board
        self.max_x = len(board) - 1
        self.max_y = len(board[0]) - 1


        # check edges for 'O's and and replace them with 'P' (protected)
        # check neighbours of protected 'P's and protect them
        # if they are 'O's
        for row, _ in enumerate(board):
            for col, item in enumerate(board[row]):
                if row == 0 and item == 'O':
                    self.board[0][col] = 'P'
                    self.check_neighbours(0, col)
                elif row == self.max_x and item == 'O':
                    self.board[-1][col] = 'P'
                    self.check_neighbours(self.max_x, col)
                elif col == 0 and item == 'O':
                    self.board[row][0] = 'P'
                    self.check_neighbours(row, 0)
                elif col == self.max_y and item == 'O':
                    self.board[row][-1] = 'P'
                    self.check_neighbours(row, self.max_y)

        # iterate through entire board and replace 'P's with 'O's
        # and unprotected 'O's with 'X's
        for row, _ in enumerate(board):
            for col, item in enumerate(board[row]):
                if item == 'P':
                    self.board[row][col] = 'O'
                elif item == 'O':
                    self.board[row][col] = 'X'
  
    
    def check_neighbours(self, x, y):
        # a and x represent rows
        # b and y represent cols
        self.map_x_y = ((x-1, y), (x, y-1), (x, y+1), (x+1, y))

        for a, b in self.map_x_y:
            if 0 <= a <= self.max_x and 0 <= b <= self.max_y:
                if self.board[a][b] == 'O':
                    self.board[a][b] = 'P'
                    self.check_neighbours(a, b)
    

board = [['X','X','X','X'],
         ['X','O','O','X'],
         ['X','X','O','X'],
         ['X','O','X','X']]


for row in board:
    print(row)

solution = Solution()
solution.solve(board)

print()
for row in board:
    print(row)